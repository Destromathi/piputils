import prosessit
import prosessori
import muisti
from yhteinen import kirjoita_loki

YHTEIS_LOKI = "resurssienvalvonta.log"

kirjoita_loki("=== Resurssien valvonta käynnistyi ===", YHTEIS_LOKI)

for toiminto in (prosessit.tarkista_prosessit,
                  prosessori.tarkista_suoritin,
                  muisti.tarkista_muisti):
    try:
        toiminto(loki_tiedosto=YHTEIS_LOKI)  # ohitetaan oletus ja käytetään yhteistä lokia
    except Exception as e:
        kirjoita_loki(f"[PAASKRIPTI] Virhe {toiminto.__name__}: {e}", YHTEIS_LOKI)

kirjoita_loki("=== Resurssien valvonta valmis ===\n", YHTEIS_LOKI)
