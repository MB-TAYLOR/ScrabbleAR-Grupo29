import PySimpleGUI as sg

def Ayuda():
    Dicc_Informacion={"Sobre_El_Juego":"ScrabbleAR es un juego basado en el popular juego Scrabble, en el que se intenta ganar puntos mediante la construcción de palabras sobre un tablero.En ScrabbleAR se juega contra la computadora y se re-definen algunas de las reglas del juego original. En particular, respecto a las palabras a construir,sólo se podrán utilizar palabras clasificadas como adjetivos, sustantivos y verbos,de acuerdo a cómo se configure el juego.",
    "Opciones":"En el menu de opciones podras guardar tu perfil con alguna de las 3 dificultades , podiendo modificar tanto la cantidad de fichas como el valor en puntos de estas, para luego,  en un futuro, cargar los valores guardados con aterioridad.",
    "Como_Se_Juega":"En esta version de SCRABBLE , ganaras la partida cuando , en el momento de su finalizacion(Se acabo el tiempo o se terminaron las fichas) tengas mas puntos que el CPU.\nPara ganar puntos debes formar palabras que , leidas de : derecha a izquierda/arriba a bajo , sean validas , las palabras solo se podran validar , si estan formadas horizontal o verticalmente\nPara saber si una palabra bien colocada es valida debes precionar el boton 'Validar'\nPara dejar en el tablero la palabra que formaste debes precionar el boton 'Terminar Turno' , si la palabra era valida , las fichas se quedaran en el tablero , ganaras puntos y tomaras de la bolsa la misma cantidad de fichas que usaste para formar la palabra , de lo contrario se te devolveran las fichas y tu turno terminara.",
    "Botones_Tablero":"Los botones en el tablero son :\nTerminar Turno :Verificara si las fichas colocadas en el tablero estan puestas de forma correcta y si la palabra formada es validad , luego terminara tu turno.\n\nValidar:Verificara si las fichas estan correctamente colocadas y si lo estan verificara si la palabra es valida.\nIntercambiar Fichas : Podras intercambiar 3 veces tus fichas por partida , al hacer click en el boton podras seleccionar las fichas del atril que deceas intercambiar , para confirmar vuelve a pulsar el boton Intercambiar Fichas.\n\nPausa:Pausa el juego.\n\nRendirse:Termina la partida y no guarda ningun dato de esta.\n\nSalir:Sales de la partida a la pantalla principal , la partida se guardara y podras reanudarla la proxima vez que inices una partida. "}

    #Diseño
    Ventana=[     [sg.Text("Explicacion del juego : ")],
                  [sg.Button(button_text="Sobre El Juego",size=(12,2),key="Sobre_El_Juego"),sg.Button(button_text="Opciones",size=(12,2),key="Opciones"),sg.Button(button_text="Como se juega",size=(12,2),key="Como_Se_Juega"),sg.Button(button_text="Botones en el Tablero",size=(12,2),key="Botones_Tablero")],
                  [sg.Text("Este es el menu de Ayuda , haz click en un boton para saber mas sobre el\ntema elegido\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ",key="Info",auto_size_text=True)],
                  [sg.Button(button_text="Salir",size=(10,2),key="Salir")]

                 ]


    #Aplico y muestro


    window = sg.Window('Ayuda',Ventana,location=(540,100),size=(500,650),finalize=True)
    while True:
        boton_cliqueado,datos_ingresados=window.Read()
        if(boton_cliqueado=="Sobre_El_Juego"):
            window["Info"].update(Dicc_Informacion["Sobre_El_Juego"])
        elif(boton_cliqueado=="Opciones"):
            window["Info"].update(Dicc_Informacion["Opciones"])
        elif(boton_cliqueado=="Como_Se_Juega"):
            window["Info"].update(Dicc_Informacion["Como_Se_Juega"])
        elif(boton_cliqueado=="Botones_Tablero"):
            window["Info"].update(Dicc_Informacion["Botones_Tablero"])
        elif(boton_cliqueado in (None,"Salir")):
            break
    window.close()
    return(boton_cliqueado)

if __name__ == "__main__":
    Ayuda()
