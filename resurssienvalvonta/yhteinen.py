from pathlib import Path
from datetime import datetime

LOKIKANSIO = Path("lokit")
LOKITIEDOSTO = "resurssivalvonta.log"

def kirjoita_loki(viesti):
    LOKIKANSIO.mkdir(exist_ok=True)
    with open(LOKIKANSIO / LOKITIEDOSTO, "a", encoding="utf-8") as loki:
        loki.write(f"{datetime.now()}: {viesti}\n")
