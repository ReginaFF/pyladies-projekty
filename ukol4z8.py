def porovnej_seznamy(seznam1, seznam2):
    """Porovna zvirata ve dvou seznamech"""
    spolecna_zvirata = []
    pouze_seznam1 = []
    for z in seznam1:
        print(z)
        if z in seznam2:
            spolecna_zvirata.append(z)
            seznam2.remove(z)
        else:
            pouze_seznam1.append(z)
    print ("Spolecna zvirata: ", spolecna_zvirata)
    print ("Zvirata pouze v seznamu 1:", pouze_seznam1)
    print ("Zvirata pouze v seznamu 2:", seznam2)

domaci_zvirata = ["pes", "kocka", "kralik", "had", "prase"]
zoo_zvirata = ["had", "papousek", "tygr", "kralik", "lev"]
porovnej_seznamy(domaci_zvirata, zoo_zvirata)
