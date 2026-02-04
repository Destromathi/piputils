import yhteinen
import varmuuskopio
import levytila

try:
    # Kaikki tässä sisentyy
    levytila.tarkista_levytila("C:/")
    varmuuskopio.varmuuskopioi("varmuuskopio", "varmuuskopio_backup")

except Exception as e:
    yhteinen.kirjoita_loki(f"Levytilan tarkistus tai varmuuskopiointi epäonnistui: {str(e)}", "levytilalogi.txt")
    yhteinen.kirjoita_loki("Virhe suorituksessa.", "Virheloki.txtpip --version")
