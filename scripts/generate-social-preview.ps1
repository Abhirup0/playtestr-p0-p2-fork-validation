$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$repoRoot = Split-Path -Parent $PSScriptRoot
$outputDir = Join-Path $repoRoot 'site\static\images'
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
$outputPath = Join-Path $outputDir 'social-preview.png'

$bitmap = [System.Drawing.Bitmap]::new(1200, 630)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$paper = [System.Drawing.ColorTranslator]::FromHtml('#ffffff')
$ink = [System.Drawing.ColorTranslator]::FromHtml('#142235')
$muted = [System.Drawing.ColorTranslator]::FromHtml('#526174')
$line = [System.Drawing.ColorTranslator]::FromHtml('#dce3eb')
$accent = [System.Drawing.ColorTranslator]::FromHtml('#244cc7')

try {
    $graphics.Clear($paper)
    $accentBrush = [System.Drawing.SolidBrush]::new($accent)
    $inkBrush = [System.Drawing.SolidBrush]::new($ink)
    $mutedBrush = [System.Drawing.SolidBrush]::new($muted)
    $linePen = [System.Drawing.Pen]::new($line, 2)
    $smallFont = [System.Drawing.Font]::new('Arial', 20, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    $titleFont = [System.Drawing.Font]::new('Arial', 64, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $taglineFont = [System.Drawing.Font]::new('Arial', 29, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)

    $graphics.FillRectangle($accentBrush, 0, 0, 12, 630)
    $graphics.DrawString('>_  playtestr', $taglineFont, $inkBrush, 76, 65)
    $graphics.DrawString('Test the terminal.', $titleFont, $inkBrush, 70, 188)
    $graphics.DrawString('See what changed.', $titleFont, $inkBrush, 70, 267)
    $graphics.DrawString('End-to-end testing for interactive CLIs and TUIs.', $taglineFont, $mutedBrush, 76, 398)
    $graphics.DrawLine($linePen, 76, 500, 1124, 500)
    $graphics.DrawString('Real terminal sessions. Reviewed snapshots. Clear failure evidence.', $smallFont, $mutedBrush, 76, 531)

    $bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
}
finally {
    foreach ($item in @($titleFont, $taglineFont, $smallFont, $accentBrush, $inkBrush, $mutedBrush, $linePen, $graphics, $bitmap)) {
        if ($null -ne $item) { $item.Dispose() }
    }
}

Write-Output $outputPath
