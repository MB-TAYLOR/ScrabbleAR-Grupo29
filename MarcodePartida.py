import PySimpleGUI as sg
import csv

sg.ChangeLookAndFeel('BrownBlue') # change style
def generar_Pantalla():
    filename:str = None
    arch = open('Archivo_Opciones.csv','r')
    reader = csv.reader(arch)

    layout: list = [[sg.sg.Button(Pausar),sg.Button(Rendirse),sg.Button(Salir)]

    window: object = sg.Window('Top', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
    
    def modificar_dato(filename,puntaje):
      filas = 10
      fila = 1
      columna
      contenido = list()
      contenido = filename.readlines()
          for fila in filas:
              columnas = contenido[fila-1].split(';')
              columnas[4] = nuevo_dato
              contenido[fila-1] = ';'.join(columnas)+ '\n'
      with open(ruta, 'w') as filename:
          archivo.writelines(contenido)
    
    while True:
        event, values = window.read()
          if event in ('Pausar',None):
           layout = [[sg.Text('¿Reanudar?')],
                     [, sg.Stop()]]      
            window = sg.Window('Pausa', layout)
         if event in ('Rendirse',None):
           layout = [[sg.Text('¿Arrojas la toalla?')],
                     [sg.exit(), sg.Cancel()]]      
            window = sg.Window('Rendirse', layout)
        if event in ('Salir',None):
           layout = [[sg.Text('¿Guardar partida?')],         
                     [sg.Save(), sg.Cancel()]]      
            window = sg.Window('Salir', layout)    
        elif event == 'Total':
            filename = open('Puntajes_Total.txt','r+')
            modificar_dato(filename,puntaje)
            filename.close()
        elif event == 'Facil':
            filename = open('Puntajes_Facil.txt','r+')
            modificar_dato(filename,puntaje)
            filename.close()
        elif event == 'Medio':
            filename = open('Puntajes_Medio.txt','r+')
            modificar_dato(filename,puntaje)
            filename.close()
        elif event == 'Dificil':
            filename = open('Puntajes_Dificil.txt','r+')
            modificar_dato(filename,puntaje)
            filename.close()
    window.close()
    return(event)
#ProgramaPrincipal
if __name__ == "__main__":
    generar_Pantalla()