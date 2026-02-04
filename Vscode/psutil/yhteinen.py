from pathlib import Path
from datetime import datetime
import json

LOKIKANSIO = Path("lokit")

def kirjoita_loki(viesti, tiedosto):
    """Kirjoittaa viestin lokitiedostoon lokit-kansioon"""
    LOKIKANSIO.mkdir(exist_ok=True)
    polku = LOKIKANSIO / tiedosto
    with open(polku, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: {viesti}\n")

def lue_asetukset():
    """Lataa asetukset config.json tiedostosta"""
    with open("config.json", "r", encoding="utf-8") as tiedosto:
        return json.load(tiedosto)
