import psutil
from yhteinen import kirjoita_loki

def tarkista_prosessit():
    prosessit = [
        "python.exe",
        "chrome.exe",
        "ei_olemassa.exe"
    ]

    loydetyt = []
    puuttuvat = []

    kirjoita_loki("[PROSESSIT] Tarkistus aloitettu")

    try:
        kaynnissa_olevat = {
            p.info["name"].lower()
            for p in psutil.process_iter(["name"])
            if p.info["name"]
        }
    except Exception as e:
        kirjoita_loki(f"[PROSESSIT] Virhe prosessilistan lukemisessa: {e}")
        kaynnissa_olevat = set()

    for prosessi in prosessit:
        try:
            if prosessi.lower() in kaynnissa_olevat:
                kirjoita_loki(f"[PROSESSIT] Käynnissä: {prosessi}")
                loydetyt.append(prosessi)
            else:
                kirjoita_loki(f"[PROSESSIT] Ei käynnissä: {prosessi}")
                puuttuvat.append(prosessi)

        except Exception as e:
            kirjoita_loki(
                f"[PROSESSIT] Virhe prosessin {prosessi} tarkistuksessa: {e}"
            )
            puuttuvat.append(prosessi)

    kirjoita_loki(
        f"[PROSESSIT] Yhteenveto – "
        f"Käynnissä ({len(loydetyt)}): {', '.join(loydetyt) or 'ei yhtään'}, "
        f"Ei käynnissä ({len(puuttuvat)}): {', '.join(puuttuvat) or 'ei yhtään'}"
    )

    kirjoita_loki("[PROSESSIT] Tarkistus päättyi\n")
