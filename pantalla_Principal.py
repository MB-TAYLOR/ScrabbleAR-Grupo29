import json
import PySimpleGUI as sg
from Opciones import Ventana_Opciones
import csv

#Aca Arranca La Pantalla Principal----------------------------------------------------------------------------------------------------------------------------------------------
def obtengo_Perfil():
    archivo_csv=open('Archivo_Opciones.csv','r')
    perfiles=csv.reader(archivo_csv)
    for perfil in perfiles:
        if((len(perfil))>0):
            perfil_Actual=perfil[0]
    archivo_csv.close()
    return(perfil_Actual)

def establezco_PP(nombre):
#Columnas
    columna_izquierda=[     [sg.Text("USUARIO:"+nombre)],  #Tomar el nombre del usuario del archivo que se deberia generar desde el menu opciones
                            [sg.Button(button_text="JUGAR",size=(40,4),pad=(0,20))],
                            [sg.Button(button_text="OPCIONES",size=(40,4),pad=(0,20))],
                            [sg.Button(button_text="VER TOP 10",size=(40,4),pad=(0,20))],                          ]

    columna_derecha=[       [sg.Text("ESCRABBLE-AR",font=("default",40),pad=(130,0))],
                            [sg.Button(button_text="SALIR",size=(10,3),pad=((550,0),(510,0)))]       ]

#Diseño
    diseño=[        [sg.Column(columna_izquierda),sg.Column(columna_derecha)]       ]

#Aplico y muestro

    window = sg.Window('Pantalla Principal',diseño,location=(540,100),size=(1035,650))
    boton_cliqueado,datos_ingresados=window.Read()
    while True:
        if boton_cliqueado in(None,'SALIR'):
            break
        if boton_cliqueado == 'JUGAR':
            print(boton_cliqueado)
            window.close()
        #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            break
        elif boton_cliqueado =='VER TOP 10':
            print(boton_cliqueado)
        #Aca abro una ventana al lado de la principal
            break
        elif boton_cliqueado =='OPCIONES':
            window.close()
            if(Ventana_Opciones()=='Salir'):
                establezco_PP(obtengo_Perfil())

        #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
            break
    return()

#Programa Principal-----------------------------------------------
if __name__ == "__main__":
    establezco_PP(obtengo_Perfil())