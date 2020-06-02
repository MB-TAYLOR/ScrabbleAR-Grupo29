import PySimpleGUI as sg
import csv

def Cargar(values,window):
    arch = open('Archivo_Opciones.csv','r')
    reader = csv.reader(arch)
    for row in reader:
        if (len(row) > 0):
            if (row[0] == values['Usuario']):
                values['Facil'] = row[1]
                values['Normal'] = row[2]
                values['Dificil'] = row[3]
                if (values['Facil'] == 'True'):
                    window['Facil'].update(values['Facil'])
                elif(values['Normal'] == 'True'):
                    window['Normal'].update(values['Normal'])
                else:
                    window['Dificil'].update(values['Dificil'])
                values['Lote1'] = row[4]
                window['Lote1'].update(values['Lote1'])
                values['Lote2'] = row[5]
                window['Lote2'].update(values['Lote2'])
                values['Lote3'] = row[6]
                window['Lote3'].update(values['Lote3'])
                values['Lote4'] = row[7]
                window['Lote4'].update(values['Lote4'])
                values['Lote5'] = row[8]
                window['Lote5'].update(values['Lote5'])
                values['Lote6'] = row[9]
                window['Lote6'].update(values['Lote6'])
                values['Lote7'] = row[10]
                window['Lote7'].update(values['Lote7'])
    arch.close()
    return values

def AgregarDatos(values):
    arch = open('Archivo_Opciones.csv','a')
    writer = csv.writer(arch)
    writer.writerow([values['Usuario'].strip(),values['Facil'],values['Normal'],values['Dificil'],values['Lote1'],values['Lote2'],values['Lote3'],values['Lote4'],values['Lote5'],values['Lote6'],values['Lote7']])
    arch.close()

def GuardarDatos(lista):
    arch = open('Archivo_Opciones.csv','w')
    writer = csv.writer(arch)
    writer.writerow(['Usuario','Facil','Normal','Dificil','Lote1','Lote2','Lote3','Lote4','Lote5','Lote6','Lote7'])
    for row in lista:
        writer.writerow([row['Usuario'].strip(),row['Facil'],row['Normal'],row['Dificil'],row['Lote1'],row['Lote2'],row['Lote3'],row['Lote4'],row['Lote5'],row['Lote6'],row['Lote7']])
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

def RestablecerPredeterminado(values,window):
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
    return values

def Layout():
    layout = [[sg.Text('Usuario:'),sg.Input(size=(15, 6),key='Usuario',default_text='Usuario1'),sg.OK('Cargar')],
            [sg.Text('Dificultad:',pad=(5,20)),
            sg.Radio('Facil','Dificultad',key='Facil'),
            sg.Radio('Normal','Dificultad', default='1',key='Normal'),
            sg.Radio('Dificil','Dificultad',key='Dificil')],
            [sg.Text('Cantidad de puntos por ficha:')],
            [sg.Text('A E O S I U N L R T:'),sg.Slider(range=(1,2),orientation="h",size=(6,10),pad=((5,3),(0,15)),default_value=1,key='Lote1')],
            [sg.Text('C D G :'),sg.Slider(range=(1,3),orientation="h",size=(6,10),pad=((82,3),(0,15)),default_value=2,key='Lote2')],
            [sg.Text('M B P:'),sg.Slider(range=(2,4),orientation="h",size=(6,10),pad=((85,3),(0,15)),default_value=3,key='Lote3')],
            [sg.Text('F H V Y:'),sg.Slider(range=(3,5),orientation="h",size=(6,10),pad=((75,3),(0,15)),default_value=4,key='Lote4')],
            [sg.Text('J:'),sg.Slider(range=(5,7),orientation="h",size=(6,10),pad=((116,3),(0,15)),default_value=6,key='Lote5')],
            [sg.Text('K LL Ñ Q RR W X:'),sg.Slider(range=(7,9),orientation="h",size=(6,10),pad=((18,3),(0,15)),default_value=8,key='Lote6')],
            [sg.Text('Z:'),sg.Slider(range=(9,11),orientation="h",size=(6,10),pad=((115,3),(0,15)),default_value=10,key='Lote7')],
            [sg.Save('Guardar'),sg.OK('Restablecer predeterminado'),sg.Exit('Salir')]]
    return layout

def Ventana_Opciones ():
    sg.theme('DarkAmber')
    window = sg.Window('Opciones', Layout())
    while True:
        event, values = window.read()

        if (event == 'Restablecer predeterminado'):
            values = RestablecerPredeterminado(values,window)

        elif (event == 'Guardar'):
            Lista = LeerDatos()
            existe = list(filter(lambda jug:values['Usuario'].strip() == jug['Usuario'],Lista))
            if existe != []: #Reemplazo la configuracion del usuario existente
                Lista.pop(Lista.index(existe[0]))
                Lista.append(values)
                GuardarDatos(Lista)
            else: #Simplemente lo agrego
                AgregarDatos(values)

        else:                   #Cargar
            values = Cargar(values,window)

        if event in (None, 'Salir'):
            break
    window.close()
    return values


#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    values = Ventana_Opciones()
