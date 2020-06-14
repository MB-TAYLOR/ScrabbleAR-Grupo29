import PySimpleGUI as sg
from Generadores import Generador_de_letras

MAX_ROWS = MAX_COL = 15

def Update_Tablero():
    tablero1={"0,0":"white","0,1":"white","0,2":"red","0,3":"white","0,4":"green","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"green","0,11":"white","0,12":"red","0,13":"white","0,14":"white",
          "1,0":"white","1,1":"green","1,2":"white","1,3":"white","1,4":"white","1,5":"orange","1,6":"white","1,7":"blue","1,8":"white","1,9":"orange","1,10":"white","1,11":"white","1,12":"white","1,13":"green","1,14":"white",
          "2,0":"red","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"green","2,7":"white","2,8":"green","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"red",
          "3,0":"white","3,1":"white","3,2":"white","3,3":"blue","3,4":"white","3,5":"white","3,6":"white","3,7":"orange","3,8":"white","3,9":"white","3,10":"white","3,11":"blue","3,12":"white","3,13":"white","3,14":"white",
          "4,0":"green","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"green",
          "5,0":"white","5,1":"orange","5,2":"white","5,3":"white","5,4":"white","5,5":"blue","5,6":"white","5,7":"red","5,8":"white","5,9":"blue","5,10":"white","5,11":"white","5,12":"white","5,13":"orange","5,14":"white",
          "6,0":"white","6,1":"white","6,2":"green","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"green","6,13":"white","6,14":"white",
          "7,0":"white","7,1":"blue","7,2":"white","7,3":"orange","7,4":"white","7,5":"red","7,6":"white","7,7":"black","7,8":"white","7,9":"red","7,10":"white","7,11":"orange","7,12":"white","7,13":"blue","7,14":"white",
          "8,0":"white","8,1":"white","8,2":"green","8,3":"white","8,4":"white","8,5":"white","8,6":"white","8,7":"white","8,8":"white","8,9":"white","8,10":"white","8,11":"white","8,12":"green","8,13":"white","8,14":"white",
          "9,0":"white","9,1":"orange","9,2":"white","9,3":"white","9,4":"white","9,5":"blue","9,6":"white","9,7":"red","9,8":"white","9,9":"blue","9,10":"white","9,11":"white","9,12":"white","9,13":"orange","9,14":"white",
          "10,0":"green","10,1":"white","10,2":"white","10,3":"white","10,4":"white","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"white","10,11":"white","10,12":"white","10,13":"white","10,14":"green",
          "11,0":"white","11,1":"white","11,2":"white","11,3":"blue","11,4":"white","11,5":"white","11,6":"white","11,7":"orange","11,8":"white","11,9":"white","11,10":"white","11,11":"blue","11,12":"white","11,13":"white","11,14":"white",
          "12,0":"red","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"green","12,7":"white","12,8":"green","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"red",
          "13,0":"white","13,1":"green","13,2":"white","13,3":"white","13,4":"white","13,5":"orange","13,6":"white","13,7":"blue","13,8":"white","13,9":"orange","13,10":"white","13,11":"white","13,12":"white","13,13":"green","13,14":"white",
          "14,0":"white","14,1":"white","14,2":"red","14,3":"white","14,4":"green","14,5":"white","14,6":"white","14,7":"white","14,8":"white","14,9":"white","14,10":"green","14,11":"white","14,12":"red","14,13":"white","14,14":"white",
          }
    for x in range(15):
        for y in range(15):
            coord = (x,y)
            Pos_Dicc = str(x) + ',' + str(y)
            window[coord].update(button_color=('Black',str(tablero1[Pos_Dicc])))
    return

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ''
    return Dicc

def Layout(Lista_Atril):
    MAX_ROWS = MAX_COL = 15
    formato_fichas_cpu={'filename':r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Ficha.png','size':(40,40),'pad':(7,3)  }

    formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Ficha.png','image_size':(40,40),'pad':(7,3)  }

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
    [(sg.Image(filename=r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Atril_back.png',pad=(20,3)))],
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
     [(sg.Image(filename=r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Atril.png'))]]

    return layout


#PROGRAMA PRINCIPAL
#sg.theme('Black')
Lista_Atril = []
Dicc = Generar_Dicc()
window = sg.Window('Tablero', Layout(Lista_Atril),location=(530,0))
window.read(timeout=1)           #Es correcto esta solucion?(Hacer doble read?)
Update_Tablero()
while True:
    event = window.read()[0]     #Leo solamente el "event" porque las "values" estan vacias,no sirven.
    if event in (None, 'Exit'):  #Event puede ser una tupla con Coordenadas O una posicion de la letra seleccionada del atril
        break
    if (type(event) == str):     #Si event es una Letra:
        letra_1 = Lista_Atril[int(event)]
        event = window.read()[0]
        if (type(event) != str): #Si event no es una letra(Por descarte tiene que ser una coordenada):
            Dicc[event] = letra_1
            window[event].update(str(letra_1),button_color=('black','#FDD357'))
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
