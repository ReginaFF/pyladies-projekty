 # zjisti pocet znaku k v textu pisne
def zjisti_pocet_znaku():
    pisen = """Je statisticky dokázáno,
že slunce vyjde každé ráno,
a i když je tma jako v ranci,
noc nemá celkem žádnou šanci.


Statistika nuda je má však cenné údaje,
neklesejme na mysli, ona nám to vyčíslí.
Statistika nuda je má však cenné údaje,
neklesejme na mysli, ona nám to vyčíslí.

Když drak si z nosu síru pouští
a Honza na něj číhá v houští,
pak statistika předpovídá,
že nestvůra už neposnídá.


Statistika nuda je má však cenné údaje,
neklesejme na mysli, ona nám to vyčíslí.
Statistika nuda je má však cenné údaje,
neklesejme na mysli, ona nám to vyčíslí.


Tak vyřiďte to ctěné sani,
že záleží to čistě na ní,
když nepustí ji choutky dračí,
tak bude o hlavičky kratší.


Statistika nuda je má však cenné údaje,mneklesejte na mysli, ona nám to vyčíslí.
Statistika nuda je má však cenné údaje,
neklesejme na mysli, ona nám to vyčíslí."""

    pisen = pisen.lower()
    pocet = pisen.count("k")
    print ("V pisni je", pocet, "znaku k")

zjisti_pocet_znaku()
