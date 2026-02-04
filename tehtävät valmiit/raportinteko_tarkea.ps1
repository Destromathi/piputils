function Kirjoita-Loki {
	param (
		[string]$Viesti,
		[string]$Tiedosto = "loki.txt"
	)
	"$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - $Viesti" | Out-File $Tiedosto -Append
}

Kirjoita-Loki "Skripti Ok"
Kirjoita-Loki "Tarkistetaan kansio"

try {
	Copy-Item "C:\EiOle" "Backup" -ErrorAction Stop
}
catch {
	Kirjoita-Loki "Virhe kopioinnissa"
}
