import PySimpleGUI as sg
sg.ChangeLookAndFeel('BrownBlue') # change style
def genero_Top():
    filename:str = None
# string variables to shorten loop and menu code
    menu_layout: list = ['Total','Facil','Medio','Dificil','Salir']

    layout: list = [[sg.Button(menu_layout[0]),sg.Button(menu_layout[1]),sg.Button(menu_layout[2]),sg.Button(menu_layout[3]),sg.Button(menu_layout[4])],
                    [sg.Text('', font=('Consolas', 10), size=(90, 1), key='_INFO_')],
                    [sg.Text(font=('Consolas', 12), size=(90, 25), key='_BODY_')]]

    window: object = sg.Window('Top', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
    Tabla=window.FindElement('_BODY_')
    while True:
        event, values = window.read()
        if event in ('Salir',None):
            break
        elif event == 'Total':
            filename = open('Puntajes_Total.txt','r')
            Tabla.Update(filename.read())
            filename.close()
        elif event == 'Facil':
            filename = open('Puntajes_Facil.txt','r')
            Tabla.Update(filename.read())
            filename.close()
        elif event == 'Medio':
            filename = open('Puntajes_Medio.txt','r')
            Tabla.Update(filename.read())
            filename.close()
        elif event == 'Dificil':
            filename = open('Puntajes_Dificil.txt','r')
            Tabla.Update(filename.read())
            filename.close()
    window.close()
    return(event)
#ProgramaPrincipal-------------
if __name__ == "__main__":
    genero_Top()
