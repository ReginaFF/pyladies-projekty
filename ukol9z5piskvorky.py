# Nacte 1-d piskvorky a vyhodnoti
def vyhodnot_piskvorky():
    herni_pole = input("Zadej herni pole: ")
    herni_pole = herni_pole.lower()
    if ("xxx" in herni_pole) == True:
        print ("Stav hry:", "x")
    elif ("ooo" in herni_pole) == True:
        print ("Stav hry:", "o")
    elif ("-" not in herni_pole) == True:
        print ("Stav hry:", "!")
    else:
        print ("Stav hry:", "-")


vyhodnot_piskvorky()
