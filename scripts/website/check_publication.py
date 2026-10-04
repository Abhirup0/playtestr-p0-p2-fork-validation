"""Bounded production route and asset verification for the built project site."""
import concurrent.futures
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

base = "https://wyrcan-io.github.io/playtestr/"
root = Path(sys.argv[1] if len(sys.argv) > 1 else "artifacts/website-redesign-preview")
paths = [str(x.relative_to(root)).replace("\\", "/").removesuffix("index.html") for x in root.rglob("*.html") if x.name != "404.html"]
paths += [str(x.relative_to(root)).replace("\\", "/") for x in root.rglob("*.json")]
paths += ["sitemap.xml", "robots.txt", "favicon.svg", "images/social-preview.png", "demos/README.txt"]
class Assets(HTMLParser):
    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "script" and "src" in attrs: paths.append(attrs["src"].removeprefix("/playtestr/"))
        if tag == "link" and attrs.get("rel") == "stylesheet": paths.append(attrs["href"].removeprefix("/playtestr/"))
Assets().feed((root / "index.html").read_text(encoding="utf8"))
def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Playtestr-website-validation"}), timeout=30) as response:
            return {"url": url, "status": response.status, "content_type": response.headers.get("Content-Type"), "body": response.read(4 * 1024 * 1024).decode("utf8", errors="replace")}
    except urllib.error.HTTPError as error:
        return {"url": url, "status": error.code, "body": error.read(4096).decode("utf8", errors="replace")}
    except Exception as error:
        return {"url": url, "status": 0, "error": str(error), "body": ""}
urls = [base + p for p in sorted(set(paths))] + [base + "missing-publication-check/", "https://wyrcan-io.github.io/robots.txt"]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results = list(pool.map(fetch, urls))
errors = [r for r in results[:-2] if r["status"] != 200]
if results[-2]["status"] != 404: errors.append(results[-2])
home = next(r for r in results if r["url"] == base)
if not all(term in home["body"] for term in ("Test the terminal.", "v0.4.0-rc.3", "See what changed.")): errors.append({"error": "Homepage does not match reviewed release/design"})
for result in results: result.pop("body", None)
record = {"base": base, "checked": len(results), "results": results, "errors": errors, "robots_scope": "Only host-root robots.txt controls crawl policy; project robots is informational"}
Path("artifacts/website-production-http.json").write_text(json.dumps(record, indent=2), encoding="utf8")
print(json.dumps({"checked":len(results), "errors":errors, "host_root_robots":results[-1]},indent=2))
raise SystemExit(bool(errors))
