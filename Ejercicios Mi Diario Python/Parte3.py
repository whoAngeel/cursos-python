''' Ejercicio 3
    Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
    las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
    últimas tiene que decir que riman un poco y si no, que no riman.
'''


def rimas(palabra1, palabra2):
    if palabra1[-3:].lower() == palabra2[-3:].lower():
        print("Las palabras riman")
    else:
        print("Las palabras no riman")



rimas("pirinola", "granola")