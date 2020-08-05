import string
import random
import sys
import traceback
import tkinter
import PySimpleGUI as sg
import platform
import os

def corrector_paths(path):
    sistema_Operativo=platform.system()
    path_base=os.getcwd()
    path_add=path.split(chr(92))
    path=os.path.join(path_base,*path_add)
    return(path)


def identificador_carpeta_error(ProgramaPrincipal):
    event=""
    try:
        event=ProgramaPrincipal()
    except FileNotFoundError:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[2]
        ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
        ruta_carpeta=ruta_archivo_error[:ruta_archivo_error.find(chr(92))]
        sg.popup_error("Error al intentar acceder al archivo de la siguiente ruta :",ruta_archivo_error,"\nRevise que el archivo se encuentre en la carpeta",ruta_carpeta,title='Error')
    except tkinter.TclError:
        Direciones_error={"inicio":r'ScrabbleAR_Imagenes_png\icono_inicio.png',"yellow":r'ScrabbleAR_Imagenes_png\icono3.png',"red":r'ScrabbleAR_Imagenes_png\icono_x2.png',
        "green":r'ScrabbleAR_Imagenes_png\icono_-3.png',"blue":r'ScrabbleAR_Imagenes_png\icono_-2.png',"white":r'ScrabbleAR_Imagenes_png\modelo_ficha.png'}
        tb = sys.exc_info()[2]
        if("window[coord].update" in traceback.format_tb(tb)[2]):
            tbinfo = traceback.format_tb(tb)[2]
            ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
            ruta_archivo_error=ruta_archivo_error[:ruta_archivo_error.find(",")]
            ruta_archivo_error=ruta_archivo_error[ruta_archivo_error.find("=")+1:]
            ruta_carpeta=Direciones_error[ruta_archivo_error]
            ruta_carpeta=ruta_carpeta[:ruta_carpeta.find(chr(92))]
            sg.popup_error("Error al intentar acceder a la imagen de la siguiente ruta :",Direciones_error[ruta_archivo_error] ,"\nRevise que la imagen se encuentre el la carpeta: ",ruta_carpeta ,title='Error')
        else:
            sg.popup_error("Falta alguna imagen en la carpeta ScrabbleAR_Imagenes_png",title='Error')
    except UnicodeDecodeError:
        tb = sys.exc_info()[2]
        if "playsound" in traceback.format_tb(tb)[2]:
            tbinfo = traceback.format_tb(tb)[2]
            ruta_archivo_error=tbinfo[tbinfo.find("(")+1:tbinfo.find(")")].strip(",'r'")
            ruta_archivo_error=ruta_archivo_error[:ruta_archivo_error.find("'")]
            ruta_carpeta=ruta_archivo_error[:ruta_archivo_error.find(chr(92))]
            sg.popup_error("Error al intentar acceder al archivo de audio de la siguiente ruta :",ruta_archivo_error,"\nRevise que el archivo de audio se encuentre el la carpeta: ",ruta_carpeta ,title='Error')
        else:
            sg.popup_error("Falta un archivo de audio , revise la carpeta ScrabbleAR_Sonidos ",title='Error')
    #except:
    #    sg.popup_error("Ah ocurrido un error desconocido",title='Error')
    return(event)



def Selector_de_coordenadas_disponibles(conjunto):
    x=random.randint(0,(len(conjunto)-1))
    conjunto=list(conjunto)
    return(tuple(conjunto[x]))
