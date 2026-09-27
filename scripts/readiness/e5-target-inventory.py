"""Record actual retained target/runtime bytes without collecting environments."""
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rows=[]
for path in sorted((ROOT/'.trial-private/corpus-tools').rglob('*')):
    selected=path.suffix.lower() in ['.exe','.dll','.pyd'] or path.name in ['package-lock.json','qualification-targets.txt'] or (path.name=='package.json' and path.parent.name in ['package','create-vite','npkill','ipm-cli']) or (path.suffix=='' and path.name in ['gum','lazygit','btm','micro','gitui','tv','fzf','tig','task','taskwarrior-tui'])
    if not selected: continue
    if not path.is_file() or path.is_symlink() or any(part.endswith('-runs') for part in path.parts): continue
    with path.open('rb') as stream: digest=hashlib.file_digest(stream,'sha256').hexdigest()
    rows.append(dict(path=str(path.relative_to(ROOT)),sha256=digest,bytes=path.stat().st_size))
outside=ROOT/'.trial-private/r3c/windows/rs-02-gitui/bin/gitui.exe'
rows.append(dict(path=str(outside.relative_to(ROOT)),sha256=hashlib.sha256(outside.read_bytes()).hexdigest(),bytes=outside.stat().st_size))
versions={name:subprocess.check_output(command,text=True).strip() for name,command in
          [('python',['python','--version']),('node',['node','--version']),('git',['git','--version']),('go',['go','version'])]}
out=ROOT/'artifacts/e5-corpus/actual-target-inventory.json'
out.write_text(json.dumps(dict(versions=versions,files=rows,scope='Retained native Windows and WSL target files; source/npm/pip pins remain attributed to corpus records. No environment or command-line inventory.'),indent=2)+'\n')
print(versions,len(rows),'target/runtime/package file identities')
