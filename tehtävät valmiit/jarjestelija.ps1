# PowerShell - Tiedostojen lajittelija

Clear-Host

Write-Host "`nKAYNNISTETAAN SIIVOUSROBOTTIA..."
Write-Host "============================================"
Write-Host "`n"

# --- 1. Kansioiden luonti / tarkistus ---
$kansiot = @("Kuvat", "Videot", "Musiikki", "Dokumentit", "Data", "Asennukset")
$kansiot | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -Path $_ -ItemType Directory
        Write-Host "Kansio '$_' luotiin."
    } else {
        Write-Host "Kansio '$_' on jo olemassa."
    }
}

# --- 2-7. Siirrettävät tiedostot ---
$tiedostotyypit = @{
    "Kuvat"      = @("jpg", "jpeg", "png", "heic", "gif", "webp", "bmp")
    "Videot"     = @("mp4", "mov", "avi", "mkv")
    "Musiikki"   = @("mp3", "wav", "flac")
    "Dokumentit" = @("pdf", "docx", "doc", "pptx", "txt", "bat")
    "Data"       = @("xlsx", "csv")
    "Asennukset" = @("exe", "msi", "zip", "rar")
}

$tiedostotyypit.GetEnumerator() | ForEach-Object {
    $kategoria = $_.Key
    $laajennukset = $_.Value
    Write-Host "`nLajitellaan '$kategoria'..."
    $laajennukset | ForEach-Object {
        Get-ChildItem -Path . -Filter "*.$_" | ForEach-Object {
            Move-Item -Path $_.FullName -Destination "$kategoria\"
            Write-Host "Siirretty tiedosto '$($_.Name)' kansioon '$kategoria'."
        }
    }
}

Write-Host "`n============================================"
Write-Host "`nVALMIS! TYOPOYTA PUHDAS."
Write-Host "`n============================================"
