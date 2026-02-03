import psutil
from yhteinen import kirjoita_loki

def tarkista_muisti():
    kirjoita_loki("[MUISTI] Tarkistus aloitettu")

    try:
        muisti = psutil.virtual_memory()
        kirjoita_loki(
            f"[MUISTI] Käyttö: {muisti.percent} % "
            f"({muisti.used // (1024**2)} MB / {muisti.total // (1024**2)} MB)"
        )

    except Exception as e:
        kirjoita_loki(f"[MUISTI] Virhe tarkistuksessa: {e}")

    kirjoita_loki("[MUISTI] Tarkistus päättyi\n")
