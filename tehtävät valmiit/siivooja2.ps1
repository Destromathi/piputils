Clear-Host
 
Write-Host "KANSION SIIVOUS KAYNNISSA" -ForegoundColor Green
 
$kansiot=@("Kuvat2", "Videot2", "Musiikki2", "Asiakirjat2", "Data2")
 
foreach ($kansio in $kansiot){
New-Item -ItemType Directory $kansio -Force | Out-Null
}
 
Write-Host "Siirretaan kuvia2..."
Get-ChildItem *.jpg, *.png, *.jpeg, *.gif, *.bmp | Move-Item Kuvat2 -ErrorAction SilentlyContinue
Write-Host "Siirretaan videot2..."
Get-ChildItem *.mp4 *.mov | Move-Item Videot2 -ErrorAction SilentlyContinue
 
Write-Host "Siirretaan musiikki2..."
Get-ChildItem *.mp3, *.wav, *.ogg | Move-Item Musiikki2 -ErrorAction SilentlyContinue
 
Write-Host "Siirretaan asiakirjat2..."
Get-ChildItem *.pdf, *.txt, *.doc, *.docx | Move-Item Asiakirjat2 -ErrorAction SilentlyContinue
 
Write-Host "Siirretaan taulukoita..."
Get-ChildItem *.xls, *.xlsx | Move-Item Data2 -ErrorAction SilentlyContinue
 
Write-Host "=====================================" -ForegroundColor Green
Write-Host "		Valmis!	" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
