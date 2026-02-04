@echo off
title Tiedostojen Lajittelija
color 0A

echo.
echo KAYNNISTETAAN SIIVOUSROBOTTIA...
echo ============================================
echo.

:: --- 1. LUODAAN KANSIOT (Lyhyilla nimilla) ---
echo Luodaan kansiot...
if not exist "Kuvat" mkdir "Kuvat"
if not exist "Videot" mkdir "Videot"
if not exist "Musiikki" mkdir "Musiikki"
if not exist "Dokumentit" mkdir "Dokumentit"
if not exist "Data" mkdir "Data"
if not exist "Asennukset" mkdir "Asennukset"

:: --- 2. KUVAT (Sis. iPhone HEIC) ---
echo [1/6] Lajitellaan kuvia...
move *.jpg Kuvat\ >nul 2>&1
move *.jpeg Kuvat\ >nul 2>&1
move *.png Kuvat\ >nul 2>&1
move *.heic Kuvat\ >nul 2>&1
move *.gif Kuvat\ >nul 2>&1
move *.webp Kuvat\ >nul 2>&1
move *.bmp Kuvat\ >nul 2>&1

:: --- 3. VIDEOIT ---
echo [2/6] Lajitellaan videoita...
move *.mp4 Videot\ >nul 2>&1
move *.mov Videot\ >nul 2>&1
move *.avi Videot\ >nul 2>&1
move *.mkv Videot\ >nul 2>&1

:: --- 4. MUSIIKKI ---
echo [3/6] Lajitellaan musiikkia...
move *.mp3 Musiikki\ >nul 2>&1
move *.wav Musiikki\ >nul 2>&1
move *.flac Musiikki\ >nul 2>&1

:: --- 5. DOKUMENTIT (Word, PDF, Powerpoint) ---
echo [4/6] Lajitellaan papereita...
move *.pdf Dokumentit\ >nul 2>&1
move *.docx Dokumentit\ >nul 2>&1
move *.doc Dokumentit\ >nul 2>&1
move *.pptx Dokumentit\ >nul 2>&1

:: --- 6. DATA (Excel, CSV) ---
echo [5/6] Lajitellaan taulukoitia...
move *.xlsx Data\ >nul 2>&1
move *.csv Data\ >nul 2>&1

:: --- 7. ASENNUKSET JA PAKETIT ---
echo [6/6] Lajitellaan asennustiedostoja...
move *.exe Asennukset\ >nul 2>&1
move *.msi Asennukset\ >nul 2>&1
move *.zip Asennukset\ >nul 2>&1
move *.rar Asennukset\ >nul 2>&1

echo.
echo ============================================
echo.
echo VALMIS! TYOPYOTA PUHDAS.
echo.
pause

