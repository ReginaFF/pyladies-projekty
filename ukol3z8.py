domaci_zvirata = ["pes", "kocka", "kralik", "had"]

def vyskyt_v_seznamu(zvire):
    """Zjisti, zda je zvire v seznamu"""
    if zvire in domaci_zvirata:
      vysledek = True
    else:
      vysledek = False

    return (vysledek)

zvire = input("Zadej zvire: ")
print ("Je zvire na seznamu domacich zvirat?", vyskyt_v_seznamu(zvire))
