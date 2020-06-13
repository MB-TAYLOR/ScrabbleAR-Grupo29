import PySimpleGUI as sg
from Generadores import Generador_de_letras

MAX_ROWS = MAX_COL = 15

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ''
    return Dicc

def Layout():
    layout =  [[sg.Button('', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
    return layout


#PROGRAMA PRINCIPAL
sg.theme('DarkPurple2')
Dicc = Generar_Dicc()
window = sg.Window('Tablero', Layout())
#event, values = window.read()  #Realizar un layout de "Loading" o lo que sea para que el usuario de click y updatear el tablero
#window.FindElement((7,7)).Update('',button_color=('black','black'))
while True:
    Letra = Generador_de_letras()                   #Del atril escogo una letra (Importo del programa de Marcos)
    print('Supongamos que escogi la letra:',Letra)  #Solo para visualizar
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    if (Dicc[event] == ''):
        Dicc[event] = Letra
        window[event].update(str(Letra),button_color=('black','white'))
print(Dicc)
window.close()
