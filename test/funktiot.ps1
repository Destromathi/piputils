function Luo-kansio {
New-Item -ItemType Directory -Path Kansio -Force | Out-Null
}

function Siirra-tiedostot{
Get-ChildItem *.txt -ErrorAction SilentlyContinue | Move-Item -Destination Kansio -ErrorAction SilentlyContinue
}

Write-Host "1- Luo kansio"
Write-Host "2- Siirra txt-tiedostot"
$valinta = Read-Host "Valitse:"
Switch ($valinta){
"1" {Luo-kansio}
"2" {Siirra-tiedostot}
}
