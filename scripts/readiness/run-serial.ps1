param([string]$Output='artifacts/readiness-2026-09-26/serial')
$ErrorActionPreference='Stop'
$root=(Get-Location).Path
$runner=(Resolve-Path -LiteralPath 'artifacts/qualified candidate extracted/playtestr_0.4.0-rc.1_windows_amd64/playtestr.exe').Path
$hash=(Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLower()
if($hash -ne '7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2'){throw 'Wrong runner pin'}
if(Test-Path -LiteralPath $Output){throw 'Evidence directory already exists'}
New-Item -ItemType Directory -Path $Output|Out-Null
$out=(Resolve-Path -LiteralPath $Output).Path
$utf8=New-Object Text.UTF8Encoding($false)
$sources=@('corpus/workflows/lazygit/rw1-resize.control','corpus/workflows/micro/micro-08.json','corpus/workflows/create-vite/create-vite-04.json','corpus/workflows/litecli/rw5-transaction.control','corpus/workflows/posting/rw6-slow-response.control')
New-Item -ItemType Directory -Path (Join-Path $out 'fixtures')|Out-Null
for($j=0;$j -lt $sources.Count;$j++){
    $s=Get-Content -LiteralPath $sources[$j] -Raw -Encoding UTF8|ConvertFrom-Json
    $base=Split-Path (Resolve-Path -LiteralPath $sources[$j]).Path
    Copy-Item -LiteralPath (Join-Path $base $s.workspace.fixture) -Destination (Join-Path $out "fixtures/$j") -Recurse
}
foreach($size in @(1,10,50)){
    $inputs=@()
    for($i=0;$i -lt $size;$i++){
        $j=$i%$sources.Count
        $s=Get-Content -LiteralPath $sources[$j] -Raw -Encoding UTF8|ConvertFrom-Json
        $base=Split-Path (Resolve-Path -LiteralPath $sources[$j]).Path
        $s.command[0]=[IO.Path]::GetFullPath((Join-Path $base ($s.command[0]+'.exe')))
        $s.workspace.fixture="fixtures/$j"
        $s.name="serial repeat $i of $($s.name)"
        $inputPath=Join-Path $out "size-$size-repeat-$i.json"
        [IO.File]::WriteAllText($inputPath,($s|ConvertTo-Json -Depth 8),$utf8)
        $inputs+=$inputPath
    }
    $report=Join-Path $out "size-$size-report.json"
    $artifact=Join-Path $out "size-$size-artifacts"
    $watch=[Diagnostics.Stopwatch]::StartNew()
    $ErrorActionPreference='Continue'
    $text=& $runner test --artifacts-dir $artifact --report $report @inputs 2>&1
    $exit=$LASTEXITCODE
    $ErrorActionPreference='Stop'
    $watch.Stop()
    [IO.File]::WriteAllText((Join-Path $out "size-$size.log"),($text -join "`n"),$utf8)
    $product=Get-Content -LiteralPath $report -Raw|ConvertFrom-Json
    $bytes=(Get-Item -LiteralPath $report).Length
    if(Test-Path -LiteralPath $artifact){$bytes+=(Get-ChildItem -LiteralPath $artifact -Recurse -File|Measure-Object Length -Sum).Sum}
    $row=[ordered]@{size=$size;host='windows_amd64';runner_sha256=$hash;exit=$exit;whole_command_ms=$watch.Elapsed.TotalMilliseconds;reported_results=@($product.results).Count;failed=@($product.results|Where-Object status -ne passed).Count;artifact_bytes=$bytes;cleanup_unconfirmed=@($product.results|Where-Object {-not $_.cleanup.confirmed_exited -or -not $_.workspace.cleaned}).Count;process_tree_cpu=$null;process_tree_rss=$null;memory_trend=$null;measurement_scope='one E1 serial correctness attempt, not 30-observation E2 performance cell';source_composition=$sources}
    [IO.File]::AppendAllText((Join-Path $out 'observations.jsonl'),(($row|ConvertTo-Json -Depth 6 -Compress)+"`n"),$utf8)
    Write-Output "size=$size exit=$exit results=$(@($product.results).Count) wall_ms=$([Math]::Round($watch.Elapsed.TotalMilliseconds))"
}
