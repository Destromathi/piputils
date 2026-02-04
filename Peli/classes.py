def choose_class():
    while True:
        print("Valitse hahmo:")
        print("1) Soturi")
        print("2) Varas")

        c = input("> ")

        if c == "1":
            return {"voima": 3, "ketteryys": 1, "taikuus": 0, "kestävyys": 3}
        elif c == "2":
            return {"voima": 1, "ketteryys": 3, "taikuus": 0, "kestävyys": 2}
        else:
            print("❌ Virheellinen valinta")
