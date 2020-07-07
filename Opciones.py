import PySimpleGUI as sg
import csv

def Cargar(values,window,Dicc_Bolsa,letra_Seleccionada):
    arch = open('Archivo_Opciones.csv','r')
    reader = csv.reader(arch)
    for row in reader:
        if (len(row) > 0):
            if (row[1] == values['Usuario']):
                values['Facil'] = row[2]
                values['Normal'] = row[3]
                values['Dificil'] = row[4]
                if (values['Facil'] == 'True'):
                    window['Facil'].update(values['Facil'])
                elif(values['Normal'] == 'True'):
                    window['Normal'].update(values['Normal'])
                else:
                    window['Dificil'].update(values['Dificil'])
                values['Lote1'] = row[5]
                window['Lote1'].update(values['Lote1'])
                values['Lote2'] = row[6]
                window['Lote2'].update(values['Lote2'])
                values['Lote3'] = row[7]
                window['Lote3'].update(values['Lote3'])
                values['Lote4'] = row[8]
                window['Lote4'].update(values['Lote4'])
                values['Lote5'] = row[9]
                window['Lote5'].update(values['Lote5'])
                values['Lote6'] = row[10]
                window['Lote6'].update(values['Lote6'])
                values['Lote7'] = row[11]
                window['Lote7'].update(values['Lote7'])
                a = 12
                for key in Dicc_Bolsa.keys():
                    Dicc_Bolsa[key] = int(row[a])
                    a = a + 1
                window['Cantidad'].update(Dicc_Bolsa[letra_Seleccionada])
    arch.close()
    return values

def AgregarDatos(values):
    arch = open('Archivo_Opciones.csv','a')
    writer = csv.writer(arch)
    writer.writerow([True,values['Usuario'].strip(),values['Facil'],values['Normal'],values['Dificil'],int(values['Lote1']),int(values['Lote2']),int(values['Lote3']),int(values['Lote4']),int(values['Lote5']),int(values['Lote6']),int(values['Lote7']),values['A'],values['B'],values['C'],values['D'],values['E'],values['F'],values['G'],values['H'],values['I'],values['J'],values['K'],values['L'],values['M'],values['N'],values['Enie'],values['O'],values['P'],values['Q'],values['R'],values['R'],values['S'],values['T'],values['U'],values['V'],values['W'],values['X'],values['Y'],values['Z']])
    arch.close()

def GuardarDatos(lista):
    arch = open('Archivo_Opciones.csv','w')
    writer = csv.writer(arch)
    writer.writerow(['Actual','Usuario','Facil','Normal','Dificil','Lote1','Lote2','Lote3','Lote4','Lote5','Lote6','Lote7','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    print(lista)
    for row in lista:
        writer.writerow([row['Actual'],row['Usuario'].strip(),row['Facil'],row['Normal'],row['Dificil'],int(row['Lote1']),int(row['Lote2']),int(row['Lote3']),int(row['Lote4']),int(row['Lote5']),int(row['Lote6']),int(row['Lote7']),row['A'],row['B'],row['C'],row['D'],row['E'],row['F'],row['G'],row['H'],row['I'],row['J'],row['K'],row['L'],row['M'],row['N'],row['Enie'],row['O'],row['P'],row['Q'],row['R'],row['R'],row['S'],row['T'],row['U'],row['V'],row['W'],row['X'],row['Y'],row['Z']])
    arch.close()

def LeerDatos():
    arch = open('Archivo_Opciones.csv','r')
    reader = csv.reader(arch)
    datos = []
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index == 0):
                claves = row
                index = index + 1
            else:
                dicc = {}
                [dicc.setdefault(claves[i],row[i]) for i in range(len(claves))]
                datos.append(dicc.copy())
    arch.close()
    return datos

def RestablecerPredeterminado(values,window,Dicc_Bolsa,letra_Seleccionada):
    values['Facil'] = False
    window['Facil'].update(values['Facil'])
    values['Normal'] = True
    window['Normal'].update(values['Normal'])
    values['Dificil'] = False
    window['Dificil'].update(values['Dificil'])
    values['Lote1'] = 1
    window['Lote1'].update(values['Lote1'])
    values['Lote2'] = 2
    window['Lote2'].update(values['Lote2'])
    values['Lote3'] = 3
    window['Lote3'].update(values['Lote3'])
    values['Lote4'] = 4
    window['Lote4'].update(values['Lote4'])
    values['Lote5'] = 6
    window['Lote5'].update(values['Lote5'])
    values['Lote6'] = 8
    window['Lote6'].update(values['Lote6'])
    values['Lote7'] = 10
    window['Lote7'].update(values['Lote7'])
    Dicc_Bolsa={"A":11,"B":3,"C":4,"D":4,"E":11,"F":2,"G":2,"H":2,"I":6,"J":2,"K":1,"L":4,"M":3,"N":5,
                      "Enie":1,"O":8,"P":2,"Q":1,"R":4,"S":7,"T":4,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1}

    window['Cantidad'].update(Dicc_Bolsa[letra_Seleccionada])
    return values

def Layout_Columna():
    layout = [[sg.Text('Cantidad de fichas por letra:',pad=(50,92))],
              [sg.Text('LETRAS',key='Texto_Letra'),sg.Slider(range=(0,26),orientation="v",pad=((5,3),(5,0)),size=(6,10),disable_number_display=True,enable_events=True,key='Letras'),sg.Text('A',key='Letra_Pantalla',font=('Default',80),pad=(20,3))],
              [sg.Slider(range=(1,15),orientation="h",pad=((90,3),(0,3)),key='Cantidad',enable_events=True,size=(12,10))],
              [sg.Text('CANTIDAD',key='Texto_Cantidad',pad=((110,3),(5,3)))]]
    return layout

def Layout_Main():
    layout = [[sg.Text('Usuario:'),sg.Input(size=(15, 6),key='Usuario',default_text='Default'),sg.OK('Cargar perfil',key='Cargar')],
            [sg.Text('Dificultad:',pad=(5,20)),
            sg.Radio('Facil','Dificultad',key='Facil',tooltip='En "Facil" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Adjetivos, Sustantivos y Verbos\nTiempo por ronda: 60sg \nTiempo Total: 60Min'),
            sg.Radio('Normal','Dificultad', default='1',key='Normal',tooltip='En "Normal" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Sustantivos y Verbos\nTiempo por ronda: 45sg \nTiempo Total: 45Min'),
            sg.Radio('Dificil','Dificultad',key='Dificil',tooltip='En "Dificil" se aplicaran los siguientes cambios:\n_____________\nSe aceptaran: Adjetivos,Sustantivos y Verbos(De forma Aleatoria)\nTiempo por ronda: 30sg \nTiempo Total: 30Min')],
            [sg.Text('Cantidad de puntos por ficha:')],
            [sg.Text('A E O S I U N L R T:'),sg.Slider(range=(1,2),orientation="h",size=(6,10),pad=((5,3),(0,15)),default_value=1,key='Lote1')],
            [sg.Text('C D G :'),sg.Slider(range=(1,3),orientation="h",size=(6,10),pad=((82,3),(0,15)),default_value=2,key='Lote2')],
            [sg.Text('M B P:'),sg.Slider(range=(2,4),orientation="h",size=(6,10),pad=((85,3),(0,15)),default_value=3,key='Lote3')],
            [sg.Text('F H V Y:'),sg.Slider(range=(3,5),orientation="h",size=(6,10),pad=((75,3),(0,15)),default_value=4,key='Lote4')],
            [sg.Text('J:'),sg.Slider(range=(5,7),orientation="h",size=(6,10),pad=((116,3),(0,15)),default_value=6,key='Lote5')],
            [sg.Text('K Ñ Q W X:'),sg.Slider(range=(7,9),orientation="h",size=(6,10),pad=((58,3),(0,15)),default_value=8,key='Lote6')],
            [sg.Text('Z:'),sg.Slider(range=(9,11),orientation="h",size=(6,10),pad=((115,3),(0,15)),default_value=10,key='Lote7')],
            [sg.Save('Guardar'),sg.OK('Restablecer predeterminado'),sg.Exit('Salir')]]
    return layout

def Poner_Todos_En_Falso(lista):
    arch = open('Archivo_Opciones.csv','w')
    writer = csv.writer(arch)
    writer.writerow(['Actual','Usuario','Facil','Normal','Dificil','Lote1','Lote2','Lote3','Lote4','Lote5','Lote6','Lote7','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    i = 0
    for row in lista:
        lista[i]['Actual'] = False
        writer.writerow([False,row['Usuario'].strip(),row['Facil'],row['Normal'],row['Dificil'],int(row['Lote1']),int(row['Lote2']),int(row['Lote3']),int(row['Lote4']),int(row['Lote5']),int(row['Lote6']),int(row['Lote7']),row['A'],row['B'],row['C'],row['D'],row['E'],row['F'],row['G'],row['H'],row['I'],row['J'],row['K'],row['L'],row['M'],row['N'],row['Enie'],row['O'],row['P'],row['Q'],row['R'],row['R'],row['S'],row['T'],row['U'],row['V'],row['W'],row['X'],row['Y'],row['Z']])
        i = i + 1
    arch.close()

def Importar_Datos():
    arch = open('Archivo_Opciones.csv','r')
    reader = csv.reader(arch)
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index != 0):
                if (row[0] == 'True'):
                    arch.close()
                    return row
            else:
                index = index + 1

def Transformar_Values(values,Dicc_Bolsa):
    values.pop('Letras')
    values.pop('Cantidad')
    for key,elem in Dicc_Bolsa.items():
        values[key] = elem


def Ventana_Opciones ():
    Lista_Letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Enie','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Diseño = [ [sg.Column((Layout_Main())),
                sg.Column(Layout_Columna())] ]
    window = sg.Window('Opciones', Diseño)
    window.Read(timeout=1)[1]
    #values = Cargar(Importar_Datos(),window)
    #Dicc_Bolsa={"A":values['A'],"B":values['B'],"C":values['C'],"D":values['D'],"E":values['E'],"F":values['F'],"G":values['G'],"H":values['H'],"I":values['I'],"J":values['J'],"K":values['K'],"L":values['L'],"M":values['M'],"N":values['N'],
    #                  "Ñ":values['Ñ'],"O":values['O'],"P":values['P'],"Q":values['Q'],"R":values['R'],"S":values['S'],"T":values['T'],"U":values['U'],"V":values['V'],"W":values['W'],"X":values['X'],"Y":values['Y'],"Z":values['Z']}
    #Values Seria un dicc con todos los elementos, onda A B C con sus cantidad.
    Dicc_Bolsa={"A":11,"B":3,"C":4,"D":4,"E":11,"F":2,"G":2,"H":2,"I":6,"J":2,"K":1,"L":4,"M":3,"N":5,
                      "Enie":1,"O":8,"P":2,"Q":1,"R":4,"S":7,"T":4,"U":6,"V":2,"W":1,"X":1,"Y":1,"Z":1}
    letra_Seleccionada = 'A'
    Cant_Letra_Actual = Dicc_Bolsa['A']
    window['Cantidad'].update(Dicc_Bolsa['A'])
    while True:
        event, values = window.read()
        #A partir de aca values es un dicc sin las A B C, etc

        if event in (None, 'Salir'):
            break

        if event == 'Letras':
            window['Cantidad'].update(Dicc_Bolsa[Lista_Letras[int(values['Letras'])]])
            if Lista_Letras[int(values['Letras'])] != 'Enie':
                window['Letra_Pantalla'].update(Lista_Letras[int(values['Letras'])])
            else:
                window['Letra_Pantalla'].update('Ñ')
            letra_Seleccionada = Lista_Letras[int(values['Letras'])]

        if event == 'Cantidad':
            Cant_Letra_Actual = values['Cantidad']
            Dicc_Bolsa[letra_Seleccionada] = int(Cant_Letra_Actual)

        if (event == 'Restablecer predeterminado'):
            values = RestablecerPredeterminado(values,window,Dicc_Bolsa,letra_Seleccionada)

        elif (event == 'Guardar') or (event == 'Cargar'):
            Lista = LeerDatos()
            Transformar_Values(values,Dicc_Bolsa)
            existe = list(filter(lambda jug:values['Usuario'].strip() == jug['Usuario'],Lista))
            if (event == 'Guardar'):
                if values['Usuario'] != '':
                    if existe != []: #Reemplazo la configuracion del usuario existente
                        Lista.pop(Lista.index(existe[0]))
                        Lista.append(values)
                        GuardarDatos(Lista)
                        sg.popup('El perfil se modifico exitosamente!',title='Aviso',keep_on_top=True)
                    else: #Simplemente lo agrego
                        #print('Lista:',Lista)
                        #print('Values:',values)
                        Poner_Todos_En_Falso(Lista)
                        AgregarDatos(values)
                        sg.popup('El perfil se guardo exitosamente!',title='Aviso',keep_on_top=True)
                else:
                    sg.popup('No puedes guardar un usuario vacio!',title='Aviso',keep_on_top=True)
            else:           #Cargar
                if existe != []:
                    Lista.pop(Lista.index(existe[0]))
                    existe[0]['Actual'] = True
                    Poner_Todos_En_Falso(Lista)
                    Lista.append(existe[0])
                    GuardarDatos(Lista)
                    values = Cargar(values,window,Dicc_Bolsa,letra_Seleccionada)
                else:
                    sg.popup('No se encontro ningun usuario con ese nombre',title='Aviso',keep_on_top=True)

    window.close()
    return event


#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    values = Ventana_Opciones()
