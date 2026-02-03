import psutil
from yhteinen import kirjoita_loki

prosessit = [
    "python.exe",
    "chrome.exe",
    "ei_olemassa.exe"
]

LOKITIEDOSTO = "prosessit.log"

loydetyt = []
puuttuvat = []

kirjoita_loki("=== Tarkistus aloitettu ===", LOKITIEDOSTO)

try:
    kaynnissa_olevat = {p.info["name"].lower() for p in psutil.process_iter(["name"]) if p.info["name"]}
except Exception as e:
    kirjoita_loki(f"Virhe prosessilistan lukemisessa: {e}", LOKITIEDOSTO)
    kaynnissa_olevat = set()

for prosessi in prosessit:
    try:
        if prosessi.lower() in kaynnissa_olevat:
            kirjoita_loki(f"Prosessi käynnissä: {prosessi}", LOKITIEDOSTO)
            loydetyt.append(prosessi)
        else:
            kirjoita_loki(f"Prosessia ei löydy: {prosessi}", LOKITIEDOSTO)
            puuttuvat.append(prosessi)

    except Exception as e:
        kirjoita_loki(
            f"Virhe prosessin {prosessi} tarkistuksessa: {e}",
            LOKITIEDOSTO
        )
        puuttuvat.append(prosessi)

kirjoita_loki("--- YHTEENVETO ---", LOKITIEDOSTO)
kirjoita_loki(
    f"Käynnissä ({len(loydetyt)}): {', '.join(loydetyt) if loydetyt else 'ei yhtään'}",
    LOKITIEDOSTO
)
kirjoita_loki(
    f"Ei käynnissä ({len(puuttuvat)}): {', '.join(puuttuvat) if puuttuvat else 'ei yhtään'}",
    LOKITIEDOSTO
)
kirjoita_loki("=== Tarkistus päättyi ===\n", LOKITIEDOSTO)
