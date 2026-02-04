import yhteinen
import shutil


def tarkista_levytila(path: str = "C:/"):
    total, used, free = shutil.disk_usage(path)
    yhteinen.kirjoita_loki(
        f"Kokotila: {total // (1024**3)} GiB, Kaytossa: {used // (1024**3)} GiB, Vapaana: {free // (1024**3)} GiB",
        "levytilalogi.txt",
    )
    if free < total * 0.1:
        yhteinen.kirjoita_loki("Varoitus: Levytila alle 10%!", "levytilalogi.txt")
    return total, used, free