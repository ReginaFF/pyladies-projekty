domaci_zvirata = ["pes", "kocka", "kralik", "had"]

def vypis_jmeno_na_k(seznam_zvire):
    """vypise zvirata zacinajici na pismeno k"""
    jmena_na_k = []
    for z in seznam_zvire:
        if z[0] == "k":
            jmena_na_k.append(z)
    return (jmena_na_k)

print ("Domaci zvirata se jmenem zacinajicim na k jsou:", vypis_jmeno_na_k(domaci_zvirata))
