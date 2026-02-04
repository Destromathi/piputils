import psutil
from yhteinen import kirjoita_loki

def tarkista_prosessori():
    kirjoita_loki("[CPU] Tarkistus aloitettu")

    try:
        cpu = psutil.cpu_percent(interval=1)
        kirjoita_loki(f"[CPU] Käyttö: {cpu} %")

    except Exception as e:
        kirjoita_loki(f"[CPU] Virhe tarkistuksessa: {e}")

    kirjoita_loki("[CPU] Tarkistus valmis\n")