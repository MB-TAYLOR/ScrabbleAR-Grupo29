import json
import PySimpleGUI as sg
import csv

#Aca Arranca La Pantalla Principal----------------------------------------------------------------------------------------------------------------------------------------------


#Columnas
columna_izquierda=[     [sg.Text("USUARIO:(USUARIO)")],  #Tomar el nombre del usuario del archivo que se deberia generar desde el menu opciones
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
        print(boton_cliqueado)
        window.close()
        #Aca abro la nueva ventana en el mismo lugar que la anterior , luego de cerrar la principal
        break
