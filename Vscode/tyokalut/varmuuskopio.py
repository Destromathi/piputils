from pathlib import Path
import shutil
import yhteinen
 
def varmuuskopioi(lahde, kohde):
    lahto = Path(lahde)
    maali = Path(kohde)
 
    # Tarkista, että lähdekansio on olemassa
    if not lahto.exists():
        yhteinen.kirjoita_loki(f"Lahdekansio {lahde} ei ole olemassa.", "varmuuskopiologi.txt")
        return
 
    # Luo kohdekansio, jos sitä ei ole
    maali.mkdir(parents=True, exist_ok=True)
 
    # Iteroi lähdekansion tiedostot ja kopioi ne kohteeseen
    for tiedosto in lahto.iterdir():
        if tiedosto.is_file() and not tiedosto.name.startswith('.'):  # Vältä piilotiedostoja
            try:
                shutil.copy(tiedosto, maali / tiedosto.name)
                yhteinen.kirjoita_loki(f"Tiedosto {tiedosto.name} kopioitu kansiosta {lahde} kansioon {kohde}.", "varmuuskopiologi.txt")
            except Exception as e:
                yhteinen.kirjoita_loki(f"Virhe kopioitaessa tiedostoa {tiedosto.name}: {str(e)}", "varmuuskopiologi.txt")
 
    yhteinen.kirjoita_loki(f"Varmuuskopiointi {lahde} -> {kohde} valmis.", "varmuuskopiologi.txt")
 
# funktiokutsu, että scripti toimii -> varmuuskopioi("testidata","varmuuskopio_testidata")