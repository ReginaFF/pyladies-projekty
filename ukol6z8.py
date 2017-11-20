domaci_zvirata = ["zirafa", "pes", "andulka", "kocka", "kralik", "had"]

def serad_seznam_druhe_pismeno(seznam):
    """Seradi seznam dle abecedy druheho pismene"""
    seznam_dvojic = []
    for zvire in seznam:
        zvire_bez_pp = zvire[1:]
        seznam_dvojic.append((zvire_bez_pp, zvire))
    seznam_dvojic.sort()
    serazeni_virat = []

    for zvire_bez_pp, zvire in seznam_dvojic:
        serazeni_virat.append(zvire)

    return (serazeni_virat)

print(serad_seznam_druhe_pismeno(domaci_zvirata))
