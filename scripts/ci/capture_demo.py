#!/usr/bin/env python3
"""Reproduce pass/seeded-defect/recovery using an existing published runner."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runner", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("artifacts/adoption-demo"))
    args = parser.parse_args()
    runner = args.runner.resolve(strict=True)
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / "artifacts"):
        parser.error("output must be inside this repository's artifacts directory")
    if output.exists():
        parser.error("output must be fresh; previous evidence is preserved")
    output.mkdir(parents=True)
    suffix = ".exe" if sys.platform == "win32" else ""
    target = output / "bin" / ("demo" + suffix)
    target.parent.mkdir()
    source_spec = ROOT / "examples/menu.json"
    spec = json.loads(source_spec.read_text(encoding="utf-8"))
    spec["command"] = ["./" + target.relative_to(ROOT).as_posix()]
    spec_path = output / "menu.json"
    spec_path.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    (output / "snapshots").mkdir()
    baseline = output / "snapshots/diagnostics.txt"
    shutil.copyfile(ROOT / "examples/snapshots/diagnostics.txt", baseline)
    records = []
    transcript = []

    def execute(label, command, expected=0):
        result = subprocess.run([str(x) for x in command], cwd=ROOT,
                                capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=120)
        (output / (label + ".log")).write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode != expected:
            raise RuntimeError(f"{label}: expected {expected}, got {result.returncode}; inspect its log")
        return result

    version = execute("version", [runner, "--version"]).stdout.strip()
    if version != "playtestr v0.4.0-rc.3":
        raise RuntimeError("This capture is pinned to published v0.4.0-rc.3")
    transcript += [version, "Repository-owned demo; REGRESSION is a deliberately seeded defect."]
    original_spec_hash, baseline_hash = sha(spec_path), sha(baseline)
    for label, defect, expected in (("pass", False, 0), ("seeded-defect", True, 1), ("recovery", False, 0)):
        build = ["go", "build"]
        if defect:
            build += ["-ldflags", "-X main.diagnosticsSuffix=REGRESSION"]
        build += ["-o", target, "./cmd/demo"]
        execute(label + "-build", build)
        report = output / label / "results.json"
        evidence_root = report.parent
        # Relative references keep Windows drive prefixes out of the renderer's
        # URI rejection path and reproduce the documented adopter workflow.
        command = [runner, "test", "--artifacts-dir", (evidence_root / "screens").relative_to(ROOT).as_posix(),
                   "--report", report.relative_to(ROOT).as_posix(), spec_path.relative_to(ROOT).as_posix()]
        result = execute(label, command, expected)
        document = json.loads(report.read_text(encoding="utf-8"))
        item = document["results"][0]
        if item["status"] != ("failed" if defect else "passed"):
            raise RuntimeError("Unexpected captured outcome")
        if not item["cleanup"]["confirmed_exited"]:
            raise RuntimeError("Target cleanup was not confirmed")
        if defect and item["failure"]["category"] != "snapshot_mismatch":
            raise RuntimeError("The seeded defect did not produce the expected screen diff")
        if sha(spec_path) != original_spec_hash or sha(baseline) != baseline_hash:
            raise RuntimeError("Spec or baseline changed during capture")
        execute(label + "-html", [runner, "report", "--input", report,
                                  "--evidence-root", evidence_root,
                                  "--output", evidence_root / "report.html"])
        execute(label + "-summary", [sys.executable, ROOT / "scripts/ci/report_summary.py",
                                     "--input", report, "--evidence-root", evidence_root,
                                     "--output", evidence_root / "summary.md",
                                     "--setup-outcome", "success", "--prepare-outcome", "success",
                                     "--test-outcome", "failure" if defect else "success",
                                     "--html-outcome", "success"])
        records.append({"case": label, "test_exit": result.returncode,
                        "status": item["status"], "category": (item.get("failure") or {}).get("category"),
                        "cleanup_confirmed": item["cleanup"]["confirmed_exited"],
                        "target_sha256": sha(target), "report_sha256": sha(report),
                        "spec_sha256": original_spec_hash, "baseline_sha256": baseline_hash,
                        "evidence_directory": evidence_root.relative_to(ROOT).as_posix()})
        # Retain complete logs privately; compact presentation never fabricates output.
        transcript += ["", f"{label}: actual exit {result.returncode}", result.stdout.strip()]
        if defect:
            diff = Path(item["evidence"]["diff_path"])
            transcript += [diff.read_text(encoding="utf-8")]
    metadata = {"runner_version": version, "runner_sha256": sha(runner),
                "host": sys.platform, "target_source_sha256": sha(ROOT / "cmd/demo/main.go"),
                "cases": records, "disclosure": "Operator-run synthetic target defect; not independent adoption"}
    (output / "capture.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    (output / "transcript.txt").write_text("\n".join(transcript) + "\n", encoding="utf-8")
    print("Verified pass 0, seeded snapshot mismatch 1, unchanged recovery 0; cleanup confirmed.")


if __name__ == "__main__":
    main()
