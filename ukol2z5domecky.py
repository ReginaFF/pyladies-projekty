# nakresli domecek dane velikosti

def namaluj_domecek():
    """ Namaluje tri zvetsujici se domecky zadane velikosti"""
    from turtle import forward, shape, right, left, exitonclick
    from math import sqrt
    shape("turtle")
    stena = float(input("Napis delku steny nejmensiho domecku: "))

    for cislo in range(3):
        for cislo in range (4):
            forward(stena)
            left(90)
        left(45)
        forward(sqrt(2*stena**2))

        for cislo in range(2):
            left(90)
            forward(sqrt(2*stena**2)/2)
        left(90)
        forward(sqrt(2*stena**2))
        left(45)
        forward(stena)

        stena = stena * 2

    exitonclick()

namaluj_domecek()
