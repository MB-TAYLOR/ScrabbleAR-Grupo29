import json
import PySimpleGUI as sg
from Opciones import Ventana_Opciones
from TabladePosiciones import Tabla
from Tablero import genero_Tablero
from ventana_Ayuda import Ayuda
from playsound import playsound
import csv
from Generadores import identificador_carpeta_error
import tkinter           #Para poder usar su excepcion se tuvo que importar tkinter

#Aca Arranca La Pantalla Principal----------------------------------------------------------------------------------------------------------------------------------------------

def obtengo_Perfil():                                #Busco el nombre del ultimo usuario registrado
    archivo_csv=open('ScrabbleAR_Datos\Archivo_Opciones.csv','r')
    perfiles=csv.reader(archivo_csv)
    for perfil in perfiles:
        if((len(perfil))>0):
            perfil_Actual=perfil[1]
    archivo_csv.close()
    return(perfil_Actual)

def establezco_PP():
#Columnas
    columna_izquierda=[ [sg.Text("USUARIO",relief='groove',font=('default',15),text_color='orange',size=(27,1),pad=((6,5),(3,3)),justification='center')],
                        [sg.Frame('',[[sg.Text(obtengo_Perfil(),font=('default',19),size=(19,1),justification='center')]],relief="sunken",pad=((5,5),(3,30)))],
                        [sg.Text('.',text_color='orange',font=('webdings',40),relief='solid'),
                        sg.Button(button_text="JUGAR",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Text('@',text_color='orange',font=('webdings',40),relief='solid'),
                        sg.Button(button_text="OPCIONES",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Text('%',text_color='orange',font=('webdings',40),relief='solid'),
                        sg.Button(button_text="TOP 10",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Text('s',text_color='orange',font=('webdings',40),relief='solid'),
                        sg.Button(button_text="INSTRUCCIONES",key="AYUDA",font=('impact',20),size=(18,1),pad=(0,20))],
                        [sg.Text('r',text_color='orange',font=('webdings',40),relief='solid',pad=((5,5),(80,3))),
                        sg.Button(button_text="SALIR",font=('Impact',20),size=(9,1),pad=((5,5),(80,3)))]  ]

    Linea = [[sg.Image(r'ScrabbleAR_Imagenes_png\Linea.png')]]

    columna_derecha=[ [sg.Text("SCRABBLE-AR",font=("ink free",40),pad=(130,0))] ]

#Diseño
    diseño=[        [sg.Column(columna_izquierda),
                    sg.Column(Linea),
                    sg.Column(columna_derecha)]       ]

#Aplico y muestro

    window = sg.Window('Pantalla Principal',diseño,location=(540,100),size=(1035,650))
    boton_cliqueado,datos_ingresados=window.Read()
    playsound(r'ScrabbleAR_Sonidos/Click.mp3',block=False)
    while True:
        if boton_cliqueado in(None,'SALIR'):
            break
        elif boton_cliqueado == 'JUGAR':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((genero_Tablero())in(None,'Salir')):
                establezco_PP()
            break
        elif boton_cliqueado =='TOP 10':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((Tabla())in(None,'Salir')):
                establezco_PP()
            break
        elif boton_cliqueado =='OPCIONES':
            #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            window.close()
            if((Ventana_Opciones())in(None,'Salir')):
                establezco_PP()
            break
        elif boton_cliqueado=="AYUDA":
            window.close()
            if((Ayuda())in(None,'Salir')):
                establezco_PP()
            break

    return(boton_cliqueado)

#Programa Principal-----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    identificador_carpeta_error(establezco_PP)
