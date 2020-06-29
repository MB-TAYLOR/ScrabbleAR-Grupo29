from palabra_Existe import verificar_Palabra
from Generadores import Selector_de_coordenadas_disponibles
from AiMaquina import formar_palabra
from threading import Thread
import PySimpleGUI as sg
from random import randint
import random
import time
import csv

MAX_ROWS = MAX_COL = 15


Bolsa_Diccionario={"A":11,"B":3,"C":4,"D":4,"E":11,"F":2,"G":2,"H":2,"I":6,"J":2,"K":1,"L":4,"LL":1,"M":3,"N":5,
                  "Ñ":1,"O":8,"P":2,"Q":1,"R":4,"RR":1,"S":7,"T":4,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1}
Cant_fichas=101

def Letra_Bolsa(Bolsa_Diccionario):
    global Cant_fichas
    sigue=True
    letra=""
    while((sigue)and(Cant_fichas >= 14)):
        x=random.randint(0,(len(Bolsa_Diccionario.keys())-1))
        letra=list(Bolsa_Diccionario.keys())[x]
        if(Bolsa_Diccionario[letra]> 0):
            Bolsa_Diccionario[letra]=(Bolsa_Diccionario[letra])-1
            Cant_fichas=Cant_fichas-1
            sigue=False
            break
    if Cant_fichas < 14 :
        print("El juego ACABA porque uno de los 2 jugadores no tiene sus 7 fichas")
    return(letra)

def Fin_Tiempo(terminar):
    terminar[0] = True

def Update_Tablero(window,Dicc):
    Lista_Tableros=[
        {"0,0":"white","0,1":"white","0,2":"red","0,3":"white","0,4":"green","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"green","0,11":"white","0,12":"red","0,13":"white","0,14":"white",
         "1,0":"white","1,1":"green","1,2":"white","1,3":"white","1,4":"white","1,5":"yellow","1,6":"white","1,7":"blue","1,8":"white","1,9":"yellow","1,10":"white","1,11":"white","1,12":"white","1,13":"green","1,14":"white",
         "2,0":"red","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"green","2,7":"white","2,8":"green","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"red",
         "3,0":"white","3,1":"white","3,2":"white","3,3":"blue","3,4":"white","3,5":"white","3,6":"white","3,7":"yellow","3,8":"white","3,9":"white","3,10":"white","3,11":"blue","3,12":"white","3,13":"white","3,14":"white",
         "4,0":"green","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"green",
         "5,0":"white","5,1":"yellow","5,2":"white","5,3":"white","5,4":"white","5,5":"blue","5,6":"white","5,7":"red","5,8":"white","5,9":"blue","5,10":"white","5,11":"white","5,12":"white","5,13":"yellow","5,14":"white",
         "6,0":"white","6,1":"white","6,2":"green","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"green","6,13":"white","6,14":"white",
         "7,0":"white","7,1":"blue","7,2":"white","7,3":"yellow","7,4":"white","7,5":"red","7,6":"white","7,7":"black","7,8":"white","7,9":"red","7,10":"white","7,11":"yellow","7,12":"white","7,13":"blue","7,14":"white",
         "8,0":"white","8,1":"white","8,2":"green","8,3":"white","8,4":"white","8,5":"white","8,6":"white","8,7":"white","8,8":"white","8,9":"white","8,10":"white","8,11":"white","8,12":"green","8,13":"white","8,14":"white",
         "9,0":"white","9,1":"yellow","9,2":"white","9,3":"white","9,4":"white","9,5":"blue","9,6":"white","9,7":"red","9,8":"white","9,9":"blue","9,10":"white","9,11":"white","9,12":"white","9,13":"yellow","9,14":"white",
         "10,0":"green","10,1":"white","10,2":"white","10,3":"white","10,4":"white","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"white","10,11":"white","10,12":"white","10,13":"white","10,14":"green",
         "11,0":"white","11,1":"white","11,2":"white","11,3":"blue","11,4":"white","11,5":"white","11,6":"white","11,7":"yellow","11,8":"white","11,9":"white","11,10":"white","11,11":"blue","11,12":"white","11,13":"white","11,14":"white",
         "12,0":"red","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"green","12,7":"white","12,8":"green","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"red",
         "13,0":"white","13,1":"green","13,2":"white","13,3":"white","13,4":"white","13,5":"yellow","13,6":"white","13,7":"blue","13,8":"white","13,9":"yellow","13,10":"white","13,11":"white","13,12":"white","13,13":"green","13,14":"white",
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
         "1,0":"green","1,1":"white","1,2":"white","1,3":"white","1,4":"white","1,5":"white","1,6":"white","1,7":"blue","1,8":"white","1,9":"white","1,10":"white","1,11":"white","1,12":"white","1,13":"white","1,14":"green",
         "2,0":"white","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"blue","2,7":"white","2,8":"white","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"white",
         "3,0":"red","3,1":"white","3,2":"blue","3,3":"white","3,4":"white","3,5":"white","3,6":"red","3,7":"white","3,8":"white","3,9":"white","3,10":"white","3,11":"white","3,12":"red","3,13":"white","3,14":"red",
         "4,0":"white","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"white",
         "5,0":"white","5,1":"white","5,2":"white","5,3":"yellow","5,4":"white","5,5":"white","5,6":"white","5,7":"white","5,8":"white","5,9":"white","5,10":"white","5,11":"yellow","5,12":"white","5,13":"white","5,14":"white",
         "6,0":"blue","6,1":"white","6,2":"white","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"white","6,13":"white","6,14":"red",
         "7,0":"white","7,1":"white","7,2":"white","7,3":"green","7,4":"white","7,5":"white","7,6":"white","7,7":"black","7,8":"white","7,9":"white","7,10":"white","7,11":"green","7,12":"white","7,13":"white","7,14":"white",
         "8,0":"blue","8,1":"white","8,2":"white","8,3":"white","8,4":"white","8,5":"blue","8,6":"white","8,7":"white","8,8":"white","8,9":"blue","8,10":"white","8,11":"white","8,12":"white","8,13":"white","8,14":"red",
         "9,0":"white","9,1":"white","9,2":"white","9,3":"white","9,4":"white","9,5":"white","9,6":"white","9,7":"white","9,8":"white","9,9":"white","9,10":"white","9,11":"white","9,12":"white","9,13":"white","9,14":"white",
         "10,0":"white","10,1":"white","10,2":"white","10,3":"white","10,4":"yellow","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"yellow","10,11":"white","10,12":"white","10,13":"white","10,14":"white",
         "11,0":"red","11,1":"white","11,2":"blue","11,3":"white","11,4":"white","11,5":"white","11,6":"white","11,7":"white","11,8":"red","11,9":"white","11,10":"white","11,11":"white","11,12":"red","11,13":"white","11,14":"red",
         "12,0":"white","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"white","12,7":"white","12,8":"blue","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"white",
         "13,0":"green","13,1":"white","13,2":"white","13,3":"white","13,4":"white","13,5":"white","13,6":"white","13,7":"blue","13,8":"white","13,9":"white","13,10":"white","13,11":"white","13,12":"white","13,13":"white","13,14":"green",
         "14,0":"white","14,1":"white","14,2":"white","14,3":"white","14,4":"blue","14,5":"white","14,6":"white","14,7":"white","14,8":"white","14,9":"white","14,10":"red","14,11":"white","14,12":"white","14,13":"white","14,14":"white",
             }
             ]

    num = randint(0,(len(Lista_Tableros)-1))
    tablero_random=(Lista_Tableros[num])
    for x in range(15):
        for y in range(15):
            coord = (x,y)
            Pos_Dicc = str(x) + ',' + str(y)
            Dicc[coord][1] = tablero_random[Pos_Dicc]
            window[coord].update(button_color=('Black',str(tablero_random[Pos_Dicc])))
    return Dicc

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ['','White']
    return Dicc

def Layout_Columna():

    layout = [ [sg.Text('Tiempo Disponible',font=("impact",20))],
               [sg.Text('00:60  |   30:00',pad=(20,3),font=("Bahnschrift",20),key=('Tiempo'))],
               [sg.Text('__________________________________')],
               [sg.Text('Puntos CPU',key='PuntosCPU',font=("impact",20))],
               [sg.Text('0000',key='PuntajeCPU',font=("impact",20))],
               [sg.Text('__________________________________')],
               [sg.Text('Puntos Usuario',key='PuntosUsuario',font=("impact",20))],
               [sg.Text('0000',key='PuntajeUsuario',font=("impact",20))],
               [sg.Text('__________________________________')],
               [sg.Button(button_text='Terminar turno',size=(15,0),font=("Unispace",20),pad=((5,0),(158,2)))],
               [sg.Button(button_text='Validar',size=(15,0),font=("Unispace",20),pad=((5,0),(5,3)))],
               [sg.Button(button_text='Intercambiar fichas',size=(15,0),font=("Unispace",20))],
               [sg.Button(button_text='Pausar',key='Pausar',font=("default",16),pad=((5,0),(3,0)) ), #font=("default",19),pad=((5,43),(5,3))
                sg.Button(button_text='Rendirse',key='Rendirse',font=("default",16),pad=((5,0),(2,0)) ),#font=("default",19),pad=((5,43),(5,3))
                sg.Button(button_text='Salir',key='Salir',font=("default",16))] ]#font=("default",19)

    return layout

def Layout_Tabla(Lista_Atril):
    MAX_ROWS = MAX_COL = 15
    formato_fichas_cpu={'filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','size':(40,40),'pad':(7,3)  }

    #formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':r'd:\Users\usuario\Documents\GitHub\ScrabbleAR-Grupo29\Ficha.png','image_size':(40,40),'pad':(7,3)  }
    #Para luego reemplazar los colores dados por el boton con imagenes
    Letra_1=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_1)
    Letra_2=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_2)
    Letra_3=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_3)
    Letra_4=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_4)
    Letra_5=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_5)
    Letra_6=Letra_Bolsa(Bolsa_Diccionario)
    Lista_Atril.append(Letra_6)
    Letra_7=Letra_Bolsa(Bolsa_Diccionario)
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

def Llenar_Atril(Lista_Atril,window):
    for pos in range(len(Lista_Atril)):
        if (Lista_Atril[pos] == ''):
            Lista_Atril[pos] = Letra_Bolsa(Bolsa_Diccionario)
            window[pos].update(Lista_Atril[pos])

def Coord_Ocupada(LCO,event):
    if (event in LCO):
        return True
    else:
        return False

def Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril,window):
    Dicc[event][0] = letra_1
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
            if(((y[0]< 15)and(y[1]< 15))and((y[0]>-1)and(y[1]>-1))):
                CCD.add(y)

def Coord_Desbloqueada(CCD,event):
    if (event in CCD):
        return True
    else:
        return False

def Eliminar_Coords(CCD,coord):
    '''Elimina Coordenadas.'''
    CCD.discard(((coord[0]-1),coord[1]))     #Arriba
    CCD.discard((coord[0],(coord[1]+1)))     #Derecha
    CCD.discard(((coord[0]+1),coord[1]))     #Abajo
    CCD.discard((coord[0],(coord[1]-1)))     #Izquierda

def FichaVaciaxFichaTablero(event,coord,Dicc,Lista_Atril,window,LCO,LCOPR,CCD):
    Lista_Atril[event] = Dicc[coord][0]
    window[coord].update('',button_color=('white',Dicc[coord][1]))
    window[event].update(Dicc[coord][0])
    Dicc[coord][0] = ''
    LCO.remove(coord)
    LCOPR.remove(coord)
    Eliminar_Coords(CCD,coord)

def Reemplazar_FichaxTablero(event,coord,Dicc,Lista_Atril,window):
    aux = Dicc[coord][0]
    Dicc[coord][0] = Lista_Atril[event]
    Lista_Atril[event] = aux
    window[coord].update(Dicc[coord][0])
    window[event].update(Lista_Atril[event])

def Update_Fichas_Colocadas(LCOPR,window):
    for coord in LCOPR:
        window[coord].update(button_color=('black','#E4BE4D'))

def Acciones_Usuario(event,Dicc,Lista_Atril,LCO,LCOPR,CCD,window):
    if (type(event) == int) and (Lista_Atril[event] != ''):  #Si event es ENTERO(Por ende la posicion de la letra del atril):
        letra_1 = Lista_Atril[event]
        pos_letra_1= event
        window[pos_letra_1].update(button_color=('white','#57C3FD'))
        event = window.read()[0]
        if (type(event) != int):                             #Si event es coordenada Y no esta ocupada:
            if (Coord_Ocupada(LCOPR,event) == False):        #FichaAtril x TableroVacio
                if (Dicc[(7,7)][0] == ''):                   #Si la cordenada de inicio esta vacia (Es el primer turno):
                    if (event == (7,7)):
                        Dicc = Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril,window)
                        LCO.append(event)
                        LCOPR.append(event)
                        Coord_Disponible(LCO,CCD)
                else:
                    if (Coord_Ocupada(LCO,event) != True) and Coord_Desbloqueada(CCD,event):
                        Dicc = Colocar_Ficha(Dicc,letra_1,pos_letra_1,event,Lista_Atril,window)
                        LCO.append(event)
                        LCOPR.append(event)
                        Coord_Disponible(LCO,CCD)
            else:                               #FichaAtril x FichaTablero
                Reemplazar_FichaxTablero(pos_letra_1,event,Dicc,Lista_Atril,window)
        else:              #FichaAtril X FichaAtril (Intercambio)
            letra_2 = Lista_Atril[event]
            pos_letra_2 = event
            if (pos_letra_1 != pos_letra_2):
                window[pos_letra_1].update(letra_2)
                window[pos_letra_2].update(letra_1)
                Lista_Atril[pos_letra_1] = letra_2
                Lista_Atril[pos_letra_2] = letra_1
        window[pos_letra_1].update(button_color=('black','#FDD357'))
    else:                                #Si event NO es entero:
        if (type(event) == tuple):       #Comprobamos que sea una tupla(coordenada del tablero)
            if Coord_Ocupada(LCOPR,event): #Si la coordenada esta ocupada:
                coord = event
                window[coord].update(button_color=('white','#57C3FD'))
                event = window.read()[0]
                if coord != (7,7):
                    if (type(event) == int):
                        if (Lista_Atril[event] == ''):   #FichaTablero x FichaAtrilVacia
                            FichaVaciaxFichaTablero(event,coord,Dicc,Lista_Atril,window,LCO,LCOPR,CCD)
                        else:                            #FichaTablero x FichaAtril
                            Reemplazar_FichaxTablero(event,coord,Dicc,Lista_Atril,window)
                            window[coord].update(button_color=('black','#FDD357'))
                    else:
                        if Coord_Ocupada(LCOPR,event): #FichaTablero x FichaTablero:
                            aux = Dicc[event][0]
                            Dicc[event][0] = Dicc[coord][0]
                            Dicc[coord][0] = aux
                            window[event].update(Dicc[event][0])
                            window[coord].update(aux)
                            window[coord].update(button_color=('black','#FDD357'))
                        else:                        #FichaTablero x TableroVacio:
                            if (Coord_Ocupada(LCO,event) != True) and (Coord_Desbloqueada(CCD,event)):
                                Dicc[event][0] = Dicc[coord][0]
                                Dicc[coord][0] = ''
                                window[coord].update('',button_color=('white',Dicc[coord][1]))
                                window[event].update(Dicc[event][0],button_color=('black','#FDD357'))
                                LCO.remove(coord)
                                LCO.append(event)
                                LCOPR.remove(coord)
                                LCOPR.append(event)
                                Coord_Disponible(LCO,CCD)
                                Eliminar_Coords(CCD,coord)
                            else:
                                window[coord].update(button_color=('black','#FDD357'))
                else: #Coord es (7,7):
                    if Coord_Ocupada(LCOPR,event):
                        aux = Dicc[event][0]
                        Dicc[event][0] = Dicc[coord][0]
                        Dicc[coord][0] = aux
                        window[event].update(Dicc[event][0])
                        window[coord].update(aux)
                        window[coord].update(button_color=('black','#FDD357'))
                    elif (type(event) == int):
                        if (Lista_Atril[event] != ''):
                            Reemplazar_FichaxTablero(event,coord,Dicc,Lista_Atril,window)
                        window[coord].update(button_color=('black','#FDD357'))
            else:
                sg.popup('No puedes interactuar con las fichas ya colocadas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True) if Coord_Ocupada(LCO,event) else sg.popup('Primero selecciona una letra!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True)

def Turno(Turno_Usuario):
    if Turno_Usuario:
        sg.popup('Estas Listo?\nEmpiezas tu',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)
    else:
        sg.popup('Estas Listo?\nEmpieza la IA',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)

def Eliminar_Elementos_Ocupados_CDD(LCO,CCD):
    for L in LCO:
        CCD.discard(L)

def Validar(Palabra,LCOPR,Dicc):
    if len(LCOPR) > 1:
        if (LCOPR[0][0] == LCOPR[1][0]): #Si entra la palabra formada esta en Horizontal
            LCOPR = sorted(LCOPR, key=lambda tup: tup[1])
            for coord in LCOPR:
                Palabra = Palabra + Dicc[coord][0]
        else:                            #Sino esta en vertical
            LCOPR = sorted(LCOPR, key=lambda tup: tup[0])
            for coord in LCOPR:
                Palabra = Palabra + Dicc[coord][0]
        if verificar_Palabra(Palabra,'Facil'): #Facil a modo de ejemplo
            sg.popup(Palabra+' es una palabra valida :D',text_color='black',title='Ayuda',background_color='#57FD57',button_color=('black','white'),keep_on_top=True)
        else:
            sg.popup(Palabra+' no es una palabra valida D:',text_color='black',title='Ayuda',background_color='#FD5757',button_color=('Black','White'),keep_on_top=True)
            Palabra = ''
    else:
        sg.popup('Debes formar palabras de por lo menos 2 fichas_CPU!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True)
    return Palabra

def TerminarTurno(Palabra,Dicc,Lista_Atril,LCOPR,LCO,CCD,window):
    if (Palabra == '') and (LCOPR != []):
        Palabra = Validar(Palabra,LCOPR,Dicc)
        if (Palabra == ''):
            for Pos in range(len(Lista_Atril)):
                if (Lista_Atril[Pos] == ''): # Si esta posicion esta vacia:
                    FichaVaciaxFichaTablero(Pos,LCOPR[0],Dicc,Lista_Atril,window,LCO,LCOPR,CCD)
    return Palabra

def elimino_fichas_Usadas(fichas_CPU,Palabra):
    for x in range(len(Palabra)):
        fichas_CPU=fichas_CPU.replace(Palabra[x].upper(),"") #Elimino las fichas usadas
    return(fichas_CPU)

def intercambio_Fichas(fichas_CPU):
    global Cant_fichas
    for x in range(len(fichas_CPU)):
        Bolsa_Diccionario[fichas_CPU[x]]=(Bolsa_Diccionario[fichas_CPU[x]])+1
        Cant_fichas=Cant_fichas+1
    fichas_CPU=""
    for x in range(7):
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario)
    return(fichas_CPU)

def Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc):
    Palabra=Palabra.upper()
    for x in range(len(Palabra)):
        window[(coordenadas_CPU[0],coordenadas_CPU[1]+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
        Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+x)][0] =str(Palabra[x])
        LCO.append((coordenadas_CPU[0],coordenadas_CPU[1]+x))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc):
    Palabra=Palabra.upper()
    for y in range(len(Palabra)):
        window[(coordenadas_CPU[0]+y,coordenadas_CPU[1])].update(str(Palabra[y]),button_color=('black','#7D4DE4'))
        Dicc[(coordenadas_CPU[0]+y,coordenadas_CPU[1])][0] =str(Palabra[y])
        LCO.append((coordenadas_CPU[0]+y,coordenadas_CPU[1]))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU):
    global Cant_fichas
    Palabra=fichas_CPU
    intento=True
    puede_Colocarse=False
    if (contador_Turnos_CPU ==0):
        for x in range(7):
            fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario) #En la primera jugada toma 7 fichas aleatorias de la bolsa
            Palabra=formar_palabra(fichas_CPU,"Medio") #Facil a modo de ejemplo
        contador_Turnos_CPU=contador_Turnos_CPU+1
    else:
        Palabra=formar_palabra(fichas_CPU,"Medio")
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if(((contador_Turnos_CPU % 3)==0) and (Cant_fichas > 14 )):
        fichas_CPU=intercambio_Fichas(fichas_CPU)
        Palabra=formar_palabra(fichas_CPU,"Medio") #Facil a modo de ejemplo
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if Palabra != "":
        fichas_CPU=elimino_fichas_Usadas(fichas_CPU,Palabra)
        if CCD == set():
            for x in range(len(Palabra)):  #En el primer case , donde CCD esta vacio y se debe empezar en el cuadro 7,7
                Palabra=Palabra.upper()
                window[(7,7+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
                Dicc[7,7+x][0] =str(Palabra[x])
                LCO.append((7,7+x))
                Coord_Disponible(LCO,CCD)
                Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
        else:
            for x in range(len(CCD)) :
                if(intento):
                    coordenadas_CPU=Selector_de_coordenadas_disponibles(CCD)
                    if(coordenadas_CPU in CCD) and(not(coordenadas_CPU in LCO)):
                        if(((len(Palabra)+coordenadas_CPU[1])<15)and((len(Palabra)+coordenadas_CPU[1])>-1)):  #si se va a pasar del tablero al poner la palabra  verticalmente
                            for y in range(len(Palabra)):
                                if(((coordenadas_CPU[0],coordenadas_CPU[1]+(y)) in LCO)or(Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+(y))][0]!='')):#Si las coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc)
                                intento=False
                        elif(((len(Palabra)+coordenadas_CPU[0])<15)and((len(Palabra)+coordenadas_CPU[0])>-1)):#si se va a pasar del tablero al poner la palabra horizontalmente
                            for x in range(len(Palabra)):
                                if(((coordenadas_CPU[0]+(x),coordenadas_CPU[1]) in LCO)or(Dicc[(coordenadas_CPU[0]+(x),coordenadas_CPU[1])][0]!='')):#Si la coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc)
                                intento=False
    else:
        print("No hay palabra valida en este momento para la CPU ,la CPU pasa el turno")
    while(((len(fichas_CPU))<7)and(Cant_fichas >= 14)):          #Añado fichas de la bolsa para compeltar 7 al finalizar el turno
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario)
    if((len(fichas_CPU))<7):
        print("La CPU no tiene fichas suficientes para continuar , el juego termino")
    return(contador_Turnos_CPU,fichas_CPU)

def Importar_Datos():
    arch = open(r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Archivo_Opciones.csv','r')
    reader = csv.reader(arch)
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index != 0):
                if (row[0] == 'True'):
                    if (row[2] == 'True'):
                        dificultad =  'Facil'
                    elif (row[3] == 'True'):
                        dificultad =  'Normal'
                    elif (row[4] == 'True'):
                        dificultad =  'Dificil'
                    Usuario = row[1]
                    Lista_Lotes = [int(float(row[5])),int(float(row[6])),int(float(row[7])),int(float(row[8])),int(float(row[9])),int(float(row[10])),int(float(row[11]))]
                    arch.close()
                    return Usuario,dificultad,Lista_Lotes
            else:
                index = index + 1

def Calcular_Puntaje(Palabra,Dicc_Puntajes):
    PPR = 0
    for letra in Palabra:
        PPR = PPR + Dicc_Puntajes[letra]
    return PPR


#PROGRAMA PRINCIPAL
def genero_Tablero():
    Usuario,Dificultad,Lista_Lotes = Importar_Datos()

    Dicc_Puntajes = {"A":Lista_Lotes[0],"B":Lista_Lotes[2],"C":Lista_Lotes[1],"D":Lista_Lotes[1],"E":Lista_Lotes[0],"F":Lista_Lotes[3],"G":Lista_Lotes[1],"H":Lista_Lotes[3],"I":Lista_Lotes[0],"J":Lista_Lotes[4],"K":Lista_Lotes[5],"L":Lista_Lotes[0],"LL":Lista_Lotes[5],"M":Lista_Lotes[2],"N":Lista_Lotes[0],
                      "Ñ":Lista_Lotes[5],"O":Lista_Lotes[0],"P":Lista_Lotes[2],"Q":Lista_Lotes[5],"R":Lista_Lotes[0],"RR":Lista_Lotes[5],"S":Lista_Lotes[0],"T":Lista_Lotes[0],"U":Lista_Lotes[0],"V":Lista_Lotes[3],"W":Lista_Lotes[5],"X":Lista_Lotes[5],"Y":Lista_Lotes[3],"Z":Lista_Lotes[6]}

    Lista_Atril = []
    Terminar = [False]
    Dicc = Generar_Dicc()
    diseño = [ [sg.Column((Layout_Tabla(Lista_Atril))),
                sg.Column(Layout_Columna())] ]
    window = sg.Window('Tablero',diseño ,location=(400,0),finalize=True)
    Dicc = Update_Tablero(window,Dicc)
    window['PuntosUsuario'].update('Puntos' + Usuario)
    Turno_Usuario = bool(random.getrandbits(1))
    Turno(Turno_Usuario)
    Fin = False
    fichas_CPU=""
    contador_Turnos_CPU=0
    Puntaje_Total = 0
    CCD=set()                   #Conjunto de Coordenadas  Disponibles
    LCO = []                    #Lista de Coordenadas Ocupadas
    while True:
        LCOPR = []              #Lista de Coordenadas Ocupadas Por Ronda
        while (Turno_Usuario):  #Mientras sea el turno del usuario:
            Palabra = ''
            event = window.Read()[0]
            if event in (None, 'Salir'):

                event_popup = sg.popup_yes_no('Ey! estas saliendo en mitad de una partida\n¿Quieres posponerla?',title='Aviso',keep_on_top=True)
                #if (event_popup == 'Yes'):
                    #Pospone la partida
                #else:
                    #No la pospone y sale sin guardar
                Fin = True
                break

            Acciones_Usuario(event,Dicc,Lista_Atril,LCO,LCOPR,CCD,window)

            if (event == 'Validar'):
                Palabra = Validar(Palabra,LCOPR,Dicc)

            elif (event == 'Terminar turno'):
                Palabra = TerminarTurno(Palabra,Dicc,Lista_Atril,LCOPR,LCO,CCD,window)

                if (Palabra != ''):
                    PPR = Calcular_Puntaje(Palabra,Dicc_Puntajes) #Puntaje por ronda
                    Puntaje_Total = Puntaje_Total + PPR
                    window['PuntajeUsuario'].update(str(Puntaje_Total))

                Llenar_Atril(Lista_Atril,window)
                break

        while (Turno_Usuario == False):
            contador_Turnos_CPU,fichas_CPU=Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU)
            break
        if Fin:
            Fin_Tiempo(Terminar)
            break
        Update_Fichas_Colocadas(LCOPR,window)
        Turno_Usuario = not Turno_Usuario
    window.close()
    return(event)
#ProgramaPrincipal-------------
if __name__ == "__main__":
    genero_Tablero()
