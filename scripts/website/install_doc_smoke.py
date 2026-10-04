"""Exercise the published rc.3 install commands and linked greeting recipe."""
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import tomllib
import urllib.request

repo = Path(__file__).resolve().parents[2]
data = tomllib.loads((repo / "site/data/prerelease.toml").read_text(encoding='utf8'))
host = {"Windows": "windows", "Linux": "linux", "Darwin": "darwin"}[platform.system()]
target = next(x for x in data["targets"] if "_" + host + "_" in x["archive"])
work = repo / "artifacts" / ("website-onboarding-" + os.getenv("ONBOARDING_RUN", host))
work.mkdir(parents=True, exist_ok=True)
if (work / "playtestr rc3").exists():
    raise SystemExit("Use a fresh onboarding directory; previous evidence exists")
for filename in (target["archive"], target["archive"] + ".sha256"):
    local = os.getenv("ARCHIVES_DIR")
    if local:
        content = (Path(local) / filename).read_bytes()
    else:
        url = "https://github.com/Wyrcan-io/playtestr/releases/download/" + data["version"] + "/" + filename
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read(32 * 1024 * 1024 + 1)
        if len(content) > 32 * 1024 * 1024:
            raise SystemExit("Archive exceeds download budget")
    (work / filename).write_bytes(content)
assert hashlib.sha256((work / target["archive"]).read_bytes()).hexdigest() == target["sha256"]
guide = (repo / "site/content/docs/prerelease-installation.md").read_text(encoding='utf8')
blocks = re.findall(r"```(?:powershell|sh)\n(.*?)```", guide, re.S)
command = blocks[{"windows": 0, "linux": 1, "darwin": 2}[host]]
run = subprocess.run([shutil.which("pwsh") or "powershell.exe", "-NoProfile", "-Command", "$ErrorActionPreference='Stop';\n" + command] if host == "windows" else ["sh", "-eu", "-c", command], cwd=work, capture_output=True, text=True, timeout=90)
assert run.returncode == 0, run.stderr + run.stdout
assert "playtestr " + data["version"] in run.stdout, run.stdout
walkthrough = (repo / "docs/releases/v0.1.0-installation-walkthrough.md").read_text(encoding='utf8')
recipes = re.findall(r"```(sh|batch|json)\n(.*?)```", walkthrough, re.S)
kind = "batch" if host == "windows" else "sh"
hello = next(body for lang, body in recipes if lang == kind and ("set /p" in body or "#!/bin/sh" in body))
file = work / ("hello.cmd" if host == "windows" else "hello.sh")
file.write_text(hello, encoding='utf8')
if host != "windows": file.chmod(0o755)
specs = [json.loads(body) for lang, body in recipes if lang == "json"]
spec = specs[1 if host == "windows" else 0]
archive_dir = target["archive"].removesuffix(".zip").removesuffix(".tar.gz")
binary = work / "playtestr rc3" / archive_dir / ("playtestr.exe" if host == "windows" else "playtestr")
results = []
for label, expectation, code in [("pass", "Hello, terminal tester!", 0), ("intentional-failure", "Hello, wrong!", 1), ("recovery", "Hello, terminal tester!", 0)]:
    spec["steps"][3]["expect"] = expectation
    (work / "hello.json").write_text(json.dumps(spec), encoding='utf8')
    report = work / (label + ".json")
    result = subprocess.run([str(binary), "test", "--report", str(report), "hello.json"], cwd=work, capture_output=True, text=True, timeout=30)
    assert result.returncode == code, result.stderr + result.stdout
    record = json.loads(report.read_text(encoding='utf8'))
    assert record["summary"]["passed" if code == 0 else "failed"] == 1, record
    results.append({"case": label, "exit": code})
evidence = {"host": platform.platform(), "version": data["version"], "sha256": target["sha256"], "install_output": run.stdout.strip(), "cases": results}
(repo / "artifacts" / ("website-onboarding-" + host + ".json")).write_text(json.dumps(evidence, indent=2), encoding='utf8')
print(json.dumps(evidence, indent=2))
