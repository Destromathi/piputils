import os
import shutil

kansio = r"C:\tehtavat\testidata"

for tiedosto in os.listdir(kansio):
    tiedosto_polku = os.path.join(kansio, tiedosto)

    if os.path.isfile(tiedosto_polku):
        paate = os.path.splitext(tiedosto)[1].lower().strip(".")

        if not paate:
            continue

        kohdekansio = os.path.join(kansio, paate)
        os.makedirs(kohdekansio, exist_ok=True)

        shutil.move(tiedosto_polku, os.path.join(kohdekansio, tiedosto))
