"""Prepare two reviewed Lazygit maintenance variants, retaining patch identities."""
import hashlib
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
tools=ROOT/'.trial-private/corpus-tools'
source=ROOT/('.trial-private/source/lazygit-v0.65.0' if os.name=='nt' else '.trial-private/readiness-sources/lazygit')
suffix='.exe' if os.name=='nt' else ''
parser=argparse.ArgumentParser()
parser.add_argument('--resume-owned-preparation',action='store_true')
args=parser.parse_args()
out=ROOT/('artifacts/e4-setup-r2' if args.resume_owned_preparation else 'artifacts/e4-setup')
out.mkdir(parents=True,exist_ok=False)
rows=[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def build(cwd,target):
    tick=time.monotonic()
    subprocess.run(['go','build','-trimpath','-o',str(target),'.'],cwd=cwd,check=True,timeout=600)
    rows.append(dict(operation='build',source=str(cwd.relative_to(ROOT)),binary=str(target.relative_to(ROOT)),
        sha256=sha(target),elapsed_ms=(time.monotonic()-tick)*1000))
def patch(path,old,new):
    text=path.read_text(); assert text.count(old)==1,(path,old)
    before=sha(path); path.write_text(text.replace(old,new))
    rows.append(dict(operation='synthetic patch',file=str(path.relative_to(ROOT)),old=old,new=new,before_sha256=before,after_sha256=sha(path)))
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()=='c07f4d381b90419583b7ce04f87379654d983ebc'
for number in (1,2):
    for label in ('good','bad'):
        destination=tools/f'e4-lazygit-{number}-{label}'; destination.mkdir(exist_ok=args.resume_owned_preparation)
        targetdir=destination/'lazygit-target'; targetdir.mkdir(exist_ok=args.resume_owned_preparation)
        oracle=ROOT/'.trial-private'/f'e4-oracle-{number}-{label}'
        if not oracle.exists(): shutil.copytree(ROOT/'corpus/controls/lazygit-oracle',oracle)
        if number==2:
            path=oracle/'main.go'; text=path.read_text(); assert 'alpha.txt' in text
            path.write_text(text.replace('alpha.txt','aardvark.txt'))
            rows.append(dict(operation='synthetic fixture filename maintenance',file=str(path.relative_to(ROOT)),sha256=sha(path)))
            binary=tools/('lazygit-mutated.exe' if label=='bad' else 'lazygit-target/lazygit'+suffix)
            shutil.copy2(binary,targetdir/('lazygit'+suffix))
        else:
            variant=ROOT/'.trial-private'/f'e4-lazy-source-{label}'
            if not variant.exists(): shutil.copytree(source,variant,ignore=shutil.ignore_patterns('.git'))
            # Native E1 preparation retains its target mutation in the source
            # tree. Reconstruct this one reviewed file from the pinned commit.
            stagefile='pkg/commands/git_commands/working_tree.go'
            pristine=subprocess.check_output(['git','show','HEAD:'+stagefile],cwd=source)
            (variant/stagefile).write_bytes(pristine)
            labelpath=variant/'pkg/i18n/english.go'
            if '"Staged changes"' in labelpath.read_text(): patch(labelpath,'"Staged changes"','"Indexed changes"')
            else: assert labelpath.read_text().count('"Indexed changes"')==1
            if label=='bad':
                patch(variant/'pkg/commands/git_commands/working_tree.go',
                    'cmdArgs := NewGitCmd("add").\n\t\tArg(extraArgs...).\n\t\tArg("--").\n\t\tArg(paths...).\n\t\tToArgv()\n\n\treturn self.cmd.New(cmdArgs).Run()',
                    '_, _ = paths, extraArgs\n\treturn nil')
            build(variant,targetdir/('lazygit'+suffix))
        build(oracle,destination/('lazygit-oracle'+suffix))
        rows.append(dict(operation='target identity',file=str((targetdir/('lazygit'+suffix)).relative_to(ROOT)),sha256=sha(targetdir/('lazygit'+suffix))))
        (out/'setup.json').write_text(json.dumps(rows,indent=2)+'\n')
