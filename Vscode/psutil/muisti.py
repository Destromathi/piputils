import psutil
from yhteinen import kirjoita_loki, lue_asetukset

def tarkista_muisti(loki_tiedosto="muisti.log"):
    
    muisti = psutil.virtual_memory()
    asetukset = lue_asetukset()

    if muisti.percent >= asetukset["memory_error"]:
        kirjoita_loki(f"{muisti.percent}% Muistin käyttö - ERROR", loki_tiedosto)
    elif muisti.percent >= asetukset["memory_warning"]:
        kirjoita_loki(f"{muisti.percent}% Muistin käyttö - WARNING", loki_tiedosto)
    else:
        kirjoita_loki(f"{muisti.percent}% Muistin käyttö", loki_tiedosto)

if __name__ == "__main__":
    tarkista_muisti()
