param(
    [string]$Output = 'artifacts/readiness-2026-09-26/windows-measurements',
    [int]$Samples = 30,
    [int[]]$Sizes = @(1,10,50),
    [switch]$ObserveTree
)
$ErrorActionPreference = 'Stop'
if ($Samples -lt 1 -or $Samples -gt 100) { throw 'Samples must be 1..100' }
if (@($Sizes | Where-Object { $_ -notin @(1,10,50) }).Count) { throw 'Unsupported suite size' }
$root = (Get-Location).Path
$runner = (Resolve-Path -LiteralPath 'artifacts/qualified candidate extracted/playtestr_0.4.0-rc.1_windows_amd64/playtestr.exe').Path
$hash = (Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLower()
if ($hash -ne '7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2') { throw 'Runner pin mismatch' }
if (Test-Path -LiteralPath $Output) { throw 'Use a fresh evidence directory' }
New-Item -ItemType Directory -Path $Output | Out-Null
$out = (Resolve-Path -LiteralPath $Output).Path
$utf8 = New-Object Text.UTF8Encoding($false)
if ($ObserveTree) { Get-CimInstance Win32_Process -Filter "ProcessId=$PID" | Out-Null }
$inputs = @{}
$pins = @()
foreach ($size in $Sizes) {
    $inputs[$size] = @(Get-ChildItem -LiteralPath 'artifacts/readiness-2026-09-26/serial' -Filter "size-$size-repeat-*.json" -File | Sort-Object Name | Select-Object -ExpandProperty FullName)
    if ($inputs[$size].Count -ne $size) { throw "Missing prepared size-$size inputs" }
    foreach ($file in $inputs[$size]) { $pins += [ordered]@{path=$file;sha256=(Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLower()} }
}
[IO.File]::WriteAllText((Join-Path $out 'input-pins.json'), ($pins | ConvertTo-Json -Depth 5), $utf8)
# Process counters here cover the runner only. Target CPU/RSS and exited children
# cannot be reconstructed from these samples and remain explicitly unknown.
for ($sample = 1; $sample -le $Samples; $sample++) {
    # Reverse alternate suite-size order to reduce systematic temporal bias.
    $order = @($Sizes)
    if ($sample % 2 -eq 0) { [array]::Reverse($order) }
    foreach ($size in $order) {
        $id = "size-$size-sample-$sample"
        $report = Join-Path $out "$id.json"
        $artifact = Join-Path $out "$id-artifacts"
        $arguments = @('test','--artifacts-dir',$artifact,'--report',$report) + $inputs[$size]
        # Every argument is a controlled path or literal; Windows native paths
        # cannot contain quotes. Quote paths with spaces for Start-Process.
        $quoted = @($arguments | ForEach-Object { '"' + $_ + '"' })
        $watch = [Diagnostics.Stopwatch]::StartNew()
        $process = Start-Process -FilePath $runner -ArgumentList $quoted -WorkingDirectory $root -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $out "$id.stdout.log") -RedirectStandardError (Join-Path $out "$id.stderr.log")
        # Retain the process handle before Refresh/HasExited so Windows
        # PowerShell can still retrieve its exit code after termination.
        $processHandle = $process.Handle
        $rss = @()
        $cpu = $null
        $owned = @{}
        $treePeak = 0L
        $survivors = $null
        $deadlineMs = 30000 * $size + 10000
        try {
            while (-not $process.HasExited) {
                if ($watch.ElapsedMilliseconds -gt $deadlineMs) {
                    & taskkill.exe /PID $process.Id /T /F | Out-Null
                    throw "Bounded harness deadline reached: $id"
                }
                try { $process.Refresh(); $rss += [long]$process.WorkingSet64; $cpu = $process.TotalProcessorTime.TotalMilliseconds } catch { }
                if ($ObserveTree) {
                    # Do not record command lines, arguments or environment.
                    $inventory = @(Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,CreationDate)
                    $reachable = @{}
                    $reachable[[int]$process.Id] = $process.StartTime.ToUniversalTime()
                    do {
                        $added = $false
                        foreach ($item in $inventory) {
                            # Parent IDs persist after a parent exits and may be
                            # reused. A genuine child cannot predate its parent.
                            if ($reachable.ContainsKey([int]$item.ParentProcessId) -and -not $reachable.ContainsKey([int]$item.ProcessId) -and $item.CreationDate.ToUniversalTime() -ge $reachable[[int]$item.ParentProcessId]) {
                                $reachable[[int]$item.ProcessId] = $item.CreationDate.ToUniversalTime(); $added = $true
                            }
                        }
                    } while ($added)
                    $liveBytes = 0L
                    foreach ($item in $inventory | Where-Object { $reachable.ContainsKey([int]$_.ProcessId) }) {
                        $identity = "$($item.ProcessId):$($item.CreationDate.ToUniversalTime().Ticks)"
                        if (-not $owned.ContainsKey($identity)) { $owned[$identity] = [ordered]@{pid=[int]$item.ProcessId;name=$item.Name;creation_utc=$item.CreationDate.ToUniversalTime().ToString('o');max_observed_cpu_ms=0} }
                        try {
                            $child = Get-Process -Id $item.ProcessId -ErrorAction Stop
                            # CIM rounds creation timestamps to microseconds.
                            if ([math]::Abs(($child.StartTime.ToUniversalTime() - $item.CreationDate.ToUniversalTime()).TotalMilliseconds) -ge 1) { continue }
                            $owned[$identity].max_observed_cpu_ms = [math]::Max($owned[$identity].max_observed_cpu_ms, $child.TotalProcessorTime.TotalMilliseconds)
                            $liveBytes += $child.WorkingSet64
                        } catch { }
                    }
                    $treePeak = [math]::Max($treePeak, $liveBytes)
                }
                Start-Sleep -Milliseconds 100
            }
            $process.WaitForExit()
            $watch.Stop()
            $exit = $process.ExitCode
            if ($ObserveTree) {
                $survivors = @()
                foreach ($record in $owned.Values) {
                    try {
                        $child = Get-Process -Id $record.pid -ErrorAction Stop
                        if ([math]::Abs(($child.StartTime.ToUniversalTime() - [datetime]::Parse($record.creation_utc).ToUniversalTime()).TotalMilliseconds) -lt 1) { $survivors += $record }
                    } catch { }
                }
            }
            $product = Get-Content -LiteralPath $report -Raw -Encoding UTF8 | ConvertFrom-Json
            $bytes = (Get-Item -LiteralPath $report).Length
            if (Test-Path -LiteralPath $artifact) { $bytes += (Get-ChildItem -LiteralPath $artifact -Recurse -File | Measure-Object Length -Sum).Sum }
            $row = [ordered]@{
                attempt_id=$id;size=$size;sample=$sample;host='windows_amd64';runner_sha256=$hash
                whole_command_ms=$watch.Elapsed.TotalMilliseconds;exit=$exit
                passed=@($product.results | Where-Object status -eq passed).Count
                failed=@($product.results | Where-Object status -ne passed).Count
                cleanup_unconfirmed=@($product.results | Where-Object { -not $_.cleanup.confirmed_exited -or -not $_.workspace.cleaned }).Count
                artifact_bytes=$bytes;runner_sampled_cpu_ms=$cpu
                runner_sampled_peak_rss_bytes=($rss | Measure-Object -Maximum).Maximum
                runner_last_sample_rss_bytes=if($rss.Count){$rss[-1]}else{$null}
                rss_sample_count=$rss.Count;sample_interval_ms=100
                process_tree_sampled_cpu_ms=if($ObserveTree){($owned.Values | ForEach-Object { $_.max_observed_cpu_ms } | Measure-Object -Sum).Sum}else{$null}
                process_tree_sampled_peak_rss_bytes=if($ObserveTree){$treePeak}else{$null}
                observed_processes=if($ObserveTree){@($owned.Values)}else{$null};observed_survivors=$survivors
                scope='Instrumented Windows observations; sampled CPU/RSS lower bounds; short-lived descendants may be missed; no matched alternative or complete survivor guarantee'
            }
            [IO.File]::AppendAllText((Join-Path $out 'observations.jsonl'), (($row | ConvertTo-Json -Compress -Depth 5) + "`n"), $utf8)
            Write-Output "$id exit=$exit passed=$($row.passed) wall_ms=$([math]::Round($row.whole_command_ms))"
        } finally { $process.Dispose() }
    }
}
