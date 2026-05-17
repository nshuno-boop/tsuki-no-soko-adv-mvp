param(
    [string]$ShortcutName = "Tsuki no Soko",
    [string]$DesktopPath = [Environment]::GetFolderPath("Desktop")
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$launcher = Join-Path $repoRoot "Start_TsukiNoSoko_ADV_MVP.cmd"
$icon = Join-Path $repoRoot "TsukiNoSoko.ico"

if (-not (Test-Path $launcher)) {
    throw "Launcher not found: $launcher"
}

if (-not (Test-Path $icon)) {
    throw "Icon not found: $icon"
}

$shortcutPath = Join-Path $DesktopPath "$ShortcutName.lnk"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "$env:SystemRoot\System32\cmd.exe"
$shortcut.Arguments = "/c ""$launcher"""
$shortcut.WorkingDirectory = "$repoRoot"
$shortcut.IconLocation = "$icon,0"
$shortcut.Description = "Tsuki no Soko ADV launcher"
$shortcut.Save()

Write-Output "Created shortcut: $shortcutPath"
