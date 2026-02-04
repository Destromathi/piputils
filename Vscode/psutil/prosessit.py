import psutil
from yhteinen import kirjoita_loki

def tarkista_prosessit(loki_tiedosto="prosessit.log"):
    prosessien_maara = len(psutil.pids())
    kirjoita_loki(f"Aktiivisten prosessien määrä: {prosessien_maara}", loki_tiedosto)

if __name__ == "__main__":
    tarkista_prosessit()
