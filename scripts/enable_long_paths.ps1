# Enable Long Path support in Windows
$regPath = "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem"
$regName = "LongPathsEnabled"
$regValue = 1

try {
    Set-ItemProperty -Path $regPath -Name $regName -Value $regValue -Type DWord
    Write-Host "Long Path support has been enabled. Please restart your computer."
} catch {
    Write-Host "Failed to set LongPathsEnabled value: $_"
}
