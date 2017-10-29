# Nacte jmeno a zjisti pohlavi
def zjisti_pohlavi():
    prijmeni = input("Zadej prijmeni: ")
    koncovka = prijmeni[-3:]
    if koncovka.lower() == "ova":
        print ("Podle prijmeni jsi zena")
    else:
        print ("Podle prijmeni pravdepodobne nejsi zena")


zjisti_pohlavi()
