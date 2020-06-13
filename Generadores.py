import string
import random
string.ascii_letters
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def Generador_de_letras():
    return random.choice(string.ascii_letters).upper()
