import PySimpleGUI as sg
import random
from random import randint
from Generadores import Generador_de_letras
import time
from threading import Thread

MAX_ROWS = MAX_COL = 15

def Fin_Tiempo(terminar):
    terminar[0] = True

def Timer(run,pausar,terminar,dificultad):
    if(dificultad=="Facil"):
        secs = 60*2*30
    elif(dificultad=="Normal"):
        secs=45*2*30
    elif (dificultad =="Dificil"):
        secs=30*2*30
    if run == "start":
        while (secs >= 0) & (terminar[0] == False):
            if (pausar == True):
                return(pausar)
            if secs >= 60:
                minutos = secs // 60
                secs_print=secs % 60
            window['Tiempo'].update("{}:{}".format(minutos,secs_print))
            time.sleep(1)
            secs -= 1

def Update_Tablero():
    Lista_Tableros=[
        {"0,0":"white","0,1":"white","0,2":"red","0,3":"white","0,4":"green","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"green","0,11":"white","0,12":"red","0,13":"white","0,14":"white",
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
             },
        {"0,0":"green","0,1":"white","0,2":"white","0,3":"white","0,4":"white","0,5":"red","0,6":"white","0,7":"white","0,8":"white","0,9":"red","0,10":"white","0,11":"white","0,12":"white","0,13":"white","0,14":"green",
         "1,0":"white","1,1":"green","1,2":"white","1,3":"white","1,4":"white","1,5":"white","1,6":"red","1,7":"white","1,8":"red","1,9":"white","1,10":"white","1,11":"white","1,12":"white","1,13":"green","1,14":"white",
         "2,0":"white","2,1":"white","2,2":"blue","2,3":"green","2,4":"white","2,5":"white","2,6":"white","2,7":"yellow","2,8":"white","2,9":"white","2,10":"white","2,11":"green","2,12":"blue","2,13":"white","2,14":"white",
         "3,0":"white","3,1":"white","3,2":"green","3,3":"blue","3,4":"white","3,5":"white","3,6":"white","3,7":"white","3,8":"white","3,9":"white","3,10":"white","3,11":"blue","3,12":"green","3,13":"white","3,14":"white",
         "4,0":"white","4,1":"white","4,2":"white","4,3":"white","4,4":"blue","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"blue","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"white",
         "5,0":"white","5,1":"white","5,2":"green","5,3":"white","5,4":"white","5,5":"yellow","5,6":"red","5,7":"white","5,8":"red","5,9":"yellow","5,10":"white","5,11":"white","5,12":"green","5,13":"white","5,14":"white",
         "6,0":"white","6,1":"red","6,2":"white","6,3":"white","6,4":"white","6,5":"red","6,6":"white","6,7":"white","6,8":"white","6,9":"red","6,10":"white","6,11":"white","6,12":"white","6,13":"red","6,14":"white",
         "7,0":"white","7,1":"white","7,2":"yellow","7,3":"white","7,4":"white","7,5":"white","7,6":"white","7,7":"black","7,8":"white","7,9":"white","7,10":"white","7,11":"white","7,12":"yellow","7,13":"white","7,14":"white",
         "8,0":"white","8,1":"red","8,2":"white","8,3":"white","8,4":"white","8,5":"red","8,6":"white","8,7":"white","8,8":"white","8,9":"red","8,10":"white","8,11":"white","8,12":"white","8,13":"red","8,14":"white",
         "9,0":"white","9,1":"white","9,2":"green","9,3":"white","9,4":"white","9,5":"yellow","9,6":"red","9,7":"white","9,8":"red","9,9":"yellow","9,10":"white","9,11":"white","9,12":"green","9,13":"white","9,14":"white",
         "10,0":"white","10,1":"white","10,2":"white","10,3":"white","10,4":"blue","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"blue","10,11":"white","10,12":"white","10,13":"white","10,14":"white",
         "11,0":"white","11,1":"white","11,2":"green","11,3":"blue","11,4":"white","11,5":"white","11,6":"white","11,7":"white","11,8":"white","11,9":"white","11,10":"white","11,11":"blue","11,12":"green","11,13":"white","11,14":"white",
         "12,0":"white","12,1":"white","12,2":"blue","12,3":"green","12,4":"white","12,5":"white","12,6":"white","12,7":"yellow","12,8":"white","12,9":"white","12,10":"white","12,11":"green","12,12":"blue","12,13":"white","12,14":"white",
         "13,0":"white","13,1":"green","13,2":"white","13,3":"white","13,4":"white","13,5":"white","13,6":"red","13,7":"white","13,8":"red","13,9":"white","13,10":"white","13,11":"white","13,12":"white","13,13":"green","13,14":"white",
         "14,0":"green","14,1":"white","14,2":"white","14,3":"white","14,4":"white","14,5":"red","14,6":"white","14,7":"white","14,8":"white","14,9":"red","14,10":"white","14,11":"white","14,12":"white","14,13":"white","14,14":"green",
             },
        {"0,0":"white","0,1":"white","0,2":"white","0,3":"white","0,4":"blue","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"red","0,11":"white","0,12":"white","0,13":"white","0,14":"white",
         "1,0":"green","1,1":"white","1,2":"white","1,3":"white","1,4":"white","1,5":"white","1,6":"white","1,7":"white","1,8":"cyan","1,9":"white","1,10":"white","1,11":"white","1,12":"white","1,13":"white","1,14":"green",
         "2,0":"white","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"white","2,7":"cyan","2,8":"white","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"white",
         "3,0":"brown","3,1":"white","3,2":"blue","3,3":"white","3,4":"white","3,5":"white","3,6":"white","3,7":"brown","3,8":"white","3,9":"white","3,10":"white","3,11":"white","3,12":"red","3,13":"white","3,14":"brown",
         "4,0":"white","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"white",
         "5,0":"white","5,1":"white","5,2":"white","5,3":"orange","5,4":"white","5,5":"white","5,6":"white","5,7":"white","5,8":"white","5,9":"white","5,10":"white","5,11":"orange","5,12":"white","5,13":"white","5,14":"white",
         "6,0":"blue","6,1":"white","6,2":"white","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"white","6,13":"white","6,14":"red",
         "7,0":"white","7,1":"white","7,2":"white","7,3":"SlateGray","7,4":"white","7,5":"white","7,6":"white","7,7":"black","7,8":"white","7,9":"white","7,10":"white","7,11":"SlateGray","7,12":"white","7,13":"white","7,14":"white",
         "8,0":"blue","8,1":"white","8,2":"white","8,3":"white","8,4":"white","8,5":"cyan","8,6":"white","8,7":"white","8,8":"white","8,9":"cyan","8,10":"white","8,11":"white","8,12":"white","8,13":"white","8,14":"red",
         "9,0":"white","9,1":"white","9,2":"white","9,3":"white","9,4":"white","9,5":"white","9,6":"white","9,7":"white","9,8":"white","9,9":"white","9,10":"white","9,11":"white","9,12":"white","9,13":"white","9,14":"white",
         "10,0":"white","10,1":"white","10,2":"white","10,3":"white","10,4":"orange","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"orange","10,11":"white","10,12":"white","10,13":"white","10,14":"white",
         "11,0":"brown","11,1":"white","11,2":"blue","11,3":"white","11,4":"white","11,5":"white","11,6":"white","11,7":"brown","11,8":"white","11,9":"white","11,10":"white","11,11":"white","11,12":"red","11,13":"white","11,14":"brown",
         "12,0":"white","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"white","12,7":"white","12,8":"cyan","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"white",
         "13,0":"green","13,1":"white","13,2":"white","13,3":"white","13,4":"white","13,5":"white","13,6":"white","13,7":"cyan","13,8":"white","13,9":"white","13,10":"white","13,11":"white","13,12":"white","13,13":"white","13,14":"green",
         "14,0":"white","14,1":"white","14,2":"white","14,3":"white","14,4":"blue","14,5":"white","14,6":"white","14,7":"white","14,8":"white","14,9":"white","14,10":"red","14,11":"white","14,12":"white","14,13":"white","14,14":"white",
             }
             ]
    tablero_random=(Lista_Tableros[randint(0,(len(Lista_Tableros)-1))])
    for x in range(15):
        for y in range(15):
            coord = (x,y)
            Pos_Dicc = str(x) + ',' + str(y)

            window[coord].update(button_color=('Black',str(tablero_random[Pos_Dicc])))
    return

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ''
    return Dicc

def Layout_Columna():

    layout = [ [sg.Text('Tiempo Disponible',font=("impact",20))],
               [sg.Text('30:00',pad=(70,3),font=("Bahnschrift",20),key=('Tiempo'))],
               [sg.Text('Puntos CPU',font=("impact",20))],
               [sg.Text('0',font=("impact",20))],
               [sg.Text('Puntos Usuario',font=("impact",20))],
               [sg.Text('0',font=("impact",20))],
               [sg.Button(button_text='Terminar turno',size=(15,0),font=("Unispace",20),pad=((5,0),(233,2)))],
               [sg.Button(button_text='Validar',size=(15,0),font=("Unispace",20),pad=((5,0),(5,3)))],
               [sg.Button(button_text='Intercambiar fichas',size=(15,0),font=("Unispace",20))],
               [sg.Button(button_text='Pa',key='Pausar',font=("default",19),pad=((5,43),(5,3)) ),
                sg.Button(button_text='Re',key='Rendirse',font=("default",19),pad=((5,42),(5,3)) ),
                sg.Button(button_text='Sa',key='Salir',font=("default",19))] ]

    return layout

def Layout_Tabla(Lista_Atril):
    MAX_ROWS = MAX_COL = 15
    formato_fichas_cpu={'filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','size':(40,40),'pad':(7,3)  }

    #formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','image_size':(40,40),'pad':(7,3)  }

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

    layout = [[sg.Text('',key='texto1',pad=(45,3)),(sg.Image(**formato_fichas_cpu,key='fichasbot1')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot2')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot3')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot4')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot5')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot6')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot7'))],
                [(sg.Image(filename=r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Atril_back.png',key='atril',pad=(20,3)))]]

    layout.extend([[sg.Button('', size=(4, 2),key=(i,j),pad=(0,0))for j in range(MAX_COL)] for i in range(MAX_ROWS)])

    layout.extend([[sg.Text('',key='texto2',pad=(28,3)),
                    (sg.Button(button_text=Letra_1,key=0,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_2,key=1,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_3,key=2,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_4,key=3,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_5,key=4,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_6,key=5,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_7,key=6,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357')))],
                    [(sg.Image(filename=r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Atril.png',key='texto'))]])

    return layout

def Llenar_Atril(Lista_Atril):
    #Falta una condicion de fin de turno para que se llenen las fichas
    for pos in range(len(Lista_Atril)):
        if (Lista_Atril[pos] == ''):
            Lista_Atril[pos] = Generador_de_letras()
            window[pos].update(Lista_Atril[pos])

def Coord_Ocupada(LCO,event):
    if (event in LCO):
        return True
    else:
        return False

def Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril):
    Dicc[event] = letra_1
    window[event].update(letra_1,button_color=('black','#FDD357'))
    Lista_Atril[pos_letra_1] = ''
    window[pos_letra_1].update('')
    return Dicc

def Coord_Adyacentes(coord):
    x,y=coord
    coord1=(x+1,y)
    coord2=(x,y+1)
    coord3=(x-1,y)
    coord4=(x,y-1)
    return coord1,coord2,coord3,coord4

def Coord_Disponible(LCO,CCD):
    for x in range(len(LCO)):
        for y in Coord_Adyacentes(LCO[x]):
            CCD.add(y)

def Coord_Desbloqueada(CCD,event):
    if (event in CCD):
        return True
    else:
        return False

def Acciones_Usuario(event,Dicc,Lista_Atril,LCO,CCD):
    if (type(event) == int) and (Lista_Atril[event] != ''):  #Si event es ENTERO #Event es la posicion de la letra pulsada
        letra_1 = Lista_Atril[event]
        pos_letra_1= event
        window[pos_letra_1].update(button_color=('white','#57C3FD'))
        event = window.read()[0]
        if (type(event) != int):                            #Si event es coordenada Y no esta ocupada:
            if (Coord_Ocupada(LCO,event) == False):         #event es en donde quiero poner la ficha
                if (Dicc[(7,7)] == ''):
                    if (event == (7,7)):
                        Dicc = Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril)
                        LCO.append(event)
                        Coord_Disponible(LCO,CCD)
                else:
                    if Coord_Desbloqueada(CCD,event):
                        Dicc = Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril)
                        LCO.append(event)
                        Coord_Disponible(LCO,CCD)
        else:
            letra_2 = Lista_Atril[event]
            pos_letra_2 = event
            if (pos_letra_1 != pos_letra_2):
                window[pos_letra_1].update(letra_2)
                window[pos_letra_2].update(letra_1)
                Lista_Atril[pos_letra_1] = letra_2
                Lista_Atril[pos_letra_2] = letra_1
        window[pos_letra_1].update(button_color=('black','#FDD357'))
    else:
        if (type(event) == tuple):
            if Coord_Ocupada(LCO,event): #Si la coordenada esta ocupada:
                if (event != (7,7)):
                    coord = event
                    window[coord].update(button_color=('white','#57C3FD'))
                    event = window.read()[0]
                    if (type(event) == int):
                        if (Lista_Atril[event] == ''): #FichaTablero x FichaAtrilVacia
                            Lista_Atril[event] = Dicc[coord]
                            window[coord].update('',button_color=('white','white')) #Temporal(Tengo que actualizar el dicc con los colores D:)
                            window[event].update(Dicc[coord])
                            Dicc[coord] = ''
                            LCO.remove(coord)
                        else: #FichaTablero x FichaAtril
                            window[coord].update(button_color=('black','#FDD357'))
                    else:
                        if Coord_Ocupada(LCO,event): #FichaTablero x FichaTablero:
                            aux = Dicc[event]
                            Dicc[event] = Dicc[coord]
                            Dicc[coord] = aux
                            window[event].update(Dicc[event])
                            window[coord].update(aux)
                            window[coord].update(button_color=('black','#FDD357'))
                        else:                        #FichaTablero x TableroVacio:
                            Dicc[event] = Dicc[coord]
                            Dicc[coord] = ''
                            window[coord].update('',button_color=('white','white')) #Temporal
                            window[event].update(Dicc[event],button_color=('black','#FDD357'))
                            LCO.remove(coord)
                            LCO.append(event)
            else:
                sg.popup('Primero selecciona una letra!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True)

def Turno(Turno_Usuario):
    if Turno_Usuario:
        sg.popup('Estas Listo?\nEmpiezas tu',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)
    else:
        sg.popup('Estas Listo?\nEmpieza la IA',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)

#PROGRAMA PRINCIPAL

sg.theme('DarkBlue')
Lista_Atril = []
Terminar = [False]
Dicc = Generar_Dicc()
diseño = [ [sg.Column((Layout_Tabla(Lista_Atril))),
            sg.Column(Layout_Columna())] ]
window = sg.Window('Tablero',diseño ,location=(400,0))
window.read(timeout=1)           #Es correcto esta solucion?(Hacer doble read?)
Update_Tablero()
Turno_Usuario = bool(random.getrandbits(1))
Turno(Turno_Usuario)
T=Thread(target=Timer,args=("start",False,Terminar,"Dificil"))
T.start()
Fin = False
CCD=set() #Conjunto de Coordenadas  Disponibles
LCO = []  #Lista de Coordenadas Ocupadas
while True:
    while (Turno_Usuario): #Mientras sea el turno del usuario:
        event = window.Read()[0]

        if event in (None, 'Salir'):
            Fin = True
            break

        Acciones_Usuario(event,Dicc,Lista_Atril,LCO,CCD)

        if (event == 'Terminar turno'):
            Llenar_Atril(Lista_Atril)
            break
    #while (Turno_Usuario == False):
        #ACTUA LA MAQUINA
    if Fin:
        Fin_Tiempo(Terminar)
        T.join()
        break
    Turno_Usuario = not Turno_Usuario
window.close()
