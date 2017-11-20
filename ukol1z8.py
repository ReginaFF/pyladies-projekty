domaci_zvirata = ["pes", "kocka", "kralik", "had"]

def vypis_kratke_jmeno(seznam_zvire):
    """vypise zvirata kratsi nez 5 pismena"""
    kratke_jmeno = []
    for z in seznam_zvire:
        if len(z) < 5:
            kratke_jmeno.append(z)
    return (kratke_jmeno)

print ("Domaci zvirata se jmenem kratsim nez 5 pismen jsou:", vypis_kratke_jmeno(domaci_zvirata))


# kratke_jmeno = []
# for zvire in domaci_zvirata:
#     if len(zvire) < 5:
#         kratke_jmeno.append(zvire)
# print ("Domaci zvirata se jmenem kratsim nez 5 pismen jsou:", kratke_jmeno)
#
# print ("Domaci zvirata se jmenem kratsim nez 5 pismen jsou:", kratke_jmeno)
