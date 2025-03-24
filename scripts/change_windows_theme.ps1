$currentHour = (Get-Date).Hour

$themeValue = if ($currentHour -ge 6 -and $currentHour -lt 18) { "Material White Lighter High Contrast" } else { "Default Dark+" }

# Change Windows theme
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

if (!(Test-Path $regPath)) {
    New-Item -Path $regPath -Force | Out-Null
}

$windowsThemeValue = if ($currentHour -ge 6 -and $currentHour -lt 18) { 1 } else { 0 }

New-ItemProperty -Path $regPath -Name "AppsUseLightTheme" -Value $windowsThemeValue -PropertyType DWord -Force
New-ItemProperty -Path $regPath -Name "SystemUsesLightTheme" -Value $windowsThemeValue -PropertyType DWord -Force

# Change VS Code theme
$settingsPath = "$env:APPDATA\Code\User\settings.json"

if (Test-Path $settingsPath) {
    $settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
    $settingsHashtable = @{}
    foreach ($key in $settings.PSObject.Properties.Name) {
        $settingsHashtable[$key] = $settings.$key
    }
    $settingsHashtable["workbench.colorTheme"] = $themeValue
    $settingsHashtable | ConvertTo-Json -Depth 32 | Set-Content $settingsPath
} else {
    $settings = @{
        "workbench.colorTheme" = $themeValue
    }
    $settings | ConvertTo-Json -Depth 32 | Set-Content $settingsPath
}