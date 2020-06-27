import string
import random
string.ascii_letters
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def Generador_de_letras():
    return random.choice(string.ascii_letters).upper()
def Selector_de_coordenadas_disponibles(conjunto):
    x=random.randint(0,(len(conjunto)-1))
    conjunto=list(conjunto)
    return(tuple(conjunto[x]))
