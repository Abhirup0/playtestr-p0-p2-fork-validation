"""Pinned native E1 target preparation; never runs holdout targets."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / '.trial-private/corpus-tools'
SOURCES = ROOT / '.trial-private/readiness-sources'
OUT = ROOT / 'artifacts/readiness-native'
GOOS = subprocess.check_output(['go', 'env', 'GOOS'], text=True).strip()
if GOOS not in ('linux', 'darwin'):
    raise SystemExit('This preparer admits native Linux/macOS only')
for path in (TOOLS, SOURCES, OUT):
    path.mkdir(parents=True, exist_ok=True)
ledger = []

def run(args, cwd=ROOT):
    started = time.monotonic()
    subprocess.run([str(x) for x in args], cwd=cwd, check=True, timeout=1200)
    ledger.append({'command': [str(x) for x in args], 'cwd':str(Path(cwd).relative_to(ROOT)), 'elapsed_ms': (time.monotonic()-started)*1000})

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def clone(name, repo, commit):
    destination = SOURCES/name
    if destination.exists():
        raise RuntimeError('Refuse existing source tree: '+str(destination))
    run(['git', 'init', '-q', destination])
    run(['git', 'remote', 'add', 'origin', repo], destination)
    run(['git', 'fetch', '--depth', '1', 'origin', commit], destination)
    run(['git', 'checkout', '--detach', 'FETCH_HEAD'], destination)
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=destination,text=True).strip()==commit
    return destination

def patch(path, old, new):
    content=path.read_text()
    if content.count(old)!=1:
        raise RuntimeError('Nonunique reviewed mutation anchor: '+str(path))
    before=sha(path)
    path.write_text(content.replace(old,new))
    ledger.append({'mutation':str(path.relative_to(ROOT)), 'before_sha256':before,'after_sha256':sha(path)})

def variant(source, name, file, old, new):
    destination=TOOLS/name
    if destination.exists(): raise RuntimeError('Variant already exists')
    shutil.copytree(source,destination)
    patch(destination/file,old,new)
    return destination

try:
    lazy=clone('lazygit','https://github.com/jesseduffield/lazygit.git','c07f4d381b90419583b7ce04f87379654d983ebc')
    (TOOLS/'lazygit-target').mkdir(exist_ok=True)
    run(['go','build','-trimpath','-o',TOOLS/'lazygit-target/lazygit','.'],lazy)
    patch(lazy/'pkg/commands/git_commands/working_tree.go',
          'cmdArgs := NewGitCmd("add").\n\t\tArg(extraArgs...).\n\t\tArg("--").\n\t\tArg(paths...).\n\t\tToArgv()\n\n\treturn self.cmd.New(cmdArgs).Run()',
          '_, _ = paths, extraArgs\n\treturn nil')
    run(['go','build','-trimpath','-o',TOOLS/'lazygit-mutated.exe','.'],lazy)
    micro=clone('micro','https://github.com/zyedidia/micro.git','04c577049ca898f097cd6a2dae69af0b4d4493e1')
    run(['go','build','-trimpath','-o',TOOLS/'micro.exe','./cmd/micro'],micro)
    patch(micro/'internal/buffer/save.go','if fileSize, e = file.Write(b.lines[0].data); e != nil {',
          'firstLine := bytes.TrimPrefix(b.lines[0].data, []byte("edited "))\n\t\tif fileSize, e = file.Write(firstLine); e != nil {')
    run(['go','build','-trimpath','-o',TOOLS/'micro-mutated.exe','./cmd/micro'],micro)
    fzf=clone('fzf','https://github.com/junegunn/fzf.git','a140afeb4d733cad3c96a56bf6db7e26853b6757')
    run(['go','build','-trimpath','-o',TOOLS/'fzf','.'],fzf)
    run(['go','build','-trimpath','-o',TOOLS/'fzf-mutated','.'],ROOT/'corpus/controls/fzf-mutated')
    runtime=TOOLS/'create-vite-runtime'
    runtime.mkdir()
    run(['npm','pack','create-vite@9.2.1'],runtime)
    tarball=runtime/'create-vite-9.2.1.tgz'
    assert sha(tarball)=='4dd92d0e734e96e88ec8afd8c0153f6a9446156205460a995b978b63b49b4eb8'
    run(['npm','install','--ignore-scripts','--no-audit','--no-fund',str(tarball)],runtime)
    variant(runtime,'create-vite-code-mutated-runtime','node_modules/create-vite/dist/index.js',
            'D.name=m,T(`package.json`','D.name=m,D.type=`commonjs`,T(`package.json`')
    template_bad=variant(runtime,'create-vite-mutated-runtime','node_modules/create-vite/template-vanilla/package.json',
                         '"type": "module"','"type": "commonjs"')
    for source,name in [(runtime,'create-vite-ui-runtime'),(template_bad,'create-vite-ui-mutated-runtime')]:
        v=variant(source,name,'node_modules/create-vite/dist/index.js','Select a framework:','Choose a framework:')
        patch(v/'node_modules/create-vite/dist/index.js','Select a variant:','Choose a variant:')
    for project,ident,wheelhash in [('posting','py-01-posting','c0fd982a22ddeb9fb01f85f89045600f440452dda7b47d69eb0944264a3b88dc'),('litecli','py-02-litecli','4d1743dfa086b178de6543b36f1780203e8a9bc99643af4b721f6c880c5aa7a9')]:
        env=ROOT/'.trial-private/r3c'/GOOS/ident/'venv'
        run([sys.executable,'-m','venv',env])
        python=env/'bin/python'
        wheels=OUT/(project+'-wheels')
        run([python,'-m','pip','download','-r',ROOT/'scripts/readiness'/(project+'-requirements.txt'),'-d',wheels])
        targetwheel=next(wheels.glob(project+'-*.whl'))
        assert sha(targetwheel)==wheelhash
        run([python,'-m','pip','install','--no-index','--find-links',wheels,'-r',ROOT/'scripts/readiness'/(project+'-requirements.txt')])
        installed=subprocess.check_output([python,'-c','import '+project+';print('+project+'.__path__[0])'],text=True).strip()
        source=Path(installed)
        if project=='posting':
            bad=variant(source,'posting-save-mutated/posting','collection.py','path.write_text(yaml_content, encoding="utf-8")',
                        'path.write_text(yaml_content.replace("http://127.0.0.1:28741/saved", "http://127.0.0.1:28741/stale"), encoding="utf-8")')
            for original,name in [(source,'posting-ui-changed/posting'),(bad,'posting-ui-save-mutated/posting')]:
                variant(original,name,'app.py','Request saved','Request stored')
        else:
            variant(source,'litecli-state-mutated/litecli','sqlexecute.py','cur.execute(sql)',
                    '''cur.execute(sql.replace("'gamma','three'", "'gamma','wrong'"))''')
    for project in ['lazygit','micro','create-vite','posting','litecli']:
        run(['go','build','-trimpath','-o',TOOLS/(project+'-oracle'),'.'],ROOT/'corpus/controls'/(project+'-oracle'))
    # Freeze inputs before running task controls; wheels stay out of uploaded logs.
    inputs=[p for p in TOOLS.rglob('*') if p.is_file() and 'node_modules/.cache' not in str(p)]
    inputs += [p for p in OUT.glob('*-wheels/*') if p.is_file()]
    (OUT/'target-pins.json').write_text(json.dumps([{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in sorted(inputs)],indent=2)+'\n')
finally:
    (OUT/'setup-operations.json').write_text(json.dumps(ledger,indent=2)+'\n')
