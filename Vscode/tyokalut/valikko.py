import yhteinen
import varmuuskopio
import levytila
import tiedostojensiirto

def nayta_valikko():
    while True:
        print("Tervetuloa ylläpito - työkaluun!")
        print("1. Suorita ylläpito")
        print("2. Järjestä tiedostot kansioihin")
        print("3. Poistu")

        valinta = input("Valitse toiminto (1-3): ")

        if valinta == "1":
            levytila.tarkista_levytila("C:/")
            lahde = input("Anna varmuuskopioitava kansio: ")
            kohde = input("Anna varmuuskopiokansio: ")
            varmuuskopio.varmuuskopioi(lahde, kohde)
            print("Ylläpito suoritettu2.")
           
        elif valinta == "2":
            lahde = input("Anna lähdekansio (tyhjä=CurrentFolder): ")
            kohde = input("Anna kohdekansio (tyhjä=CurrentFolder): ")
            tiedostojensiirto.jarjesta_tiedostot(lahde, kohde)
            print("Järjestetään tiedostot kansioihin.")
        elif valinta == "3":
            print("Poistutaan ohjelmasta.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

# 🔹 Tämä varmistaa, että valikko käynnistyy, kun ajetaan valikko.py
if __name__ == "__main__":
    nayta_valikko()
