from pathlib import Path
import shutil  
import yhteinen

def jarjesta_tiedostot(lahde, kohde):
    lahto = Path(lahde)
    maali = Path(kohde)

    if not lahto.exists():
        yhteinen.kirjoita_loki(f"Lahdekansio {lahde} ei ole olemassa.", "jarjestamislogi.txt")
        return

    maali.mkdir(parents=True, exist_ok=True)

    siirretty = 0
    for tiedosto in lahto.iterdir():
        if tiedosto.is_file() and not tiedosto.name.startswith('.'):
            tiedostopääte = tiedosto.suffix[1:] if tiedosto.suffix else "muut"
            kohdekansio = maali / tiedostopääte
            kohdekansio.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(tiedosto, kohdekansio / tiedosto.name)
                yhteinen.kirjoita_loki(f"Tiedosto {tiedosto.name} siirretty kansioon {kohdekansio}.", "jarjestamislogi.txt")
                print(f"Tiedosto {tiedosto.name} siirretty kansioon {kohdekansio}.")
                siirretty += 1
            except Exception as e:
                yhteinen.kirjoita_loki(f"Virhe siirrettäessä tiedostoa {tiedosto.name}: {str(e)}", "jarjestamislogi.txt")
                print(f"Virhe siirrettäessä tiedostoa {tiedosto.name}: {str(e)}")

    if siirretty == 0:
        print("Ei siirrettäviä tiedostoja.")
    else:
        print(f"Siirrettiin {siirretty} tiedostoa.")
    yhteinen.kirjoita_loki(f"Tiedostojen järjestäminen kansiosta {lahde} kansioon {kohde} valmis.", "jarjestamislogi.txt")