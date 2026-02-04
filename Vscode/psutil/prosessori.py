import psutil
from yhteinen import kirjoita_loki, lue_asetukset

def tarkista_suoritin(loki_tiedosto="cpu.log"):
    cpu = psutil.cpu_percent(interval=1)
    asetukset = lue_asetukset()

    if cpu >= asetukset["cpu_error"]:
        kirjoita_loki(f"{cpu}% CPU usage - ERROR", loki_tiedosto)
    elif cpu >= asetukset["cpu_warning"]:
        kirjoita_loki(f"{cpu}% CPU usage - WARNING", loki_tiedosto)
    else:
        kirjoita_loki(f"{cpu}% CPU käyttö", loki_tiedosto)

# Solo-ajossa käytetään oletus-lokia
if __name__ == "__main__":
    tarkista_suoritin()
