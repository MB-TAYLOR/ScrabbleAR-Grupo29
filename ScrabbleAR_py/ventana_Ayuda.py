import PySimpleGUI as sg
from playsound import playsound
from ScrabbleAR_py.Generadores import identificador_carpeta_error

def Comprobaciones(Boton_actual,pagina,window):
    '''Condiciones para activar o desactivar los botones "<" y ">"  '''
    if (Boton_actual=='Como_Se_Juega') or (Boton_actual=='Opciones'):
        if (pagina > 0) and (pagina < 3):
            window['>'].update(disabled=False)
            window['<'].update(disabled=False)
        elif (pagina == 3):
            window['>'].update(disabled=True)
        elif (pagina == 0):
            window['<'].update(disabled=True)


def Ayuda():
    ''' Diseño de la ventana Ayuda , se generan los botones para navegar entre la distinta informacion y la zona donde se muestra dicha informacion'''
    Dicc_Informacion={'Sobre_El_Juego':[r'ScrabbleAR_Imagenes_png\SobreElJuego.png'],
                      'Como_Se_Juega':[r'ScrabbleAR_Imagenes_png\ComoSeJuega1.png',r'ScrabbleAR_Imagenes_png\ComoSeJuega2.png',r'ScrabbleAR_Imagenes_png\ComoSeJuega3.png',r'ScrabbleAR_Imagenes_png\ComoSeJuega4.png'],
                      'Opciones':[r'ScrabbleAR_Imagenes_png\Opciones1.png',r'ScrabbleAR_Imagenes_png\Opciones2.png',r'ScrabbleAR_Imagenes_png\Opciones3.png',r'ScrabbleAR_Imagenes_png\Opciones4.png'],
                      'Tablero':[]}

    botones = [[sg.Button(button_text="Sobre el juego",size=(12,2),key="Sobre_El_Juego"),sg.Button(button_text="Como se juega",size=(12,2),key="Como_Se_Juega"),sg.Button(button_text="Opciones",size=(12,2),key="Opciones"),sg.Button(button_text="Tablero",size=(12,2),key="Botones_Tablero")]]

    Ventana=[     [sg.Text("Este es el menu de Ayuda , haz click en un boton para saber mas sobre el tema elegido")],
                  [sg.Frame('',botones,relief='raised')],
                  [sg.Image(r'ScrabbleAR_Imagenes_png\Instrucciones.png',key='Info')],
                  [sg.Button(button_text="Salir",size=(10,2),key="Salir"),sg.Button('<',disabled=True,pad=((320,5),(3,3))),sg.Button('>',disabled=True)] ]

    window = sg.Window('Ayuda',Ventana,location=(540,100),size=(500,650),finalize=True)
    while True:
        event,values=window.Read()
        playsound(r'ScrabbleAR_Sonidos\Click.mp3',block=False)
        if(event in (None,"Salir")):
            playsound(r'ScrabbleAR_Sonidos\Click.mp3')
            break

        elif (event != '>') and (event != '<'):
            Boton_actual = event
            pagina = 0
            if(event=="Sobre_El_Juego"):
                window["Info"].update(Dicc_Informacion["Sobre_El_Juego"][0])
                window['>'].update(disabled=True)
                window['<'].update(disabled=True)
            elif(event=="Como_Se_Juega"):
                window["Info"].update(Dicc_Informacion["Como_Se_Juega"][0])
                window['>'].update(disabled=False)
                window['<'].update(disabled=False)
            elif(event=="Opciones"):
                window["Info"].update(Dicc_Informacion["Opciones"][0])
                window['>'].update(disabled=False)
                window['<'].update(disabled=False)
            elif(event=="Tablero"):
                window["Info"].update(Dicc_Informacion["Botones_Tablero"][0])

        elif(event=='>'):
            pagina = pagina + 1
            window["Info"].update(Dicc_Informacion[Boton_actual][pagina])
        elif(event=='<'):
            pagina = pagina - 1
            window["Info"].update(Dicc_Informacion[Boton_actual][pagina])
        Comprobaciones(Boton_actual,pagina,window)
    window.close()
    return(event)

if __name__ == "__main__":
    sg.theme('DarkGrey2')
    identificador_carpeta_error(Ayuda)