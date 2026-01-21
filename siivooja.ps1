Clear-Host
Write-Host "KANSION SIIVOUS KÄYNNISSÄ"
Write-Host "====================================="

function Luo-Kansiot {
$kansiot = @("Kuvat","Videot","Musiikki","Dokumentit","Data")
foreach ($kansio in $kansiot) {
	New-Item -ItemType Directory -Path $kansio -Force | Out-Null
	}
}

function Luo-UusiKansio {
	$nimi = Read-Host "anna kansion nimi"
	New-Item -ItemType Directory -Path $nimi -Force | Out-Null
	Write-Host "Kansio $nimi on luotu"
	return $nimi
}

function Siirra-Kuvat {    
$tiedostot = Get-ChildItem *.jpg,*.jpeg,*.png,*.heic,*.gif,*.webp,*.bmp -ErrorAction SilentlyContinue

if  ($tiedostot.Count -eq 0){
	Write-Host "Ei tiedostoja siirrettavaksi" -ForegroundColor Yellow
	return
	}

$kuvakansio = Luo-UusiKansio
Write-Host "Siirretty kuvat"
$tiedostot | Move-Item -Destination $kuvakansio -ErrorAction SilentlyContinue

}

function Siirra-Videot {    
$tiedostot = Get-ChildItem *.mp4,*.mov,*.avi, *.mkv -ErrorAction SilentlyContinue

if  ($tiedostot.Count -eq 0){
	Write-Host "Ei videoita siirrettavaksi" -ForegroundColor Yellow
	return
	}

$videokansio = Luo-UusiKansio
Write-Host "Siirretty videot"
$tiedostot | Move-Item -Destination $videokansio -ErrorAction SilentlyContinue

}

function Siirra-Musiikki {
$musiikkikansio = Luo-UusiKansio
Write-Host "Siirretään musiikkia..."
Get-ChildItem *.mp3,*.wav, *.flac -ErrorAction SilentlyContinue |
	Move-Item -Destination $musiikkikansio -ErrorAction SilentlyContinue
	Write-Host "Siirretty musiikit"
}

function Siirra-Dokumentit {
$dokumenttikansio = Luo-UusiKansio
Write-Host "Siirretään dokumentteja..."
Get-ChildItem *.pdf,*.docx,*.doc,*.pptx,*.txt,*.bat -ErrorAction SilentlyContinue |
	Move-Item -Destination $dokumenttikansio -ErrorAction SilentlyContinue
	Write-Host "Siirretty dokumentit"
}


function Siirra-Data {
$datakansio = Luo-UusiKansio
Write-Host "Siirretään data..."
Get-ChildItem *.xls,*.xlsx,*.csv -ErrorAction SilentlyContinue |
	Move-Item -Destination $datakansio -ErrorAction SilentlyContinue
	Write-Host "Siirretty data"
}


Luo-Kansiot
do {
Write-Host "1 - Siirra Kuvat"
Write-Host "2 - Siirra Videot"
Write-Host "3 - Siirra Musiikki"
Write-Host "4 - Siirra Dokumentit"
Write-Host "5 - Siirra Data"
Write-Host "6 - Siirra Kaikki"
Write-Host "0 - Poistu"
$valinta = Read-Host "Valitse toiminto"

switch ($valinta){
	"1" {Siirra-Kuvat}
	"2" {Siirra-Videot}
	"3" {Siirra-Musiikki}
	"4" {Siirra-Dokumentit}
	"5" {Siirra-Data}
	"6" {Siirra-Kuvat
			Siirra-Videot
			Siirra-Musiikki
			Siirra-Dokumentit
			Siirra-Data
			}
	"0" {Write-Host "Ohjelma lopetetaan"}
	default {Write-Host "Virheellinen valinta"-ForegroundColor Red}
	}
} while ($valinta -ne "0")

Write-Host "====================================="
Write-Host "               \,.,\ Valmis!  /,.,/              "
Write-Host "====================================="
