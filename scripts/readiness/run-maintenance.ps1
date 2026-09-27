param([string]$Output='artifacts/readiness-2026-09-26/maintenance')
$ErrorActionPreference='Stop'
$runner=(Resolve-Path -LiteralPath 'artifacts/qualified candidate extracted/playtestr_0.4.0-rc.1_windows_amd64/playtestr.exe').Path
$hash=(Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLower()
if($hash -ne '7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2'){throw 'Wrong runner pin'}
if(Test-Path -LiteralPath $Output){throw 'Evidence directory exists; choose a new revision'}
New-Item -ItemType Directory -Path $Output|Out-Null
$utf8=New-Object Text.UTF8Encoding($false)
foreach($case in @(@('RW2','micro','rw2'),@('RW3','create-vite','rw3'),@('RW6','posting','rw6'))){
    foreach($phase in @(@('unmaintained',1),@('maintained',0),@('defect',1),@('recovery',0))){
        $variant=$phase[0]; if($variant -eq 'recovery'){$variant='maintained'}
        $spec="corpus/workflows/$($case[1])/$($case[2])-ui-$variant.control"
        $id="$($case[0])-$($phase[0])"
        $report=Join-Path $Output "$id.json"
        $artifact=Join-Path $Output "$id-artifacts"
        $watch=[Diagnostics.Stopwatch]::StartNew()
        $ErrorActionPreference='Continue'
        $text=& $runner test --artifacts-dir $artifact --report $report $spec 2>&1
        $exit=$LASTEXITCODE
        $ErrorActionPreference='Stop'
        $watch.Stop()
        [IO.File]::WriteAllText((Join-Path (Get-Location) (Join-Path $Output "$id.log")),($text -join "`n"),$utf8)
        $product=Get-Content -LiteralPath $report -Raw|ConvertFrom-Json
        $row=[ordered]@{attempt_id=$id;host='windows_amd64';spec=$spec;spec_sha256=(Get-FileHash -LiteralPath $spec -Algorithm SHA256).Hash.ToLower();runner_sha256=$hash;exit=$exit;expected_exit=$phase[1];exit_matches=($exit -eq $phase[1]);whole_command_ms=$watch.Elapsed.TotalMilliseconds;results=$product.results;report=$report;maintenance_kind='synthetic realistic UI change; not upstream version upgrade';active_authoring_minutes=$null}
        [IO.File]::AppendAllText((Join-Path (Get-Location) (Join-Path $Output 'attempts.jsonl')),(($row|ConvertTo-Json -Depth 14 -Compress)+"`n"),$utf8)
        Write-Output "$id exit=$exit expected=$($phase[1]) wall_ms=$([Math]::Round($watch.Elapsed.TotalMilliseconds))"
    }
}
