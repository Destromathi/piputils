param (
    [Parameter(Mandatory = $true)]
    [string]$LahdeKansio,               # Lähdekansio, jonka haluat backupata
    [string]$Raportti = "loki.txt"      # Lokitiedosto skriptin kansioon
)

# --- Lokifunktio ---
function Kirjoita-Loki {
    param (
        [string]$Viesti,
        [string]$Tiedosto = $Raportti
    )

    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $Viesti" |
        Out-File $Tiedosto -Append -Encoding Unicode
}

# --- Kohdekansio aina sama kuin skriptin kansio ---
$KohdeKansio = Join-Path $PSScriptRoot "Backup"

# Luodaan kohdekansio, jos sitä ei ole
if (-not (Test-Path $KohdeKansio)) {
    New-Item -ItemType Directory -Path $KohdeKansio | Out-Null
    Kirjoita-Loki "Luotu kohdekansio: $KohdeKansio"
}

# --- Backup-funktio ---
function Tee-Varmuuskopio {
    param (
        [string]$Source,
        [string]$Destination
    )

    Kirjoita-Loki "Aloitetaan backup kansiosta: $Source"

    if (-not (Test-Path $Source)) {
        Kirjoita-Loki "Virhe: Lähdekansiota ei löytynyt: $Source"
        Write-Host "Virhe: Lähdekansiota ei löytynyt"
        return
    }

    try {
        Copy-Item "$Source\*" $Destination -Recurse -Force -ErrorAction Stop
        Kirjoita-Loki "Varmuuskopiointi valmis: $Destination"
        Write-Host "Varmuuskopio valmis: $Destination"
    }
    catch {
        Kirjoita-Loki "Virhe varmuuskopioinnissa: $_"
        Write-Host "Virhe varmuuskopioinnissa"
    }
}

# --- Suoritetaan backup ---
Kirjoita-Loki "Skripti OK"
Tee-Varmuuskopio -Source $LahdeKansio -Destination $KohdeKansio
