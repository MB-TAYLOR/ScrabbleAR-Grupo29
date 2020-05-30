import PySimpleGUI as sg 
sg.ChangeLookAndFeel('BrownBlue') # change style

WIN_W: int = 90
WIN_H: int = 25
filename:str = None

# string variables to shorten loop and menu code
file_open: str = 'Open..........(CTRL+O)'

menu_layout: list = [[sg.Button('Total'), [file_open_Total]],
                     [sg.Button('Facil'),[file_open_Facil]],
                     [sg.Button('Medio'),[file_open_Medio]],
                     [sg.Button('Dificil'),[file_open_Dificil]]]
            
layout: list = [[sg.Menu(menu_layout)],
                [sg.Text('> New file <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
                [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')],
                [sg.Button('Salir')]]

window: object = sg.Window('Tabla de Posiciones', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)


def open_file(filename) -> str:
    ''' Open file and update the infobar '''
    try:
        filename: str = sg.popup_get_file(no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

while True:
    event, values = window.read()

    if event in (None, 'Salir'):
        break
    if event in (file_open_Total, 'o:79'):
        filename = open_file(Puntajes_Total.txt)
    if event in (file_open_Facil, 'o:79'):
        filename = open_file(Puntajes_Facil.txt)
    if event in (file_open, 'o:79'):
        filename = open_file_Medio(Puntajes_Medio.txt)
    if event in (file_open_Dificil, 'o:79'):
        filename = open_file(Puntajes_Dificil.txt)
