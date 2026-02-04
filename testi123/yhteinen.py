from pathlib import Path  # Lisää tämä rivi tuomaan Path-luokka käyttöön    
from datetime import datetime
 
kansiopaikka = Path("lokit")
 
def kirjoita_loki(viesti, tiedosto):
    kansiopaikka.mkdir(exist_ok=True)
    with open(kansiopaikka / tiedosto, "a") as loki:
        loki.write(f"{datetime.now()}: {viesti}\n")