import PySimpleGUI as sg
from Generadores import Generador_de_letras

MAX_ROWS = MAX_COL = 15

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ''
    return Dicc

def Layout(Lista_Atril):
    MAX_ROWS = MAX_COL = 15
    formato_fichas_cpu={'filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','size':(40,40),'pad':(7,3)  }

    formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','image_size':(40,40),'pad':(7,3)  }

    Letra_1=Generador_de_letras()
    Lista_Atril.append(Letra_1)
    Letra_2=Generador_de_letras()
    Lista_Atril.append(Letra_2)
    Letra_3=Generador_de_letras()
    Lista_Atril.append(Letra_3)
    Letra_4=Generador_de_letras()
    Lista_Atril.append(Letra_4)
    Letra_5=Generador_de_letras()
    Lista_Atril.append(Letra_5)
    Letra_6=Generador_de_letras()
    Lista_Atril.append(Letra_6)
    Letra_7=Generador_de_letras()
    Lista_Atril.append(Letra_7)

    layout =  [[sg.Text('',pad=(45,3)),(sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu)),
                                       (sg.Image(**formato_fichas_cpu))],
    [(sg.Image(filename=r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Atril_back.png',pad=(20,3)))],
    [sg.Button('', size=(4, 2),key=(0,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(1,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(2,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(3,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(4,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(5,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(6,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(7,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(8,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(9,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(10,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(11,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(12,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(13,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Button('', size=(4, 2),key=(14,i),pad=(0,0))for i in range(MAX_ROWS)],
    [sg.Text('',pad=(35,3)),(sg.Button(button_text=Letra_1,key='0',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_2,key='1',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_3,key='2',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_4,key='3',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_5,key='4',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_6,key='5',**formato_fichas_jugador)),
                            (sg.Button(button_text=Letra_7,key='6',**formato_fichas_jugador)) ],
     [(sg.Image(filename=r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Atril.png'))]]

    return layout


#PROGRAMA PRINCIPAL
#sg.theme('Black')
Lista_Atril = []
Dicc = Generar_Dicc()
window = sg.Window('Tablero', Layout(Lista_Atril),location=(530,0))
while True:
    event = window.read()[0]     #Leo solamente el "event" porque las "values" estan vacias,no sirven.
    if event in (None, 'Exit'):  #Event puede ser una tupla con Coordenadas O una posicion de la letra seleccionada del atril
        break
    if (type(event) == str):     #Si event es una Letra:
        letra_1 = Lista_Atril[int(event)]
        event = window.read()[0]
        if (type(event) != str): #Si event no es una letra(Por descarte tiene que ser una coordenada):
            Dicc[event] = letra_1
            window[event].update(str(letra_1),button_color=('black','white'))
        else:
            Pos_letra_1 = Lista_Atril.index(letra_1)
            letra_2 = Lista_Atril[int(event)]
            Pos_letra_2 = int(event)
            if (Pos_letra_1 != Pos_letra_2):
                window[str(Pos_letra_1)].update(letra_2)
                window[str(Pos_letra_2)].update(letra_1)
                Lista_Atril[Pos_letra_1] = letra_2
                Lista_Atril[Pos_letra_2] = letra_1
    else:
         sg.popup('Hint: Primero selecciona una letra!',no_titlebar=True,background_color='Black',button_color=('Black','White'))
print(Lista_Atril)
window.close()
