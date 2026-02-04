from prosessit import tarkista_prosessit
from prosessori import tarkista_prosessori
from muisti import tarkista_muisti
from yhteinen import kirjoita_loki

kirjoita_loki("=== Resurssivalvonta käynnistyi ===")

for toiminto in (
    tarkista_prosessit,
    tarkista_prosessori,
    tarkista_muisti
):
    try:
        toiminto()
    except Exception as e:
        kirjoita_loki(
            f"[PAASKRIPTI] Virhe toiminnossa {toiminto.__name__}: {e}"
        )

kirjoita_loki("=== Resurssivalvonta suoritettu ===\n")
kirjoita_loki("================================\n")