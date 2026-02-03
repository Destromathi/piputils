from pathlib import Path
from datetime import datetime
 
kansiopaikka = Path("lokit")
 
def kirjoita_loki(viesti, tiedosto):
    kansiopaikka.mkdir(exist_ok=True)
    with open(kansiopaikka / tiedosto, "a", encoding="utf-8") as loki:
        loki.write(f"{datetime.now()}: {viesti}\n")
