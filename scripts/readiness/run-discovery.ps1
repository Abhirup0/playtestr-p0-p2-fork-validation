param(
    [string]$Runner = 'artifacts/qualified candidate extracted/playtestr_0.4.0-rc.1_windows_amd64/playtestr.exe',
    [string]$Output = 'artifacts/readiness-2026-09-26/discovery',
    [string[]]$Journeys = @('RW1','RW2','RW3','RW4','RW5','RW6')
)
$ErrorActionPreference = 'Stop'
$runnerPath = (Resolve-Path -LiteralPath $Runner).Path
$runnerHash = (Get-FileHash -LiteralPath $runnerPath -Algorithm SHA256).Hash.ToLower()
if ($runnerHash -ne '7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2') {
    throw 'Runner does not match frozen experiment identity'
}
if (Test-Path -LiteralPath $Output) { throw 'Use a new output directory; first attempts must remain intact' }
New-Item -ItemType Directory -Path $Output | Out-Null
$utf8 = New-Object Text.UTF8Encoding($false)
$rows = @(
    @('RW1','corpus/workflows/lazygit/rw1-neighbor.control','corpus/workflows/lazygit/rw1-neighbor-defect.control'),
    @('RW2','corpus/workflows/micro/rw2-reopen.control','corpus/workflows/micro/rw2-reopen-defect.control'),
    @('RW3','corpus/workflows/create-vite/create-vite-04.json','corpus/workflows/create-vite/rw3-invalid-correction-code-defect.control'),
    @('RW4','corpus/workflows/fzf/fzf-01.json','corpus/workflows/fzf/fzf-01-known-bad.control'),
    @('RW5','corpus/workflows/litecli/rw5-transaction.control','corpus/workflows/litecli/rw5-transaction-defect.control'),
    @('RW6','corpus/workflows/posting/rw6-edit-save-send.control','corpus/workflows/posting/rw6-edit-save-send-defect.control')
)
$pinPaths = @($runnerPath)
$pinPaths += @(Get-ChildItem -LiteralPath '.trial-private/corpus-tools' -Filter '*.exe' -File | Select-Object -ExpandProperty FullName)
$pinPaths += @('.trial-private/corpus-tools/lazygit-target/lazygit.exe')
foreach ($tree in @('corpus/controls','corpus/workflows/lazygit/fixture','corpus/workflows/micro/fixture','corpus/workflows/create-vite/fixture','corpus/workflows/fzf/fixture','corpus/workflows/litecli/fixture','corpus/workflows/posting/fixture','.trial-private/corpus-tools/create-vite-runtime/node_modules/create-vite','.trial-private/corpus-tools/create-vite-mutated-runtime/node_modules/create-vite','.trial-private/corpus-tools/create-vite-code-mutated-runtime/node_modules/create-vite')) {
    $pinPaths += @(Get-ChildItem -LiteralPath $tree -Recurse -File | Where-Object { $_.Extension -ne '.exe' } | Select-Object -ExpandProperty FullName)
}
$pins = @($pinPaths | Sort-Object -Unique | ForEach-Object { [ordered]@{path=$_;sha256=(Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLower()} })
[IO.File]::WriteAllText((Join-Path (Get-Location) (Join-Path $Output 'pins.json')),($pins|ConvertTo-Json -Depth 5),$utf8)
foreach ($row in $rows) {
    if ($Journeys -notcontains $row[0]) { continue }
    $attempts = @()
    for ($i=1; $i -le 5; $i++) { $attempts += ,@("good-$i",$row[1],0) }
    $attempts += ,@('defect',$row[2],1)
    $attempts += ,@('recovery',$row[1],0)
    foreach ($attempt in $attempts) {
        $id = "$($row[0])-$($attempt[0])"
        $report = Join-Path $Output "$id.json"
        $log = Join-Path $Output "$id.log"
        $artifact = Join-Path $Output "$id-artifacts"
        $before = @(Get-Process -Name lazygit,micro,fzf,litecli,posting,node -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
        $started = [DateTime]::UtcNow.ToString('o')
        $watch = [Diagnostics.Stopwatch]::StartNew()
        # Windows PowerShell wraps native stderr as ErrorRecord objects. An
        # intended negative must still be recorded before validating its exit.
        $ErrorActionPreference = 'Continue'
        $text = & $runnerPath test --artifacts-dir $artifact --report $report $attempt[1] 2>&1
        $exit = $LASTEXITCODE
        $ErrorActionPreference = 'Stop'
        $watch.Stop()
        [IO.File]::WriteAllText((Join-Path (Get-Location) $log), ($text -join "`n"), $utf8)
        $product = $null
        if (Test-Path -LiteralPath $report) { $product = Get-Content -LiteralPath $report -Raw | ConvertFrom-Json }
        $after = @(Get-Process -Name lazygit,micro,fzf,litecli,posting,node -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
        $survivors = @($after | Where-Object { $before -notcontains $_ })
        $record = [ordered]@{
            attempt_id=$id; host='windows_amd64'; started_utc=$started; spec=$attempt[1]
            spec_sha256=(Get-FileHash -LiteralPath $attempt[1] -Algorithm SHA256).Hash.ToLower()
            runner_sha256=$runnerHash; whole_command_ms=$watch.Elapsed.TotalMilliseconds
            exit=$exit; expected_exit=$attempt[2]; exit_matches=($exit -eq $attempt[2])
            report=$report; results=$product.results; new_selected_image_pids=$survivors
            survivor_probe_scope='post-command image census: lazygit,micro,fzf,litecli,posting,node; not all descendants'
            phase='six Windows core tasks; companion, variation, maintenance and native admission remain separate'
            command=@($runnerPath,'test','--artifacts-dir',$artifact,'--report',$report,$attempt[1])
        }
        [IO.File]::AppendAllText((Join-Path (Get-Location) (Join-Path $Output 'attempts.jsonl')), (($record | ConvertTo-Json -Compress -Depth 14)+"`n"), $utf8)
        Write-Output "$id exit=$exit expected=$($attempt[2]) wall_ms=$([Math]::Round($watch.Elapsed.TotalMilliseconds)) new_image_pids=$($survivors.Count)"
    }
}
if ((Get-FileHash -LiteralPath $runnerPath -Algorithm SHA256).Hash.ToLower() -ne $runnerHash) { throw 'Runner changed during campaign' }
