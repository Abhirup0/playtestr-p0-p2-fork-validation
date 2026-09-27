# Behavior-preserving synthetic UI changes; no upstream upgrade is claimed.
$ErrorActionPreference = 'Stop'
$utf8 = New-Object Text.UTF8Encoding($false)
$variants = @(
    @('.trial-private/corpus-tools/create-vite-runtime','.trial-private/corpus-tools/create-vite-ui-runtime','node_modules/create-vite/dist/index.js'),
    @('.trial-private/corpus-tools/create-vite-mutated-runtime','.trial-private/corpus-tools/create-vite-ui-mutated-runtime','node_modules/create-vite/dist/index.js'),
    @('.trial-private/r3c/windows/py-01-posting/venv/Lib/site-packages/posting','.trial-private/corpus-tools/posting-ui-changed/posting','app.py'),
    @('.trial-private/corpus-tools/posting-save-mutated/posting','.trial-private/corpus-tools/posting-ui-save-mutated/posting','app.py')
)
foreach ($variant in $variants) {
    $source = Join-Path $variant[0] $variant[2]
    $destination = Join-Path $variant[1] $variant[2]
    $text = [IO.File]::ReadAllText((Resolve-Path -LiteralPath $source).Path)
    if ($variant[2] -eq 'app.py') {
        if (-not $text.Contains('Request saved')) { throw 'Missing reviewed save title' }
        $changed = $text.Replace('Request saved','Request stored')
    } else {
        if (-not $text.Contains('Select a framework:') -or -not $text.Contains('Select a variant:')) { throw 'Missing reviewed wizard prompts' }
        $changed = $text.Replace('Select a framework:','Choose a framework:').Replace('Select a variant:','Choose a variant:')
    }
    if (Test-Path -LiteralPath $variant[1]) {
        if ([IO.File]::ReadAllText((Resolve-Path -LiteralPath $destination).Path) -ne $changed) { throw "Existing UI variant differs: $destination" }
    } else {
        New-Item -ItemType Directory -Force -Path (Split-Path $variant[1]) | Out-Null
        Copy-Item -LiteralPath $variant[0] -Destination $variant[1] -Recurse
        [IO.File]::WriteAllText((Resolve-Path -LiteralPath $destination).Path,$changed,$utf8)
    }
    Write-Output "Verified synthetic UI variant: $destination"
}
