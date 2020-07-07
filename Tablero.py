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

def tiempo_dificultad(dificultad):
    tiempo_ronda=0
    jugadores=2
    rondas_totales=30
    if(dificultad=="Facil"):
        tiempo_ronda=60
        secs =tiempo_ronda*jugadores*rondas_totales
    elif(dificultad=="Normal"):
        tiempo_ronda=45
        secs=tiempo_ronda*jugadores*rondas_totales
    elif (dificultad =="Dificil"):
        tiempo_ronda=30
        secs=tiempo_ronda*jugadores*rondas_totales
    return((secs*100),(tiempo_ronda*100))

def intercambio_Fichas_CPU(fichas_CPU,Bolsa_Diccionario,Cant_fichas):
    for x in range(len(fichas_CPU)):
        Bolsa_Diccionario[fichas_CPU[x]]=(Bolsa_Diccionario[fichas_CPU[x]])+1
        Cant_fichas=Cant_fichas+1
    fichas_CPU=""
    for x in range(7):
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    return(fichas_CPU,Cant_fichas)

def aleatorio_Dificil():
    lista_opciones=["verb","sus","adj"]
    x=random.randint(0,2)
    return(lista_opciones[x])

def Letra_Bolsa(Bolsa_Diccionario,Cant_fichas):
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

    layout = [ [sg.Text('Tiempo Disponible',font=("impact",20),pad=((15,3),(5,3)))],
               [sg.Text("00:00",font=("Bahnschrift",20),key=('Tiempo_Ronda'),pad=((35,3),(5,3))),sg.Text('|',font=("Bahnschrift",20)),sg.Text("00:00",font=("Bahnschrift",20),key=('Tiempo'))],
               [sg.Text('__________________________________')],
               [sg.Text('Puntos  CPU',key='PuntosCPU',font=("impact",20))],
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

def Layout_Tabla(Lista_Atril,Bolsa_Diccionario,Cant_fichas):
    MAX_ROWS = MAX_COL = 15 #ACA????
    formato_fichas_cpu={'filename':r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Ficha.png','size':(40,40),'pad':(7,3)  }

    #formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Ficha.png','image_size':(40,40),'pad':(7,3)  }
    #Para luego reemplazar los colores dados por el boton con imagenes
    Letra_1=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_1)
    Letra_2=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_2)
    Letra_3=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_3)
    Letra_4=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_4)
    Letra_5=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_5)
    Letra_6=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_6)
    Letra_7=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    Lista_Atril.append(Letra_7)

    layout = [[sg.Text('',key='texto1',pad=(45,3)),(sg.Image(**formato_fichas_cpu,key='fichasbot1')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot2')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot3')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot4')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot5')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot6')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot7'))],
                [(sg.Image(filename=r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Atril_back.png',key='atril',pad=(20,3)))]]

    layout.extend([[sg.Button('', size=(4, 2),key=(i,j),pad=(0,0))for j in range(MAX_COL)] for i in range(MAX_ROWS)])

    layout.extend([[sg.Text('',key='texto2',pad=(28,3)),
                    (sg.Button(button_text=Letra_1,key=0,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_2,key=1,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_3,key=2,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_4,key=3,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_5,key=4,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_6,key=5,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'))),
                    (sg.Button(button_text=Letra_7,key=6,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357')))],
                    [(sg.Image(filename=r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Atril.png',key='texto'))]])

    return layout

def Llenar_Atril(Lista_Atril,window,Bolsa_Diccionario,Cant_fichas):
    for pos in range(len(Lista_Atril)):
        if (Lista_Atril[pos] == ''):
            Lista_Atril[pos] = Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
            window[pos].update(Lista_Atril[pos])

def Coord_Ocupada(LCO,event):
    if (event in LCO):
        return True
    else:
        return False

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

def Update_Fichas_Colocadas(LCOPR,window):
    for coord in LCOPR:
        window[coord].update(button_color=('black','#E4BE4D'))

def Mensaje_Turno(Turno_Usuario):
    if Turno_Usuario:
        sg.popup('Estas Listo?\nEs tu turno',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)
    else:
        sg.popup('Estas Listo?\nEs el turno de la IA',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)

def Eliminar_Elementos_Ocupados_CDD(LCO,CCD):
    for L in LCO:
        CCD.discard(L)

def Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega):
    if (LCOPR[0][0] == LCOPR[1][0]): #Si entra la palabra formada esta en Horizontal
        LCOPR = sorted(LCOPR, key=lambda tup: tup[1])
        for coord in LCOPR:
            Palabra = Palabra + Dicc[coord][0]
    else:                            #Sino esta en vertical
        LCOPR = sorted(LCOPR, key=lambda tup: tup[0])
        for coord in LCOPR:
            Palabra = Palabra + Dicc[coord][0]
    if verificar_Palabra(Palabra,Dificultad,Dificil_se_juega):
        sg.popup(Palabra+' es una palabra valida :D',text_color='black',title='Ayuda',background_color='#57FD57',button_color=('black','white'),keep_on_top=True,non_blocking=True)
    else:
        sg.popup(Palabra+' no es una palabra valida D:',text_color='black',title='Ayuda',background_color='#FD5757',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
        Palabra = ''
    return Palabra

def elimino_fichas_Usadas(fichas_CPU,Palabra):
    for x in range(len(Palabra)):
        fichas_CPU=fichas_CPU.replace(Palabra[x].upper(),"") #Elimino las fichas usadas
    return(fichas_CPU)

def Importar_Datos():
    arch = open(r'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Archivo_Opciones.csv','r',encoding="utf8")
    reader = csv.reader(arch)
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index != 0):
                if (row[0] == 'True'):
                    if (row[2] == 'True'):
                        dificultad =  'Facil'
                    elif (row[3] == 'True'):
                        dificultad =  'Medio'
                    elif (row[4] == 'True'):
                        dificultad =  'Dificil'
                    Usuario = row[1]
                    Lista_Lotes = [int(float(row[5])),int(float(row[6])),int(float(row[7])),int(float(row[8])),int(float(row[9])),int(float(row[10])),int(float(row[11]))]
                    arch.close()
                    Dicc_Puntajes = {"A":int(Lista_Lotes[0]),"B":int(Lista_Lotes[2]),"C":int(Lista_Lotes[1]),"D":int(Lista_Lotes[1]),"E":int(Lista_Lotes[0]),"F":int(Lista_Lotes[3]),"G":int(Lista_Lotes[1]),"H":int(Lista_Lotes[3]),"I":int(Lista_Lotes[0]),"J":int(Lista_Lotes[4]),"K":int(Lista_Lotes[5]),"L":int(Lista_Lotes[0]),"M":int(Lista_Lotes[2]),"N":int(Lista_Lotes[0]),
                                      u"Ñ":int(Lista_Lotes[5]),"O":int(Lista_Lotes[0]),"P":int(Lista_Lotes[2]),"Q":int(Lista_Lotes[5]),"R":int(Lista_Lotes[0]),"S":int(Lista_Lotes[0]),"T":int(Lista_Lotes[0]),"U":int(Lista_Lotes[0]),"V":int(Lista_Lotes[3]),"W":int(Lista_Lotes[5]),"X":int(Lista_Lotes[5]),"Y":int(Lista_Lotes[3]),"Z":int(Lista_Lotes[6])}

                    Dicc_Bolsa={"A":int(row[12]),"B":int(row[13]),"C":int(row[14]),"D":int(row[15]),"E":int(row[16]),"F":int(row[17]),"G":int(row[18]),"H":int(row[19]),"I":int(row[20]),"J":int(row[21]),"K":int(row[22]),"L":int(row[23]),"M":int(row[24]),"N":int(row[25]),
                                      u"Ñ":int(row[26]),"O":int(row[27]),"P":int(row[28]),"Q":int(row[29]),"R":int(row[30]),"S":int(row[31]),"T":int(row[32]),"U":int(row[33]),"V":int(row[34]),"W":int(row[35]),"X":int(row[36]),"Y":int(row[37]),"Z":int(row[38])}

                    return Usuario,dificultad,Dicc_Puntajes,Dicc_Bolsa
            else:
                index = index + 1

def Calcular_Puntaje(Palabra,Dicc_Puntajes):
    PPR = 0
    for letra in Palabra:
        PPR = PPR + Dicc_Puntajes[letra]
    return PPR

def Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc):
    for x in range(len(Palabra)):
        window[(coordenadas_CPU[0],coordenadas_CPU[1]+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
        Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+x)][0] =str(Palabra[x])
        LCO.append((coordenadas_CPU[0],coordenadas_CPU[1]+x))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc):
    for y in range(len(Palabra)):
        window[(coordenadas_CPU[0]+y,coordenadas_CPU[1])].update(str(Palabra[y]),button_color=('black','#7D4DE4'))
        Dicc[(coordenadas_CPU[0]+y,coordenadas_CPU[1])][0] =str(Palabra[y])
        LCO.append((coordenadas_CPU[0]+y,coordenadas_CPU[1]))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU,Dificultad,Dificil_se_juega,Bolsa_Diccionario,Cant_fichas,Dicc_Puntajes,PT_CPU):
    CCD_CPU=CCD
    Palabra=fichas_CPU
    intento=True
    puede_Colocarse=False
    if (contador_Turnos_CPU ==0):
        for x in range(7):
            fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas) #En la primera jugada toma 7 fichas aleatorias de la bolsa
            Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    else:
        Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if(((contador_Turnos_CPU % 3)==0) and (Cant_fichas > 14 )):
        fichas_CPU,Cant_fichas=intercambio_Fichas_CPU(fichas_CPU,Bolsa_Diccionario,Cant_fichas)
        Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if Palabra != "":
        Palabra=Palabra.upper()
        fichas_CPU=elimino_fichas_Usadas(fichas_CPU,Palabra)
        if CCD_CPU == set():
            for x in range(len(Palabra)):  #En el primer case , donde CCD esta vacio y se debe empezar en el cuadro 7,7
                window[(7,7+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
                Dicc[7,7+x][0] =str(Palabra[x])
                LCO.append((7,7+x))
                Coord_Disponible(LCO,CCD)
                Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
            PPR_CPU = Calcular_Puntaje(Palabra,Dicc_Puntajes)
            PT_CPU = PT_CPU + PPR_CPU
            window['PuntajeCPU'].update(str(PT_CPU))
        else:
            for x in range(len(CCD)) :
                if(intento):
                    coordenadas_CPU=Selector_de_coordenadas_disponibles(CCD_CPU)
                    if(coordenadas_CPU in CCD_CPU) and(not(coordenadas_CPU in LCO)):
                        if(((len(Palabra)+coordenadas_CPU[1])<15)and((len(Palabra)+coordenadas_CPU[1])>-1)):  #si se va a pasar del tablero al poner la palabra  verticalmente
                            for y in range(len(Palabra)):
                                if(((coordenadas_CPU[0],coordenadas_CPU[1]+(y)) in LCO)or(Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+(y))][0]!='')):#Si las coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    CCD_CPU.discard(coordenadas_CPU)
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc)
                                PPR_CPU = Calcular_Puntaje(Palabra,Dicc_Puntajes)
                                PT_CPU = PT_CPU + PPR_CPU
                                window['PuntajeCPU'].update(str(PT_CPU))
                                intento=False
                        elif(((len(Palabra)+coordenadas_CPU[0])<15)and((len(Palabra)+coordenadas_CPU[0])>-1)):#si se va a pasar del tablero al poner la palabra horizontalmente
                            for x in range(len(Palabra)):
                                if(((coordenadas_CPU[0]+(x),coordenadas_CPU[1]) in LCO)or(Dicc[(coordenadas_CPU[0]+(x),coordenadas_CPU[1])][0]!='')):#Si la coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    CCD_CPU.discard(coordenadas_CPU)
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc)
                                PPR_CPU = Calcular_Puntaje(Palabra,Dicc_Puntajes)
                                PT_CPU = PT_CPU + PPR_CPU
                                window['PuntajeCPU'].update(str(PT_CPU))
                                intento=False
            if((intento)and(len(CCD_CPU)>1)):
                print("El robot no tiene una posicion valida para colocar su palabra") #Implementar que se vuelva a buscar uan palabra pero mas corta
    else:
        print("No hay palabra valida en este momento para la CPU ,la CPU pasa el turno")
    while(((len(fichas_CPU))<7)and(Cant_fichas >= 14)):          #Añado fichas de la bolsa para compeltar 7 al finalizar el turno
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    if((len(fichas_CPU))<7):
        print("La CPU no tiene fichas suficientes para continuar , el juego termino")
    return(contador_Turnos_CPU,fichas_CPU,Cant_fichas,PT_CPU)

def Actualizar_CFT(CFT,Dicc_Bolsa):
    CFT = 0
    for cant in Dicc_Bolsa.values():
        CFT = CFT + cant
    return CFT
def Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window):
    for Pos in range(len(Lista_Atril)):
        if (Lista_Atril[Pos] == ''): # Si esta posicion esta vacia:
            Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,LCOPR[0],Pos,window)

def Validar(LCOPR,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega):
    if Palabra_bien_colocada(LCOPR):
        if PrimerRonda:
            if ((7,7) in LCOPR):
                Palabra = Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega)
            else:
                sg.popup('Debes colocar una letra en la casilla "Inicio"!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
        else:
            Palabra = Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega)
    return Palabra

def Palabra_bien_colocada(LCOPR):
    if len(LCOPR) > 1:
        Vertical = True
        Horizontal = True
        for i in range(2):
            if (Horizontal):
                LCOPR = sorted(LCOPR, key=lambda tup: tup[1])
                for x in range(len(LCOPR)-1):
                    sig = x + 1
                    if (LCOPR[x][0] != LCOPR[sig][0]) or ((LCOPR[x][1] + 1) != LCOPR[sig][1]):
                        Horizontal = False
            else:
                LCOPR = sorted(LCOPR, key=lambda tup: tup[0])
                for x in range(len(LCOPR)-1):
                    sig = x + 1
                    if (LCOPR[x][1] != LCOPR[sig][1]) or ((LCOPR[x][0] + 1) != LCOPR[sig][0]):
                        Vertical = False
        if Horizontal or Vertical:
            return True
        else:
            sg.popup('Esta palabra esta mal colocada!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
            return False
    else:
        sg.popup('Debes formar palabras de por lo menos 2 fichas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
        return False

def TerminarTurno(LCOPR,LCO,CCD,Dicc,Lista_Atril,PTU,Palabra,Dificultad,PrimerRonda,Dificil_se_juega,Dicc_Puntajes,Dicc_Bolsa,CFT,window):
    if (Palabra == '') and (LCOPR != []): #Si no se valido antes Y en el tablero hay fichas:
        Palabra = Validar(LCOPR,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega)

    if (Palabra != ''):
        PPR = Calcular_Puntaje(Palabra,Dicc_Puntajes) #Puntaje por ronda
        PTU = PTU + PPR
        window['PuntajeUsuario'].update(str(PTU))
        Llenar_Atril(Lista_Atril,window,Dicc_Bolsa,CFT)
    else:
        Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window)
    return PTU


def Actualizar_LCO(LCOPR,LCO):
    for coord in LCOPR:
        LCO.append(coord)

def Intercambio_FichasTablero(LCOPR,Dicc,event1,event2,window):
    if Coord_Ocupada(LCOPR,event2):
        aux = Dicc[event2][0]
        Dicc[event2][0] = Dicc[event1][0]
        Dicc[event1][0] = aux
        window[event2].update(Dicc[event2][0])
        window[event1].update(aux)
    window[event1].update(button_color=('black','#FDD357'))

def Intercambio_FichasAtril(Lista_Atril,Pos_letra1,Pos_letra2,window):
    if (Pos_letra1 != Pos_letra2):
        window[Pos_letra1].update(Lista_Atril[Pos_letra2])
        window[Pos_letra2].update(Lista_Atril[Pos_letra1])
        aux = Lista_Atril[Pos_letra2]
        Lista_Atril[Pos_letra2] = Lista_Atril[Pos_letra1]
        Lista_Atril[Pos_letra1] = aux
    window[Pos_letra1].update(button_color=('black','#FDD357'))

def Intercambio_Fichas(Dicc,Lista_Atril,event1,event2,window):
    aux = Dicc[event1][0]
    Dicc[event1][0] = Lista_Atril[event2]
    Lista_Atril[event2] = aux
    window[event1].update(Dicc[event1][0],button_color=('black','#FDD357'))
    window[event2].update(Lista_Atril[event2],button_color=('black','#FDD357'))

def Colocar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,Letra1,event1,event2,window):
    Dicc[event2][0] = Letra1
    window[event2].update(Letra1,button_color=('black','#FDD357'))
    Lista_Atril[event1] = ''
    window[event1].update('')
    LCOPR.append(event2)
    Coord_Disponible(LCOPR,CCD) #Ya que LCOPR contiene unicamente las fichas actuales se tiene
    Coord_Disponible(LCO,CCD)   #que usar LCO para completar la actualizacion/eliminacion de elementos en CCD
    Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
    Eliminar_Elementos_Ocupados_CDD(LCOPR,CCD)
    window[event1].update(button_color=('black','#FDD357'))

def Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window):
    Lista_Atril[event2] = Dicc[event1][0]
    window[event1].update('',button_color=('white',Dicc[event1][1]))
    window[event2].update(Dicc[event1][0])
    Dicc[event1][0] = ''
    LCOPR.remove(event1)
    Eliminar_Coords(CCD,event1) #Ya que LCOPR contiene unicamente las fichas actuales se tiene
    Coord_Disponible(LCOPR,CCD) #que usar LCO para completar la actualizacion/eliminacion de elementos en CCD
    Coord_Disponible(LCO,CCD)
    Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
    Eliminar_Elementos_Ocupados_CDD(LCOPR,CCD)

def Acciones_Usuario(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window):
    if (not (event2 in LCO)): #Esto es para saber si por ejemplo, Se quiere intercambiar una (fichaAtril o FichaTablero) con una ficha ya colocada

        if (type(event1) == int) and (type(event2) == tuple):        #Atril X Tablero:
            if (Coord_Ocupada(LCOPR,event2)):                       #Intercambio FichaAtril X Tablero:
                Intercambio_Fichas(Dicc,Lista_Atril,event2,event1,window)
            else:                                                   #Colocar Ficha:
                Colocar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,Lista_Atril[event1],event1,event2,window)

        elif (type(event1) == tuple) and (type(event2) == int):     #Tablero X Atril:
            if (Lista_Atril[event2] != ''):                         #Intercambio FichaTablero X FichaAtril:
                Intercambio_Fichas(Dicc,Lista_Atril,event1,event2,window)
            else:                                                   #Retirar Ficha:
                Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window)

        elif (type(event1) == tuple) and (type(event2) == tuple):   #Intercambio FichasTablero:
            Intercambio_FichasTablero(LCOPR,Dicc,event1,event2,window)

        elif (type(event1) == int) and (type(event2) == int):       #Intercambio FichasAtril:
            Intercambio_FichasAtril(Lista_Atril,event1,event2,window)
    else:
        window[event1].update(button_color=('black','#FDD357'))
        sg.popup('No puedes interactuar con las fichas ya colocadas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)

def Boton_Intercambiar_Fichas(LCOPR,LCO,CCD,CFT,LPI,Dicc,Dicc_Bolsa,Lista_Atril,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles,event,window):
    if (type(event) == int):
        if event in LPI:
            LPI.remove(event)
            window[event].update(button_color=('black','#FDD357'))
        else:
            LPI.append(event)
            window[event].update(button_color=('white','#57C3FD'))

    elif (event == "Intercambiar fichas"):
        if Boton_Intercambiar:   #Intercambia las fichas y termina
            if (LPI != []) and CFT >= len(LPI):
                for pos in LPI: #Agrego las fichas seleccionadas a la bolsa
                    Dicc_Bolsa[Lista_Atril[pos]] = Dicc_Bolsa[Lista_Atril[pos]] + 1
                for pos in LPI:  #Y de la bolsa, se le da fichas random al usuario
                    x = random.randint(0,(len(Dicc_Bolsa.keys())-1))
                    Letra = list(Dicc_Bolsa.keys())[x]
                    while (Dicc_Bolsa[Letra] <= 0):
                        x = random.randint(0,(len(Dicc_Bolsa.keys())-1))
                        Letra = list(Dicc_Bolsa.keys())[x]
                    Lista_Atril[pos] = Letra
                    Dicc_Bolsa[Lista_Atril[pos]] = Dicc_Bolsa[Lista_Atril[pos]] - 1
                    window[pos].update(Lista_Atril[pos],button_color=('black','#FDD357'))
                Turnos_Disponibles = Turnos_Disponibles - 1
                Se_Intercambio_Ficha = True
                CFT = Actualizar_CFT(CFT,Dicc_Bolsa)
                window[event].update(button_color=('white','#283B5B'))
            else:
                sg.popup('No has intercambiado ninguna ficha! no pierdes el turno',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
                window[event].update(button_color=('white','#283B5B'))
            Boton_Intercambiar = False
        else: #Recien "Clickeo" el boton intercambiar Fichas
            if Turnos_Disponibles != 1:
                sg.popup('Te quedan '+str(Turnos_Disponibles)+' turnos disponibles\nSelecciona las fichas del atril que quieras cambiar!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
            else:
                sg.popup('Este es el ultimo turno en el que puedes cambiar fichas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
            Boton_Intercambiar = True
            window[event].update(button_color=('black','#57C3FD'))
            Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window)
    elif event != 'Reloj':
        sg.popup('Debes seleccionar fichas del Atril!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
    return CFT,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles

#PROGRAMA PRINCIPAL
def genero_Tablero():
    Usuario,Dificultad,Dicc_Puntajes,Dicc_Bolsa = Importar_Datos()
    if(Dificultad=="Dificil"):
        Dificil_se_juega=aleatorio_Dificil()
    else:
        Dificil_se_juega="Default"

    Lista_Atril = []
    Terminar = [False]
    Dicc = Generar_Dicc()
    CFT = 0
    CFT = Actualizar_CFT(CFT,Dicc_Bolsa) #Cantidad Fichas Totales
    diseño = [ [sg.Column((Layout_Tabla(Lista_Atril,Dicc_Bolsa,CFT))),
                sg.Column(Layout_Columna())] ]
    window = sg.Window('Tablero',diseño ,location=(400,0),finalize=True)
    Dicc = Update_Tablero(window,Dicc)
    window['PuntosUsuario'].update('Puntos  ' + Usuario)
    Turno_Usuario = bool(random.getrandbits(1))
    Fin = False
    fichas_CPU=""
    contador_Turnos_CPU=0
    PT_CPU=0                    #Puntaje Total CPU
    PTU = 0                     #Puntaje Total Usuario
    CCD=set()                   #Conjunto de Coordenadas  Disponibles
    LCO = []                    #Lista de Coordenadas Ocupadas
    Se_necesitan_dos = False
    event1 = ''
    Tiempo,tiempo_ronda=tiempo_dificultad(Dificultad)
    PrimerRonda = True
    Turnos_Disponibles = 3
    while True:
        LPI = []                #Lista de Posiciones de Intercambio (Para Intecambiar fichas)
        LCOPR = []              #Lista de Coordenadas Ocupadas Por Ronda
        puedo_intercambiar=True
        Boton_Intercambiar = False
        Se_Intercambio_Ficha = False
        tiempo_jugador=tiempo_ronda
        Mensaje_Turno(Turno_Usuario)
        while (Turno_Usuario):  #Mientras sea el turno del usuario:
            Palabra = ''
            event = window.Read(timeout=10,timeout_key='Reloj')[0]
            window['Tiempo'].update("{}:{}".format(((Tiempo//100)//60),((Tiempo//100)%60)))
            Tiempo -= 1
            tiempo_jugador = str(tiempo_jugador)
            window['Tiempo_Ronda'].update("00:{}".format(tiempo_jugador[0:2]))
            tiempo_jugador = int(tiempo_jugador)
            tiempo_jugador-=1

            if event in (None, 'Salir'):
                event_popup = sg.popup_yes_no('Ey! estas saliendo en mitad de una partida\n¿Quieres posponerla?',title='Aviso',keep_on_top=True)
                #if (event_popup == 'Yes'):
                    #Pospone la partida
                #else:
                    #No la pospone y sale sin guardar
                Fin = True
                puedo_intercambiar=False
                break

            if (((type(event) == int) or (type(event) == tuple)) and (Boton_Intercambiar == False)):
                if event1 == '':
                    event1 = event
                    if ((Lista_Atril[event1] != '') if type(event1) == int else Coord_Ocupada(LCOPR,event1)):
                        window[event1].update(button_color=('white','#57C3FD'))
                    else:
                        if (type(event1) == tuple):
                            sg.popup('No puedes interactuar con las fichas ya colocadas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True) if Coord_Ocupada(LCO,event) else sg.popup('Primero selecciona una letra!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
                        event1 = ''
                else:
                    Acciones_Usuario(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event,window)
                    event1 = ''

            elif (event == 'Validar') and (Boton_Intercambiar == False):
                Palabra = Validar(LCOPR,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega)

            elif (((event == 'Terminar turno') or Se_Intercambio_Ficha) and (Boton_Intercambiar == False)):
                PTU = TerminarTurno(LCOPR,LCO,CCD,Dicc,Lista_Atril,PTU,Palabra,Dificultad,PrimerRonda,Dificil_se_juega,Dicc_Puntajes,Dicc_Bolsa,CFT,window)
                CFT = Actualizar_CFT(CFT,Dicc_Bolsa)
                break

            elif (((event == "Intercambiar fichas") or (Boton_Intercambiar)) and (Turnos_Disponibles != 0)):
                CFT,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles = Boton_Intercambiar_Fichas(LCOPR,LCO,CCD,CFT,LPI,Dicc,Dicc_Bolsa,Lista_Atril,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles,event,window)

        while (Turno_Usuario == False):
            contador_Turnos_CPU,fichas_CPU,CFT,PT_CPU=Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU,Dificultad,Dificil_se_juega,Dicc_Bolsa,CFT,Dicc_Puntajes,PT_CPU)
            break
        if Fin:
            break
        Update_Fichas_Colocadas(LCOPR,window)
        Turno_Usuario = not Turno_Usuario
        Actualizar_LCO(LCOPR,LCO)
        PrimerRonda = False
    window.close()
    return(event)
#ProgramaPrincipal-------------
if __name__ == "__main__":
    genero_Tablero()
