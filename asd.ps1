try {
	Copy-Item "C:\EiOle" "Backup" -ErrorAction Stop
} catch {
	Kirjoita-Loki "Virhe kopioinnissa"
}