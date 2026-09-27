# Synthetic experiment patches, never modifications of installed good targets.
$ErrorActionPreference = 'Stop'
$utf8 = New-Object Text.UTF8Encoding($false)
$cases = @(
    @{
        Source='.trial-private/corpus-tools/create-vite-runtime'
        Destination='.trial-private/corpus-tools/create-vite-code-mutated-runtime'
        File='node_modules/create-vite/dist/index.js'
        Before='cb74cb790239b5ec7c07e91ba04ed1ef41a4eb130eb12cdd040179e5ed55838a'
        After='23ca944a09883a99b5ea3006621a08c626eb8e85719896b5e3fbb0a6307db1f0'
        Old='D.name=m,T(`package.json`'
        New='D.name=m,D.type=`commonjs`,T(`package.json`'
    },
    @{
        Source='.trial-private/r3c/windows/py-01-posting/venv/Lib/site-packages/posting'
        Destination='.trial-private/corpus-tools/posting-save-mutated/posting'
        File='collection.py'
        Before='54130864af979db95c1d1af18133ca3a437fe2f7e60d3375630d9b878cab9bbb'
        After='2d5aa43f09bdd86b286cc9a23a3ecb00bd3750fbd57861bf8b723c445da45a41'
        Old='path.write_text(yaml_content, encoding="utf-8")'
        New='path.write_text(yaml_content.replace("http://127.0.0.1:28741/saved", "http://127.0.0.1:28741/stale"), encoding="utf-8")'
    },
    @{
        Source='.trial-private/r3c/windows/py-02-litecli/venv/Lib/site-packages/litecli'
        Destination='.trial-private/corpus-tools/litecli-state-mutated/litecli'
        File='sqlexecute.py'
        Before='649d63bda90ffa7844410cf267302f20c9fb1b204f036497b6e255c0b11826ce'
        After='f18d7cad34cea9cf90d285b38085b846503b8e872d952f4598eedbe4194c9fee'
        Old='cur.execute(sql)'
        New='cur.execute(sql.replace("''gamma'',''three''", "''gamma'',''wrong''"))'
    }
)
foreach ($case in $cases) {
    $sourceFile = Join-Path $case.Source $case.File
    if ((Get-FileHash -LiteralPath $sourceFile -Algorithm SHA256).Hash.ToLower() -ne $case.Before) { throw "Unpinned source: $sourceFile" }
    $destinationFile = Join-Path $case.Destination $case.File
    if (Test-Path -LiteralPath $case.Destination) {
        if ((Get-FileHash -LiteralPath $destinationFile -Algorithm SHA256).Hash.ToLower() -ne $case.After) { throw "Existing mutation differs: $destinationFile" }
        Write-Output "Verified existing synthetic patch: $destinationFile"
        continue
    }
    New-Item -ItemType Directory -Force -Path (Split-Path $case.Destination) | Out-Null
    Copy-Item -LiteralPath $case.Source -Destination $case.Destination -Recurse
    $path = (Resolve-Path -LiteralPath $destinationFile).Path
    $content = [IO.File]::ReadAllText($path)
    if (($content.Split([string[]]@($case.Old),[StringSplitOptions]::None)).Count -ne 2) { throw "Source anchor is not unique: $path" }
    [IO.File]::WriteAllText($path,$content.Replace($case.Old,$case.New),$utf8)
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLower() -ne $case.After) { throw "Unexpected patched identity: $path" }
    Write-Output "Prepared synthetic patch: $destinationFile"
}
