from palabra_Existe import verificar_Palabra
import json
from Generadores import Selector_de_coordenadas_disponibles
from AiMaquina import formar_palabra
from threading import Thread
import PySimpleGUI as sg
from random import randint
import random
import time
import csv


MAX_ROWS = MAX_COL = 15
temp = 5
Infobox_Activa = False
HistorialUsuario = []
HistorialCPU = []
PrimerRonda = True

def rutas_letras(Dicc_letra_puntajes):
    Dicc_letras_rutas={'A1':[r'ScrabbleAR_Imagenes_png\ficha_A1_B.png',r'ScrabbleAR_Imagenes_png\ficha_A1_S.png',r'ScrabbleAR_Imagenes_png\ficha_A1_T.png'],
                       'A2':[r'ScrabbleAR_Imagenes_png\ficha_A2_B.png',r'ScrabbleAR_Imagenes_png\ficha_A2_S.png',r'ScrabbleAR_Imagenes_png\ficha_A2_T.png'],
                       'B2':[r'ScrabbleAR_Imagenes_png\ficha_B2_B.png',r'ScrabbleAR_Imagenes_png\ficha_B2_S.png',r'ScrabbleAR_Imagenes_png\ficha_B2_T.png'],
                       'B3':[r'ScrabbleAR_Imagenes_png\ficha_B3_B.png',r'ScrabbleAR_Imagenes_png\ficha_B3_S.png',r'ScrabbleAR_Imagenes_png\ficha_B3_T.png'],
                       'B4':[r'ScrabbleAR_Imagenes_png\ficha_B4_B.png',r'ScrabbleAR_Imagenes_png\ficha_B4_S.png',r'ScrabbleAR_Imagenes_png\ficha_B4_T.png'],
                       'C1':[r'ScrabbleAR_Imagenes_png\ficha_C1_B.png',r'ScrabbleAR_Imagenes_png\ficha_C1_S.png',r'ScrabbleAR_Imagenes_png\ficha_C1_T.png'],
                       'C2':[r'ScrabbleAR_Imagenes_png\ficha_C2_B.png',r'ScrabbleAR_Imagenes_png\ficha_C2_S.png',r'ScrabbleAR_Imagenes_png\ficha_C2_T.png'],
                       'C3':[r'ScrabbleAR_Imagenes_png\ficha_C3_B.png',r'ScrabbleAR_Imagenes_png\ficha_C3_S.png',r'ScrabbleAR_Imagenes_png\ficha_C3_T.png'],
                       'D1':[r'ScrabbleAR_Imagenes_png\ficha_D1_B.png',r'ScrabbleAR_Imagenes_png\ficha_D1_S.png',r'ScrabbleAR_Imagenes_png\ficha_D1_T.png'],
                       'D2':[r'ScrabbleAR_Imagenes_png\ficha_D2_B.png',r'ScrabbleAR_Imagenes_png\ficha_D2_S.png',r'ScrabbleAR_Imagenes_png\ficha_D2_T.png'],
                       'D3':[r'ScrabbleAR_Imagenes_png\ficha_D3_B.png',r'ScrabbleAR_Imagenes_png\ficha_D3_S.png',r'ScrabbleAR_Imagenes_png\ficha_D3_T.png'],
                       'E1':[r'ScrabbleAR_Imagenes_png\ficha_E1_B.png',r'ScrabbleAR_Imagenes_png\ficha_E1_S.png',r'ScrabbleAR_Imagenes_png\ficha_E1_T.png'],
                       'E2':[r'ScrabbleAR_Imagenes_png\ficha_E2_B.png',r'ScrabbleAR_Imagenes_png\ficha_E2_S.png',r'ScrabbleAR_Imagenes_png\ficha_E2_T.png'],
                       'F3':[r'ScrabbleAR_Imagenes_png\ficha_F3_B.png',r'ScrabbleAR_Imagenes_png\ficha_F3_S.png',r'ScrabbleAR_Imagenes_png\ficha_F3_T.png'],
                       'F4':[r'ScrabbleAR_Imagenes_png\ficha_F4_B.png',r'ScrabbleAR_Imagenes_png\ficha_F4_S.png',r'ScrabbleAR_Imagenes_png\ficha_F4_T.png'],
                       'F5':[r'ScrabbleAR_Imagenes_png\ficha_F5_B.png',r'ScrabbleAR_Imagenes_png\ficha_F5_S.png',r'ScrabbleAR_Imagenes_png\ficha_F5_T.png'],
                       'G1':[r'ScrabbleAR_Imagenes_png\ficha_G1_B.png',r'ScrabbleAR_Imagenes_png\ficha_G1_S.png',r'ScrabbleAR_Imagenes_png\ficha_G1_T.png'],
                       'G2':[r'ScrabbleAR_Imagenes_png\ficha_G2_B.png',r'ScrabbleAR_Imagenes_png\ficha_G2_S.png',r'ScrabbleAR_Imagenes_png\ficha_G2_T.png'],
                       'G3':[r'ScrabbleAR_Imagenes_png\ficha_G3_B.png',r'ScrabbleAR_Imagenes_png\ficha_G3_S.png',r'ScrabbleAR_Imagenes_png\ficha_G3_T.png'],
                       'H3':[r'ScrabbleAR_Imagenes_png\ficha_H3_B.png',r'ScrabbleAR_Imagenes_png\ficha_H3_S.png',r'ScrabbleAR_Imagenes_png\ficha_H3_T.png'],
                       'H4':[r'ScrabbleAR_Imagenes_png\ficha_H4_B.png',r'ScrabbleAR_Imagenes_png\ficha_H4_S.png',r'ScrabbleAR_Imagenes_png\ficha_H4_T.png'],
                       'H5':[r'ScrabbleAR_Imagenes_png\ficha_H5_B.png',r'ScrabbleAR_Imagenes_png\ficha_H5_S.png',r'ScrabbleAR_Imagenes_png\ficha_H5_T.png'],
                       'I1':[r'ScrabbleAR_Imagenes_png\ficha_I1_B.png',r'ScrabbleAR_Imagenes_png\ficha_I1_S.png',r'ScrabbleAR_Imagenes_png\ficha_I1_T.png'],
                       'I2':[r'ScrabbleAR_Imagenes_png\ficha_I2_B.png',r'ScrabbleAR_Imagenes_png\ficha_I2_S.png',r'ScrabbleAR_Imagenes_png\ficha_I2_T.png'],
                       'J5':[r'ScrabbleAR_Imagenes_png\ficha_J5_B.png',r'ScrabbleAR_Imagenes_png\ficha_J5_S.png',r'ScrabbleAR_Imagenes_png\ficha_J5_T.png'],
                       'J6':[r'ScrabbleAR_Imagenes_png\ficha_J6_B.png',r'ScrabbleAR_Imagenes_png\ficha_J6_S.png',r'ScrabbleAR_Imagenes_png\ficha_J6_T.png'],
                       'J7':[r'ScrabbleAR_Imagenes_png\ficha_J7_B.png',r'ScrabbleAR_Imagenes_png\ficha_J7_S.png',r'ScrabbleAR_Imagenes_png\ficha_J7_T.png'],
                       'K7':[r'ScrabbleAR_Imagenes_png\ficha_K7_B.png',r'ScrabbleAR_Imagenes_png\ficha_K7_S.png',r'ScrabbleAR_Imagenes_png\ficha_K7_T.png'],
                       'K8':[r'ScrabbleAR_Imagenes_png\ficha_K8_B.png',r'ScrabbleAR_Imagenes_png\ficha_K8_S.png',r'ScrabbleAR_Imagenes_png\ficha_K8_T.png'],
                       'K9':[r'ScrabbleAR_Imagenes_png\ficha_K9_B.png',r'ScrabbleAR_Imagenes_png\ficha_K9_S.png',r'ScrabbleAR_Imagenes_png\ficha_K9_T.png'],
                       'L1':[r'ScrabbleAR_Imagenes_png\ficha_L1_B.png',r'ScrabbleAR_Imagenes_png\ficha_L1_S.png',r'ScrabbleAR_Imagenes_png\ficha_L1_T.png'],
                       'L2':[r'ScrabbleAR_Imagenes_png\ficha_L2_B.png',r'ScrabbleAR_Imagenes_png\ficha_L2_S.png',r'ScrabbleAR_Imagenes_png\ficha_L2_T.png'],
                       'M2':[r'ScrabbleAR_Imagenes_png\ficha_M2_B.png',r'ScrabbleAR_Imagenes_png\ficha_M2_S.png',r'ScrabbleAR_Imagenes_png\ficha_M2_T.png'],
                       'M3':[r'ScrabbleAR_Imagenes_png\ficha_M3_B.png',r'ScrabbleAR_Imagenes_png\ficha_M3_S.png',r'ScrabbleAR_Imagenes_png\ficha_M3_T.png'],
                       'M4':[r'ScrabbleAR_Imagenes_png\ficha_M4_B.png',r'ScrabbleAR_Imagenes_png\ficha_M4_S.png',r'ScrabbleAR_Imagenes_png\ficha_M4_T.png'],
                       'N1':[r'ScrabbleAR_Imagenes_png\ficha_N1_B.png',r'ScrabbleAR_Imagenes_png\ficha_N1_S.png',r'ScrabbleAR_Imagenes_png\ficha_N1_T.png'],
                       'N2':[r'ScrabbleAR_Imagenes_png\ficha_N2_B.png',r'ScrabbleAR_Imagenes_png\ficha_N2_S.png',r'ScrabbleAR_Imagenes_png\ficha_N2_T.png'],
                       'Ñ7':[r'ScrabbleAR_Imagenes_png\ficha_Ñ7_B.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ7_S.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ7_T.png'],
                       'Ñ8':[r'ScrabbleAR_Imagenes_png\ficha_Ñ8_B.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ8_S.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ8_T.png'],
                       'Ñ9':[r'ScrabbleAR_Imagenes_png\ficha_Ñ9_B.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ9_S.png',r'ScrabbleAR_Imagenes_png\ficha_Ñ9_T.png'],
                       'O1':[r'ScrabbleAR_Imagenes_png\ficha_O1_B.png',r'ScrabbleAR_Imagenes_png\ficha_O1_S.png',r'ScrabbleAR_Imagenes_png\ficha_O1_T.png'],
                       'O2':[r'ScrabbleAR_Imagenes_png\ficha_O2_B.png',r'ScrabbleAR_Imagenes_png\ficha_O2_S.png',r'ScrabbleAR_Imagenes_png\ficha_O2_T.png'],
                       'P2':[r'ScrabbleAR_Imagenes_png\ficha_P2_B.png',r'ScrabbleAR_Imagenes_png\ficha_P2_S.png',r'ScrabbleAR_Imagenes_png\ficha_P2_T.png'],
                       'P3':[r'ScrabbleAR_Imagenes_png\ficha_P3_B.png',r'ScrabbleAR_Imagenes_png\ficha_P3_S.png',r'ScrabbleAR_Imagenes_png\ficha_P3_T.png'],
                       'P4':[r'ScrabbleAR_Imagenes_png\ficha_P4_B.png',r'ScrabbleAR_Imagenes_png\ficha_P4_S.png',r'ScrabbleAR_Imagenes_png\ficha_P4_T.png'],
                       'Q7':[r'ScrabbleAR_Imagenes_png\ficha_Q7_B.png',r'ScrabbleAR_Imagenes_png\ficha_Q7_S.png',r'ScrabbleAR_Imagenes_png\ficha_Q7_T.png'],
                       'Q8':[r'ScrabbleAR_Imagenes_png\ficha_Q8_B.png',r'ScrabbleAR_Imagenes_png\ficha_Q8_S.png',r'ScrabbleAR_Imagenes_png\ficha_Q8_T.png'],
                       'Q9':[r'ScrabbleAR_Imagenes_png\ficha_Q9_B.png',r'ScrabbleAR_Imagenes_png\ficha_Q9_S.png',r'ScrabbleAR_Imagenes_png\ficha_Q9_T.png'],
                       'R1':[r'ScrabbleAR_Imagenes_png\ficha_R1_B.png',r'ScrabbleAR_Imagenes_png\ficha_R1_S.png',r'ScrabbleAR_Imagenes_png\ficha_R1_T.png'],
                       'R2':[r'ScrabbleAR_Imagenes_png\ficha_R2_B.png',r'ScrabbleAR_Imagenes_png\ficha_R2_S.png',r'ScrabbleAR_Imagenes_png\ficha_R2_T.png'],
                       'S1':[r'ScrabbleAR_Imagenes_png\ficha_S1_B.png',r'ScrabbleAR_Imagenes_png\ficha_S1_S.png',r'ScrabbleAR_Imagenes_png\ficha_S1_T.png'],
                       'S2':[r'ScrabbleAR_Imagenes_png\ficha_S2_B.png',r'ScrabbleAR_Imagenes_png\ficha_S2_S.png',r'ScrabbleAR_Imagenes_png\ficha_S2_T.png'],
                       'T1':[r'ScrabbleAR_Imagenes_png\ficha_T1_B.png',r'ScrabbleAR_Imagenes_png\ficha_T1_S.png',r'ScrabbleAR_Imagenes_png\ficha_T1_T.png'],
                       'T2':[r'ScrabbleAR_Imagenes_png\ficha_T2_B.png',r'ScrabbleAR_Imagenes_png\ficha_T2_S.png',r'ScrabbleAR_Imagenes_png\ficha_T2_T.png'],
                       'U1':[r'ScrabbleAR_Imagenes_png\ficha_U1_B.png',r'ScrabbleAR_Imagenes_png\ficha_U1_S.png',r'ScrabbleAR_Imagenes_png\ficha_U1_T.png'],
                       'U2':[r'ScrabbleAR_Imagenes_png\ficha_U2_B.png',r'ScrabbleAR_Imagenes_png\ficha_U2_S.png',r'ScrabbleAR_Imagenes_png\ficha_U2_T.png'],
                       'V3':[r'ScrabbleAR_Imagenes_png\ficha_V3_B.png',r'ScrabbleAR_Imagenes_png\ficha_V3_S.png',r'ScrabbleAR_Imagenes_png\ficha_V3_T.png'],
                       'V4':[r'ScrabbleAR_Imagenes_png\ficha_V4_B.png',r'ScrabbleAR_Imagenes_png\ficha_V4_S.png',r'ScrabbleAR_Imagenes_png\ficha_V4_T.png'],
                       'V5':[r'ScrabbleAR_Imagenes_png\ficha_V5_B.png',r'ScrabbleAR_Imagenes_png\ficha_V5_S.png',r'ScrabbleAR_Imagenes_png\ficha_V5_T.png'],
                       'W7':[r'ScrabbleAR_Imagenes_png\ficha_W7_B.png',r'ScrabbleAR_Imagenes_png\ficha_W7_S.png',r'ScrabbleAR_Imagenes_png\ficha_W7_T.png'],
                       'W8':[r'ScrabbleAR_Imagenes_png\ficha_W8_B.png',r'ScrabbleAR_Imagenes_png\ficha_W8_S.png',r'ScrabbleAR_Imagenes_png\ficha_W8_T.png'],
                       'W9':[r'ScrabbleAR_Imagenes_png\ficha_W9_B.png',r'ScrabbleAR_Imagenes_png\ficha_W9_S.png',r'ScrabbleAR_Imagenes_png\ficha_W9_T.png'],
                       'X7':[r'ScrabbleAR_Imagenes_png\ficha_X7_B.png',r'ScrabbleAR_Imagenes_png\ficha_X7_S.png',r'ScrabbleAR_Imagenes_png\ficha_X7_T.png'],
                       'X8':[r'ScrabbleAR_Imagenes_png\ficha_X8_B.png',r'ScrabbleAR_Imagenes_png\ficha_X8_S.png',r'ScrabbleAR_Imagenes_png\ficha_X8_T.png'],
                       'X9':[r'ScrabbleAR_Imagenes_png\ficha_X9_B.png',r'ScrabbleAR_Imagenes_png\ficha_X9_S.png',r'ScrabbleAR_Imagenes_png\ficha_X9_T.png'],
                       'Y3':[r'ScrabbleAR_Imagenes_png\ficha_Y3_B.png',r'ScrabbleAR_Imagenes_png\ficha_Y3_S.png',r'ScrabbleAR_Imagenes_png\ficha_Y3_T.png'],
                       'Y4':[r'ScrabbleAR_Imagenes_png\ficha_Y4_B.png',r'ScrabbleAR_Imagenes_png\ficha_Y4_S.png',r'ScrabbleAR_Imagenes_png\ficha_Y4_T.png'],
                       'Y5':[r'ScrabbleAR_Imagenes_png\ficha_Y5_B.png',r'ScrabbleAR_Imagenes_png\ficha_Y5_S.png',r'ScrabbleAR_Imagenes_png\ficha_Y5_T.png'],
                       'Z9':[r'ScrabbleAR_Imagenes_png\ficha_Z9_B.png',r'ScrabbleAR_Imagenes_png\ficha_Z9_S.png',r'ScrabbleAR_Imagenes_png\ficha_Z9_T.png'],
                       'Z10':[r'ScrabbleAR_Imagenes_png\ficha_Z10_B.png',r'ScrabbleAR_Imagenes_png\ficha_Z10_S.png',r'ScrabbleAR_Imagenes_png\ficha_Z10_T.png'],
                       'Z11':[r'ScrabbleAR_Imagenes_png\ficha_Z11_B.png',r'ScrabbleAR_Imagenes_png\ficha_Z11_S.png',r'ScrabbleAR_Imagenes_png\ficha_Z11_T.png']}

    Dicc_Actual_Punto_Ficha={}
    for x in Dicc_letra_puntajes:
        clave_Dicc_letras_rutas=x+str(Dicc_letra_puntajes[x])
        Dicc_Actual_Punto_Ficha[x]=Dicc_letras_rutas[clave_Dicc_letras_rutas]
    Dicc_Actual_Punto_Ficha['white']=r'ScrabbleAR_Imagenes_png\modelo_ficha.png'#r'ScrabbleAR_Imagenes_png\Transparente.png'
    return(Dicc_Actual_Punto_Ficha)

def Update_Tablero2(window,Dicc):
    inicio=r'ScrabbleAR_Imagenes_png\icono_inicio.png'
    yellow=r'ScrabbleAR_Imagenes_png\icono_x3.png'
    red=r'ScrabbleAR_Imagenes_png\icono_x2.png'
    green=r'ScrabbleAR_Imagenes_png\icono_-3.png'
    blue=r'ScrabbleAR_Imagenes_png\icono_-2.png'
    white=r'ScrabbleAR_Imagenes_png\modelo_ficha.png'#r'ScrabbleAR_Imagenes_png\icono_blanco.png'

    for x in range(15):
        for y in range(15):
            coord=(x,y)
            if(Dicc[coord][1]=="yellow"):
                Dicc[coord].append(yellow)
                window[coord].update(image_filename=yellow,image_size=(40,40),image_subsample=5)
            elif(Dicc[coord][1]=="red"):
                Dicc[coord].append(red)
                window[coord].update(image_filename=red,image_size=(40,40),image_subsample=5)
            elif(Dicc[coord][1]=="green"):
                Dicc[coord].append(green)
                window[coord].update(image_filename=green,image_size=(40,40),image_subsample=5)
            elif(Dicc[coord][1]=="blue"):
                Dicc[coord].append(blue)
                window[coord].update(image_filename=blue,image_size=(40,40),image_subsample=5)
            elif(coord==(7,7)):
                Dicc[coord].append(inicio)
                window[coord].update(image_filename=inicio,image_size=(40,40),image_subsample=5)
            else:
                Dicc[coord].append(white)
                window[coord].update(image_filename=white,image_size=(40,40),image_subsample=5)
    return Dicc

def rutas_letras_CPU(Dicc_letra_puntajes):
    Dicc_letras_rutas_CPU={'A1':r'ScrabbleAR_Imagenes_png\ficha_A1_N.png','A2':r'ScrabbleAR_Imagenes_png\ficha_A2_N.png','B2':r'ScrabbleAR_Imagenes_png\ficha_B2_N.png','B3':r'ScrabbleAR_Imagenes_png\ficha_B3_N.png','B4':r'ScrabbleAR_Imagenes_png\ficha_B4_N.png',
        'C1':r'ScrabbleAR_Imagenes_png\ficha_C1_N.png','C2':r'ScrabbleAR_Imagenes_png\ficha_C2_N.png','C3':r'ScrabbleAR_Imagenes_png\ficha_C3_N.png','D1':r'ScrabbleAR_Imagenes_png\ficha_D1_N.png','D2':r'ScrabbleAR_Imagenes_png\ficha_D2_N.png','D3':r'ScrabbleAR_Imagenes_png\ficha_D3_N.png',
        'E1':r'ScrabbleAR_Imagenes_png\ficha_E1_N.png','E2':r'ScrabbleAR_Imagenes_png\ficha_E2_N.png','F3':r'ScrabbleAR_Imagenes_png\ficha_F3_N.png','F4':r'ScrabbleAR_Imagenes_png\ficha_F4_N.png','F5':r'ScrabbleAR_Imagenes_png\ficha_F5_N.png','G1':r'ScrabbleAR_Imagenes_png\ficha_G1_N.png',
        'G2':r'ScrabbleAR_Imagenes_png\ficha_G2_N.png','G3':r'ScrabbleAR_Imagenes_png\ficha_G3_N.png','H3':r'ScrabbleAR_Imagenes_png\ficha_H3_N.png','H4':r'ScrabbleAR_Imagenes_png\ficha_H4_N.png','H5':r'ScrabbleAR_Imagenes_png\ficha_H5_N.png','I1':r'ScrabbleAR_Imagenes_png\ficha_I1_N.png',
        'I2':r'ScrabbleAR_Imagenes_png\ficha_I2_N.png','J5':r'ScrabbleAR_Imagenes_png\ficha_J5_N.png','J6':r'ScrabbleAR_Imagenes_png\ficha_J6_N.png','J7':r'ScrabbleAR_Imagenes_png\ficha_J7_N.png','K7':r'ScrabbleAR_Imagenes_png\ficha_K7_N.png','K8':r'ScrabbleAR_Imagenes_png\ficha_K8_N.png',
        'K9':r'ScrabbleAR_Imagenes_png\ficha_K9_N.png','L1':r'ScrabbleAR_Imagenes_png\ficha_L1_N.png','L2':r'ScrabbleAR_Imagenes_png\ficha_L2_N.png','M2':r'ScrabbleAR_Imagenes_png\ficha_M2_N.png','M3':r'ScrabbleAR_Imagenes_png\ficha_M3_N.png','M4':r'ScrabbleAR_Imagenes_png\ficha_M4_N.png',
        'N1':r'ScrabbleAR_Imagenes_png\ficha_N1_N.png','N2':r'ScrabbleAR_Imagenes_png\ficha_N2_N.png','Ñ7':r'ScrabbleAR_Imagenes_png\ficha_Ñ7_N.png','Ñ8':r'ScrabbleAR_Imagenes_png\ficha_Ñ8_N.png','Ñ9':r'ScrabbleAR_Imagenes_png\ficha_Ñ9_N.png','O1':r'ScrabbleAR_Imagenes_png\ficha_O1_N.png',
        'O2':r'ScrabbleAR_Imagenes_png\ficha_O2_N.png','P2':r'ScrabbleAR_Imagenes_png\ficha_P2_N.png','P3':r'ScrabbleAR_Imagenes_png\ficha_P3_N.png','P4':r'ScrabbleAR_Imagenes_png\ficha_P4_N.png','Q7':r'ScrabbleAR_Imagenes_png\ficha_Q7_N.png','Q8':r'ScrabbleAR_Imagenes_png\ficha_Q8_N.png',
        'Q9':r'ScrabbleAR_Imagenes_png\ficha_Q9_N.png','R1':r'ScrabbleAR_Imagenes_png\ficha_R1_N.png','R2':r'ScrabbleAR_Imagenes_png\ficha_R2_N.png','S1':r'ScrabbleAR_Imagenes_png\ficha_S1_N.png','S2':r'ScrabbleAR_Imagenes_png\ficha_S2_N.png','T1':r'ScrabbleAR_Imagenes_png\ficha_T1_N.png',
        'T2':r'ScrabbleAR_Imagenes_png\ficha_T2_N.png','U1':r'ScrabbleAR_Imagenes_png\ficha_U1_N.png','U2':r'ScrabbleAR_Imagenes_png\ficha_U2_N.png','V3':r'ScrabbleAR_Imagenes_png\ficha_V3_N.png','V4':r'ScrabbleAR_Imagenes_png\ficha_V4_N.png','V5':r'ScrabbleAR_Imagenes_png\ficha_V5_N.png',
        'W7':r'ScrabbleAR_Imagenes_png\ficha_W7_N.png','W8':r'ScrabbleAR_Imagenes_png\ficha_W8_N.png','W9':r'ScrabbleAR_Imagenes_png\ficha_W9_N.png','X7':r'ScrabbleAR_Imagenes_png\ficha_X7_N.png','X8':r'ScrabbleAR_Imagenes_png\ficha_X8_N.png','X9':r'ScrabbleAR_Imagenes_png\ficha_X9_N.png',
        'Y3':r'ScrabbleAR_Imagenes_png\ficha_Y3_N.png','Y4':r'ScrabbleAR_Imagenes_png\ficha_Y4_N.png','Y5':r'ScrabbleAR_Imagenes_png\ficha_Y5_N.png','Z9':r'ScrabbleAR_Imagenes_png\ficha_Z9_N.png','Z10':r'ScrabbleAR_Imagenes_png\ficha_Z10_N.png','Z11':r'ScrabbleAR_Imagenes_png\ficha_Z11_N.png'}

    Dicc_Actual_Punto_Ficha_CPU={}
    for x in Dicc_letra_puntajes:
        clave_Dicc_letras_rutas_CPU=x+str(Dicc_letra_puntajes[x])
        Dicc_Actual_Punto_Ficha_CPU[x]=Dicc_letras_rutas_CPU[clave_Dicc_letras_rutas_CPU]
    return(Dicc_Actual_Punto_Ficha_CPU)

def Update_Infobox(Texto,Color,window):
    global Infobox_Activa
    global temp
    window['Infobox'].update(Texto,text_color='Black',background_color=Color)
    Infobox_Activa = True
    temp = 5

def tiempo_dificultad(dificultad):
    tiempo_ronda=0
    jugadores=2
    rondas_totales=30
    if(dificultad=="Facil"):
        tiempo_ronda=60
        secs =tiempo_ronda*jugadores*rondas_totales
    elif(dificultad=="Normal"):
        tiempo_ronda=45
        secs=tiempo_ronda*jugadores*rondas_totales
    elif (dificultad =="Dificil"):
        tiempo_ronda=30
        secs=tiempo_ronda*jugadores*rondas_totales
    return((secs*100),(tiempo_ronda*100))

def intercambio_Fichas_CPU(fichas_CPU,Bolsa_Diccionario,Cant_fichas):
    for x in range(len(fichas_CPU)):
        Bolsa_Diccionario[fichas_CPU[x]]=(Bolsa_Diccionario[fichas_CPU[x]])+1
        Cant_fichas=Cant_fichas+1
    fichas_CPU=""
    for x in range(7):
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    return(fichas_CPU,Cant_fichas)

def aleatorio_Dificil():
    lista_opciones=["verb","sus","adj"]
    x=random.randint(0,2)
    return(lista_opciones[x])

def Letra_Bolsa(Bolsa_Diccionario,Cant_fichas):
    sigue=True
    letra=""
    while((sigue)and(Cant_fichas >= 14)):
        x=random.randint(0,(len(Bolsa_Diccionario.keys())-1))
        letra=list(Bolsa_Diccionario.keys())[x]
        if(Bolsa_Diccionario[letra]> 0):
            Bolsa_Diccionario[letra]=(Bolsa_Diccionario[letra])-1
            Cant_fichas=Cant_fichas-1
            sigue=False
            break
    if Cant_fichas < 14 :
        print("El juego ACABA porque uno de los 2 jugadores no tiene sus 7 fichas")
    return(letra)

def Update_Tablero(window,Dicc):
    Lista_Tableros=[
        {"0,0":"white","0,1":"white","0,2":"red","0,3":"white","0,4":"green","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"green","0,11":"white","0,12":"red","0,13":"white","0,14":"white",
         "1,0":"white","1,1":"green","1,2":"white","1,3":"white","1,4":"white","1,5":"yellow","1,6":"white","1,7":"blue","1,8":"white","1,9":"yellow","1,10":"white","1,11":"white","1,12":"white","1,13":"green","1,14":"white",
         "2,0":"red","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"green","2,7":"white","2,8":"green","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"red",
         "3,0":"white","3,1":"white","3,2":"white","3,3":"blue","3,4":"white","3,5":"white","3,6":"white","3,7":"yellow","3,8":"white","3,9":"white","3,10":"white","3,11":"blue","3,12":"white","3,13":"white","3,14":"white",
         "4,0":"green","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"green",
         "5,0":"white","5,1":"yellow","5,2":"white","5,3":"white","5,4":"white","5,5":"blue","5,6":"white","5,7":"red","5,8":"white","5,9":"blue","5,10":"white","5,11":"white","5,12":"white","5,13":"yellow","5,14":"white",
         "6,0":"white","6,1":"white","6,2":"green","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"green","6,13":"white","6,14":"white",
         "7,0":"white","7,1":"blue","7,2":"white","7,3":"yellow","7,4":"white","7,5":"red","7,6":"white","7,7":"black","7,8":"white","7,9":"red","7,10":"white","7,11":"yellow","7,12":"white","7,13":"blue","7,14":"white",
         "8,0":"white","8,1":"white","8,2":"green","8,3":"white","8,4":"white","8,5":"white","8,6":"white","8,7":"white","8,8":"white","8,9":"white","8,10":"white","8,11":"white","8,12":"green","8,13":"white","8,14":"white",
         "9,0":"white","9,1":"yellow","9,2":"white","9,3":"white","9,4":"white","9,5":"blue","9,6":"white","9,7":"red","9,8":"white","9,9":"blue","9,10":"white","9,11":"white","9,12":"white","9,13":"yellow","9,14":"white",
         "10,0":"green","10,1":"white","10,2":"white","10,3":"white","10,4":"white","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"white","10,11":"white","10,12":"white","10,13":"white","10,14":"green",
         "11,0":"white","11,1":"white","11,2":"white","11,3":"blue","11,4":"white","11,5":"white","11,6":"white","11,7":"yellow","11,8":"white","11,9":"white","11,10":"white","11,11":"blue","11,12":"white","11,13":"white","11,14":"white",
         "12,0":"red","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"green","12,7":"white","12,8":"green","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"red",
         "13,0":"white","13,1":"green","13,2":"white","13,3":"white","13,4":"white","13,5":"yellow","13,6":"white","13,7":"blue","13,8":"white","13,9":"yellow","13,10":"white","13,11":"white","13,12":"white","13,13":"green","13,14":"white",
         "14,0":"white","14,1":"white","14,2":"red","14,3":"white","14,4":"green","14,5":"white","14,6":"white","14,7":"white","14,8":"white","14,9":"white","14,10":"green","14,11":"white","14,12":"red","14,13":"white","14,14":"white",
             },
        {"0,0":"green","0,1":"white","0,2":"white","0,3":"white","0,4":"white","0,5":"red","0,6":"white","0,7":"white","0,8":"white","0,9":"red","0,10":"white","0,11":"white","0,12":"white","0,13":"white","0,14":"green",
         "1,0":"white","1,1":"green","1,2":"white","1,3":"white","1,4":"white","1,5":"white","1,6":"red","1,7":"white","1,8":"red","1,9":"white","1,10":"white","1,11":"white","1,12":"white","1,13":"green","1,14":"white",
         "2,0":"white","2,1":"white","2,2":"blue","2,3":"green","2,4":"white","2,5":"white","2,6":"white","2,7":"yellow","2,8":"white","2,9":"white","2,10":"white","2,11":"green","2,12":"blue","2,13":"white","2,14":"white",
         "3,0":"white","3,1":"white","3,2":"green","3,3":"blue","3,4":"white","3,5":"white","3,6":"white","3,7":"white","3,8":"white","3,9":"white","3,10":"white","3,11":"blue","3,12":"green","3,13":"white","3,14":"white",
         "4,0":"white","4,1":"white","4,2":"white","4,3":"white","4,4":"blue","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"blue","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"white",
         "5,0":"white","5,1":"white","5,2":"green","5,3":"white","5,4":"white","5,5":"yellow","5,6":"red","5,7":"white","5,8":"red","5,9":"yellow","5,10":"white","5,11":"white","5,12":"green","5,13":"white","5,14":"white",
         "6,0":"white","6,1":"red","6,2":"white","6,3":"white","6,4":"white","6,5":"red","6,6":"white","6,7":"white","6,8":"white","6,9":"red","6,10":"white","6,11":"white","6,12":"white","6,13":"red","6,14":"white",
         "7,0":"white","7,1":"white","7,2":"yellow","7,3":"white","7,4":"white","7,5":"white","7,6":"white","7,7":"black","7,8":"white","7,9":"white","7,10":"white","7,11":"white","7,12":"yellow","7,13":"white","7,14":"white",
         "8,0":"white","8,1":"red","8,2":"white","8,3":"white","8,4":"white","8,5":"red","8,6":"white","8,7":"white","8,8":"white","8,9":"red","8,10":"white","8,11":"white","8,12":"white","8,13":"red","8,14":"white",
         "9,0":"white","9,1":"white","9,2":"green","9,3":"white","9,4":"white","9,5":"yellow","9,6":"red","9,7":"white","9,8":"red","9,9":"yellow","9,10":"white","9,11":"white","9,12":"green","9,13":"white","9,14":"white",
         "10,0":"white","10,1":"white","10,2":"white","10,3":"white","10,4":"blue","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"blue","10,11":"white","10,12":"white","10,13":"white","10,14":"white",
         "11,0":"white","11,1":"white","11,2":"green","11,3":"blue","11,4":"white","11,5":"white","11,6":"white","11,7":"white","11,8":"white","11,9":"white","11,10":"white","11,11":"blue","11,12":"green","11,13":"white","11,14":"white",
         "12,0":"white","12,1":"white","12,2":"blue","12,3":"green","12,4":"white","12,5":"white","12,6":"white","12,7":"yellow","12,8":"white","12,9":"white","12,10":"white","12,11":"green","12,12":"blue","12,13":"white","12,14":"white",
         "13,0":"white","13,1":"green","13,2":"white","13,3":"white","13,4":"white","13,5":"white","13,6":"red","13,7":"white","13,8":"red","13,9":"white","13,10":"white","13,11":"white","13,12":"white","13,13":"green","13,14":"white",
         "14,0":"green","14,1":"white","14,2":"white","14,3":"white","14,4":"white","14,5":"red","14,6":"white","14,7":"white","14,8":"white","14,9":"red","14,10":"white","14,11":"white","14,12":"white","14,13":"white","14,14":"green",
             },
        {"0,0":"white","0,1":"white","0,2":"white","0,3":"white","0,4":"blue","0,5":"white","0,6":"white","0,7":"white","0,8":"white","0,9":"white","0,10":"red","0,11":"white","0,12":"white","0,13":"white","0,14":"white",
         "1,0":"green","1,1":"white","1,2":"white","1,3":"white","1,4":"white","1,5":"white","1,6":"white","1,7":"blue","1,8":"white","1,9":"white","1,10":"white","1,11":"white","1,12":"white","1,13":"white","1,14":"green",
         "2,0":"white","2,1":"white","2,2":"white","2,3":"white","2,4":"white","2,5":"white","2,6":"blue","2,7":"white","2,8":"white","2,9":"white","2,10":"white","2,11":"white","2,12":"white","2,13":"white","2,14":"white",
         "3,0":"red","3,1":"white","3,2":"blue","3,3":"white","3,4":"white","3,5":"white","3,6":"red","3,7":"white","3,8":"white","3,9":"white","3,10":"white","3,11":"white","3,12":"red","3,13":"white","3,14":"red",
         "4,0":"white","4,1":"white","4,2":"white","4,3":"white","4,4":"white","4,5":"white","4,6":"white","4,7":"white","4,8":"white","4,9":"white","4,10":"white","4,11":"white","4,12":"white","4,13":"white","4,14":"white",
         "5,0":"white","5,1":"white","5,2":"white","5,3":"yellow","5,4":"white","5,5":"white","5,6":"white","5,7":"white","5,8":"white","5,9":"white","5,10":"white","5,11":"yellow","5,12":"white","5,13":"white","5,14":"white",
         "6,0":"blue","6,1":"white","6,2":"white","6,3":"white","6,4":"white","6,5":"white","6,6":"white","6,7":"white","6,8":"white","6,9":"white","6,10":"white","6,11":"white","6,12":"white","6,13":"white","6,14":"red",
         "7,0":"white","7,1":"white","7,2":"white","7,3":"green","7,4":"white","7,5":"white","7,6":"white","7,7":"black","7,8":"white","7,9":"white","7,10":"white","7,11":"green","7,12":"white","7,13":"white","7,14":"white",
         "8,0":"blue","8,1":"white","8,2":"white","8,3":"white","8,4":"white","8,5":"blue","8,6":"white","8,7":"white","8,8":"white","8,9":"blue","8,10":"white","8,11":"white","8,12":"white","8,13":"white","8,14":"red",
         "9,0":"white","9,1":"white","9,2":"white","9,3":"white","9,4":"white","9,5":"white","9,6":"white","9,7":"white","9,8":"white","9,9":"white","9,10":"white","9,11":"white","9,12":"white","9,13":"white","9,14":"white",
         "10,0":"white","10,1":"white","10,2":"white","10,3":"white","10,4":"yellow","10,5":"white","10,6":"white","10,7":"white","10,8":"white","10,9":"white","10,10":"yellow","10,11":"white","10,12":"white","10,13":"white","10,14":"white",
         "11,0":"red","11,1":"white","11,2":"blue","11,3":"white","11,4":"white","11,5":"white","11,6":"white","11,7":"white","11,8":"red","11,9":"white","11,10":"white","11,11":"white","11,12":"red","11,13":"white","11,14":"red",
         "12,0":"white","12,1":"white","12,2":"white","12,3":"white","12,4":"white","12,5":"white","12,6":"white","12,7":"white","12,8":"blue","12,9":"white","12,10":"white","12,11":"white","12,12":"white","12,13":"white","12,14":"white",
         "13,0":"green","13,1":"white","13,2":"white","13,3":"white","13,4":"white","13,5":"white","13,6":"white","13,7":"blue","13,8":"white","13,9":"white","13,10":"white","13,11":"white","13,12":"white","13,13":"white","13,14":"green",
         "14,0":"white","14,1":"white","14,2":"white","14,3":"white","14,4":"blue","14,5":"white","14,6":"white","14,7":"white","14,8":"white","14,9":"white","14,10":"red","14,11":"white","14,12":"white","14,13":"white","14,14":"white",
             }
             ]

    num = randint(0,(len(Lista_Tableros)-1))
    tablero_random=(Lista_Tableros[num])
    for x in range(15):
        for y in range(15):
            coord = (x,y)
            Pos_Dicc = str(x) + ',' + str(y)
            Dicc[coord][1] = tablero_random[Pos_Dicc]
            window[coord].update(button_color=('Black',str(tablero_random[Pos_Dicc])))
    return Dicc

def Generar_Dicc():
    Dicc = {}
    for j in range(MAX_COL):
        for i in range(MAX_ROWS):
            Dicc[(j,i)] = ['','White']
    return Dicc

def Layout_Columna_Historial(Usuario):
    layout = [[sg.Text('Historial CPU',size=(20, 1),text_color='black',font=("IMPACT", 18),justification='center',background_color='#FDFA57',relief=sg.RELIEF_RAISED)],
              [sg.Listbox([''],font=("Segoe print", 11),size=(20, 12),key=('Historial_CPU'),text_color='black',background_color='#F5DAC1')],
              [sg.Text('Historial '+Usuario,size=(20, 1),text_color='black',font=("IMPACT", 18),justification='center',background_color='#E52C46',relief=sg.RELIEF_RAISED)],
              [sg.Listbox([''],size=(20, 12),font=("Segoe print", 11),key=('Historial_Usuario'),text_color='black',background_color='#F0DCDF')]]
    return layout

def Layout_Columna_Conf(Dicc_Puntajes,Dificultad,CFT):
    layout = [[sg.Text('Dificultad: '+Dificultad,pad =(50,0),font=("impact",16))],
              [sg.Text('Cantidad de fichas: '+str(CFT),key='CantFichas',pad =(50,0),font=("impact",16))],
              [sg.Text('Fichas | Puntos',pad =(50,0),font=("impact",13))],
              [sg.Text('A      |      '+str(Dicc_Puntajes['A']),pad =(72,0),font=("impact",13))],
              [sg.Text('B      |      '+str(Dicc_Puntajes['B']),pad =(72,0),font=("impact",13))],
              [sg.Text('C      |      '+str(Dicc_Puntajes['C']),pad =(72,0),font=("impact",13))],
              [sg.Text('D      |      '+str(Dicc_Puntajes['D']),pad =(72,0),font=("impact",13))],
              [sg.Text('E      |      '+str(Dicc_Puntajes['E']),pad =(74,0),font=("impact",13))],
              [sg.Text('F      |      '+str(Dicc_Puntajes['F']),pad =(74,0),font=("impact",13))],
              [sg.Text('G      |      '+str(Dicc_Puntajes['G']),pad =(72,0),font=("impact",13))],
              [sg.Text('H      |      '+str(Dicc_Puntajes['H']),pad =(72,0),font=("impact",13))],
              [sg.Text('I      |      '+str(Dicc_Puntajes['I']),pad =(76,0),font=("impact",13))],
              [sg.Text('J      |      '+str(Dicc_Puntajes['J']),pad =(75,0),font=("impact",13))],
              [sg.Text('K      |      '+str(Dicc_Puntajes['K']),pad =(72,0),font=("impact",13))],
              [sg.Text('L      |      '+str(Dicc_Puntajes['L']),pad =(75,0),font=("impact",13))],
              [sg.Text('M      |      '+str(Dicc_Puntajes['M']),pad =(69,0),font=("impact",13))],
              [sg.Text('N      |      '+str(Dicc_Puntajes['N']),pad =(72,0),font=("impact",13))],
              [sg.Text('Ñ      |      '+str(Dicc_Puntajes['Ñ']),pad =(72,0),font=("impact",13))],
              [sg.Text('O      |      '+str(Dicc_Puntajes['O']),pad =(72,0),font=("impact",13))],
              [sg.Text('P      |      '+str(Dicc_Puntajes['P']),pad =(72,0),font=("impact",13))],
              [sg.Text('Q      |      '+str(Dicc_Puntajes['Q']),pad =(72,0),font=("impact",13))],
              [sg.Text('R      |      '+str(Dicc_Puntajes['R']),pad =(72,0),font=("impact",13))],
              [sg.Text('S      |      '+str(Dicc_Puntajes['S']),pad =(72,0),font=("impact",13))],
              [sg.Text('T      |      '+str(Dicc_Puntajes['T']),pad =(73,0),font=("impact",13))],
              [sg.Text('U      |      '+str(Dicc_Puntajes['U']),pad =(72,0),font=("impact",13))],
              [sg.Text('V      |      '+str(Dicc_Puntajes['V']),pad =(72,0),font=("impact",13))],
              [sg.Text('W      |      '+str(Dicc_Puntajes['W']),pad =(68,0),font=("impact",13))],
              [sg.Text('X      |      '+str(Dicc_Puntajes['X']),pad =(74,0),font=("impact",13))],
              [sg.Text('Y      |      '+str(Dicc_Puntajes['Y']),pad =(73,0),font=("impact",13))],
              [sg.Text('Z      |      '+str(Dicc_Puntajes['Z']),pad =(74,0),font=("impact",13))]]
    return layout

def Layout_Columna():

    layout = [ [sg.Text('Tiempo Disponible',font=("impact",20))],
               [sg.Text("00:00",font=("Bahnschrift",20),key=('Tiempo_Ronda')),sg.Text('|',font=("Bahnschrift",20)),sg.Text("00:00",font=("Bahnschrift",20),key=('Tiempo'))],
               [sg.Text('__________________________________')],
               [sg.Text('Puntos  CPU',key='PuntosCPU',font=("impact",20))],
               [sg.Text('0000',key='PuntajeCPU',font=("impact",20))],
               [sg.Text('__________________________________')],
               [sg.Text('Puntos Usuario',key='PuntosUsuario',font=("impact",20))],
               [sg.Text('0000',key='PuntajeUsuario',font=("impact",20))],
               [sg.Text('__________________________________')],
               [sg.Button('<',key='Mostrar',pad=((222,0),(29,2)))],
               [sg.Button('()',key='Rotar',pad=((222,0),(2,29)))],
               [sg.Text(pad=((6,0),(5,2)),size=(20, 3),key='Infobox',font=("Consolas", 16),background_color='#A4A4A4',justification='center',relief=sg.RELIEF_SOLID)], #Entran 60 caracteres
               [sg.Button(button_text='Terminar turno',size=(15,0),font=("Unispace",20),pad=((5,0),(5,3)))],
               [sg.Button(button_text='Validar',size=(15,0),font=("Unispace",20),pad=((5,0),(5,3)))],
               [sg.Button(button_text='Intercambiar fichas',size=(15,0),font=("Unispace",20))],
               [sg.Button(button_text='Pausar',key='Pausar',font=("default",16),pad=((5,0),(3,0)) ), #font=("default",19),pad=((5,43),(5,3))
                sg.Button(button_text='Rendirse',key='Rendirse',font=("default",16),pad=((5,0),(2,0)) ),#font=("default",19),pad=((5,43),(5,3))
                sg.Button(button_text='Salir',key='Salir',font=("default",16))] ]#font=("default",19)
    return layout

def Layout_Tabla(Lista_Atril,Bolsa_Diccionario,Cant_fichas,Dicc_rutas_letras_puntaje_partida):
    MAX_ROWS = MAX_COL = 15 #ACA????
    formato_fichas_cpu={'filename':r'ScrabbleAR_Imagenes_png\imagen_CPU.png','size':(40,40),'pad':(7,3)  }

    #formato_fichas_jugador={'font':('',25),'button_color':(None,'black'),'image_filename':'C:\Users\delma\Desktop\2do Año\PYTHON\Practicas\Scrabble\Ficha.png','image_size':(40,40),'pad':(7,3)  }
    #Para luego reemplazar los colores dados por el boton con imagenes
    if len(Lista_Atril) < 7 :
        Letra_1=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_1)
        Letra_2=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_2)
        Letra_3=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_3)
        Letra_4=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_4)
        Letra_5=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_5)
        Letra_6=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_6)
        Letra_7=Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
        Lista_Atril.append(Letra_7)
    layout = [[sg.Text('',key='texto1',pad=(45,3)),(sg.Image(**formato_fichas_cpu,key='fichasbot1')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot2')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot3')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot4')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot5')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot6')),
                                                    (sg.Image(**formato_fichas_cpu,key='fichasbot7'))],
                [(sg.Image(filename='Atril_back.png',key='atril',pad=(20,3)))]]

    layout.extend([[sg.Button('', size=(4, 2),key=(i,j),pad=(0,0))for j in range(MAX_COL)] for i in range(MAX_ROWS)])

    layout.extend([[sg.Text('',key='texto2',pad=(28,3)),
                    (sg.Button(key=0,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[0]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=1,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[1]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=2,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[2]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=3,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[3]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=4,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[4]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=5,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[5]][0],image_size=(40,40),image_subsample=5)),
                    (sg.Button(key=6,pad=(7,3),size=(3,1),font=('default',18),button_color=('black','#FDD357'),image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[6]][0],image_size=(40,40),image_subsample=5))],
                    [(sg.Image(filename='Atril.png',key='texto'))]])

    return layout

def Llenar_Atril(Lista_Atril,window,Bolsa_Diccionario,Cant_fichas,Dicc_rutas_letras_puntaje_partida):
    for pos in range(len(Lista_Atril)):
        if (Lista_Atril[pos] == ''):
            Lista_Atril[pos] = Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
            #window[pos].update(Lista_Atril[pos])
            window[pos].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[pos]][0],image_size=(40,40),image_subsample=5)


def Coord_Ocupada(LCO,event):
    if (event in LCO):
        return True
    else:
        return False

def Coord_Adyacentes(coord):
    x,y=coord
    coord1=(x+1,y)
    coord2=(x,y+1)
    coord3=(x-1,y)
    coord4=(x,y-1)
    return coord1,coord2,coord3,coord4

def Coord_Disponible(LCO,CCD):
    for x in range(len(LCO)):
        for y in Coord_Adyacentes(LCO[x]):
            if(((y[0]< 15)and(y[1]< 15))and((y[0]>-1)and(y[1]>-1))):
                CCD.add(y)

def Coord_Desbloqueada(CCD,event):
    if (event in CCD):
        return True
    else:
        return False

def Eliminar_Coords(CCD,coord):
    '''Elimina Coordenadas.'''
    CCD.discard(((coord[0]-1),coord[1]))     #Arriba
    CCD.discard((coord[0],(coord[1]+1)))     #Derecha
    CCD.discard(((coord[0]+1),coord[1]))     #Abajo
    CCD.discard((coord[0],(coord[1]-1)))     #Izquierda

def Update_Fichas_Colocadas(LCOPR,window,Dicc,Dicc_rutas_letras_puntaje_partida):
    for coord in LCOPR:
        window[coord].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[coord][0]][2],image_size=(40,40),image_subsample=5)

def Mensaje_Turno(Turno_Usuario):
    if Turno_Usuario:
        sg.popup('Estas Listo?\nEs tu turno',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)
    else:
        sg.popup('Estas Listo?\nEs el turno de la IA',custom_text="Si,lo estoy",no_titlebar=True,keep_on_top=True)

def Eliminar_Elementos_Ocupados_CDD(LCO,CCD):
    for L in LCO:
        CCD.discard(tuple(L))

def Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega,window):
    if (LCOPR[0][0] == LCOPR[1][0]): #Si entra la palabra formada esta en Horizontal
        LCOPR = sorted(LCOPR, key=lambda tup: tup[1])
        for coord in LCOPR:
            Palabra = Palabra + Dicc[coord][0]
    else:                            #Sino esta en vertical
        LCOPR = sorted(LCOPR, key=lambda tup: tup[0])
        for coord in LCOPR:
            Palabra = Palabra + Dicc[coord][0]
    if verificar_Palabra(Palabra,Dificultad,Dificil_se_juega):
        Texto = '"'+Palabra+'"\n'+'Es una palabra valida'
        Update_Infobox(Texto,'#57FD57',window)
    else:
        Texto = '"'+Palabra+'"\n'+'No es una palabra valida'
        Update_Infobox(Texto,'#FD5757',window)
        Palabra = ''
    return Palabra

def elimino_fichas_Usadas(fichas_CPU,Palabra):
    for x in range(len(Palabra)):
        fichas_CPU=fichas_CPU.replace(Palabra[x].upper(),"") #Elimino las fichas usadas
    return(fichas_CPU)

def Importar_Datos():
    arch = open('Archivo_Opciones.csv','r',encoding="utf8")
    reader = csv.reader(arch)
    index = 0
    for row in reader:
        if (len(row) > 0):
            if (index != 0):
                if (row[0] == 'True'):
                    if (row[2] == 'True'):
                        dificultad =  'Facil'
                        Tiempo_Ronda = row[14]
                        Tiempo = row[13]
                    elif (row[3] == 'True'):
                        dificultad =  'Medio'
                        Tiempo_Ronda = row[14]
                        Tiempo = row[13]
                    elif (row[4] == 'True'):
                        dificultad =  'Dificil'
                        Tiempo_Ronda = row[14]
                        Tiempo = row[13]
                    else:
                        dificultad =  'Personalizado'
                        Tiempo_Ronda = row[14]
                        Tiempo = row[13]
                        Lista_TP = []
                        if row[15] == 'True':
                            Lista_TP.append('adj')
                        if row[16] == 'True':
                            Lista_TP.append('sus')
                        if row[17] == 'True':
                            Lista_TP.append('verb')
                    Usuario = row[1]
                    Lista_Lotes = [int(float(row[6])),int(float(row[7])),int(float(row[8])),int(float(row[9])),int(float(row[10])),int(float(row[11])),int(float(row[12]))]
                    arch.close()
                    Dicc_Puntajes = {"A":int(Lista_Lotes[0]),"B":int(Lista_Lotes[2]),"C":int(Lista_Lotes[1]),"D":int(Lista_Lotes[1]),"E":int(Lista_Lotes[0]),"F":int(Lista_Lotes[3]),"G":int(Lista_Lotes[1]),"H":int(Lista_Lotes[3]),"I":int(Lista_Lotes[0]),"J":int(Lista_Lotes[4]),"K":int(Lista_Lotes[5]),"L":int(Lista_Lotes[0]),"M":int(Lista_Lotes[2]),"N":int(Lista_Lotes[0]),
                                      u"Ñ":int(Lista_Lotes[5]),"O":int(Lista_Lotes[0]),"P":int(Lista_Lotes[2]),"Q":int(Lista_Lotes[5]),"R":int(Lista_Lotes[0]),"S":int(Lista_Lotes[0]),"T":int(Lista_Lotes[0]),"U":int(Lista_Lotes[0]),"V":int(Lista_Lotes[3]),"W":int(Lista_Lotes[5]),"X":int(Lista_Lotes[5]),"Y":int(Lista_Lotes[3]),"Z":int(Lista_Lotes[6])}

                    Dicc_Bolsa={"A":int(row[18]),"B":int(row[19]),"C":int(row[20]),"D":int(row[21]),"E":int(row[22]),"F":int(row[23]),"G":int(row[24]),"H":int(row[25]),"I":int(row[26]),"J":int(row[27]),"K":int(row[28]),"L":int(row[29]),"M":int(row[30]),"N":int(row[31]),
                                      u"Ñ":int(row[32]),"O":int(row[33]),"P":int(row[34]),"Q":int(row[35]),"R":int(row[36]),"S":int(row[37]),"T":int(row[38]),"U":int(row[39]),"V":int(row[40]),"W":int(row[41]),"X":int(row[42]),"Y":int(row[43]),"Z":int(row[44])}

                    return Usuario,dificultad,Dicc_Puntajes,Dicc_Bolsa,Tiempo_Ronda,Tiempo,Lista_TP
            else:
                index = index + 1

def Calcular_Puntaje(Palabra,Dicc_Puntajes):
    PPR = 0
    for letra in Palabra:
        PPR = PPR + Dicc_Puntajes[letra]
    return PPR

def Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc,Dicc_rutas_letras_puntaje_partida_CPU,LCDPR_CPU,LCO_CPU):
    for x in range(len(Palabra)):
        #window[(coordenadas_CPU[0],coordenadas_CPU[1]+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
        window[(coordenadas_CPU[0],coordenadas_CPU[1]+x)].update(image_filename=Dicc_rutas_letras_puntaje_partida_CPU[str(Palabra[x])],image_size=(40,40),image_subsample=5)
        Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+x)][0] =str(Palabra[x])
        LCO.append((coordenadas_CPU[0],coordenadas_CPU[1]+x))
        LCO_CPU.append((coordenadas_CPU[0],coordenadas_CPU[1]+x))
        LCDPR_CPU.append((coordenadas_CPU[0],coordenadas_CPU[1]+x))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc,Dicc_rutas_letras_puntaje_partida_CPU,LCDPR_CPU,LCO_CPU):
    for y in range(len(Palabra)):
        #window[(coordenadas_CPU[0]+y,coordenadas_CPU[1])].update(str(Palabra[y]),button_color=('black','#7D4DE4'))
        window[(coordenadas_CPU[0]+y,coordenadas_CPU[1])].update(image_filename=Dicc_rutas_letras_puntaje_partida_CPU[str(Palabra[y])],image_size=(40,40),image_subsample=5)
        Dicc[(coordenadas_CPU[0]+y,coordenadas_CPU[1])][0] =str(Palabra[y])
        LCO.append((coordenadas_CPU[0]+y,coordenadas_CPU[1]))
        LCO_CPU.append((coordenadas_CPU[0]+y,coordenadas_CPU[1]))
        LCDPR_CPU.append((coordenadas_CPU[0]+y,coordenadas_CPU[1]))
        Coord_Disponible(LCO,CCD)
        Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU,Dificultad,Dificil_se_juega,Bolsa_Diccionario,Cant_fichas,Dicc_Puntajes,PT_CPU,Dicc_rutas_letras_puntaje_partida_CPU,LCO_CPU):
    global PrimerRonda
    global HistorialCPU
    LCDPR_CPU = []
    CCD_CPU=CCD
    Palabra=fichas_CPU
    intento=True
    puede_Colocarse=False
    if (contador_Turnos_CPU ==0):
        for x in range(7):
            fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas) #En la primera jugada toma 7 fichas aleatorias de la bolsa
            Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    else:
        Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if(((contador_Turnos_CPU % 3)==0) and (Cant_fichas > 14 )):
        fichas_CPU,Cant_fichas=intercambio_Fichas_CPU(fichas_CPU,Bolsa_Diccionario,Cant_fichas)
        Palabra=formar_palabra(fichas_CPU,Dificultad,Dificil_se_juega)
        contador_Turnos_CPU=contador_Turnos_CPU+1
    if Palabra != "":
        Palabra=Palabra.upper()
        fichas_CPU=elimino_fichas_Usadas(fichas_CPU,Palabra)
        if CCD_CPU == set():
            for x in range(len(Palabra)):  #En el primer case , donde CCD esta vacio y se debe empezar en el cuadro 7,7
                #window[(7,7+x)].update(str(Palabra[x]),button_color=('black','#7D4DE4'))
                window[(7,7+x)].update(image_filename=Dicc_rutas_letras_puntaje_partida_CPU[str(Palabra[x])],image_size=(40,40),image_subsample=5)
                Dicc[7,7+x][0] =str(Palabra[x])
                LCO.append((7,7+x))
                LCO_CPU.append((7,7+x))
                Coord_Disponible(LCO,CCD)
                Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
            PrimerRonda = False
        else:
            for x in range(len(CCD)) :
                if(intento):
                    coordenadas_CPU=Selector_de_coordenadas_disponibles(CCD_CPU)
                    if(coordenadas_CPU in CCD_CPU) and(not(coordenadas_CPU in LCO)):
                        if(((len(Palabra)+coordenadas_CPU[1])<15)and((len(Palabra)+coordenadas_CPU[1])>-1)):  #si se va a pasar del tablero al poner la palabra  verticalmente
                            for y in range(len(Palabra)):
                                if(((coordenadas_CPU[0],coordenadas_CPU[1]+(y)) in LCO)or(Dicc[(coordenadas_CPU[0],coordenadas_CPU[1]+(y))][0]!='')):#Si las coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    CCD_CPU.discard(coordenadas_CPU)
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Horizontal(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc,Dicc_rutas_letras_puntaje_partida_CPU,LCDPR_CPU,LCO_CPU)
                                intento=False
                        elif(((len(Palabra)+coordenadas_CPU[0])<15)and((len(Palabra)+coordenadas_CPU[0])>-1)):#si se va a pasar del tablero al poner la palabra horizontalmente
                            for x in range(len(Palabra)):
                                if(((coordenadas_CPU[0]+(x),coordenadas_CPU[1]) in LCO)or(Dicc[(coordenadas_CPU[0]+(x),coordenadas_CPU[1])][0]!='')):#Si la coordenada esta ocupada , sale y busca otra coordenada disponible
                                    puede_Colocarse=False
                                    CCD_CPU.discard(coordenadas_CPU)
                                    break
                                else:
                                    puede_Colocarse=True
                            if(puede_Colocarse):
                                Poner_Vertical(window,Palabra,coordenadas_CPU,LCO,CCD,Dicc,Dicc_rutas_letras_puntaje_partida_CPU,LCDPR_CPU,LCO_CPU)
                                intento=False
            if((intento)and(len(CCD_CPU)>1)):
                print("El robot no tiene una posicion valida para colocar su palabra") #Implementar que se vuelva a buscar uan palabra pero mas corta
        Bonus = Calcular_Bonus(LCDPR_CPU,Dicc_Puntajes,Dicc)
        PPR_CPU = Calcular_Puntaje(Palabra,Dicc_Puntajes)
        PT_CPU = (PT_CPU + PPR_CPU) + Bonus
        HistorialCPU.append(Palabra +' = '+str(PPR_CPU)+' + '+str(Bonus) +' = '+ str((PPR_CPU+Bonus)))
        window['Historial_CPU'].update(HistorialCPU)
        window['PuntajeCPU'].update(str(PT_CPU))
    else:
        print("No hay palabra valida en este momento para la CPU ,la CPU pasa el turno")
    while(((len(fichas_CPU))<7)and(Cant_fichas >= 14)):          #Añado fichas de la bolsa para compeltar 7 al finalizar el turno
        fichas_CPU=fichas_CPU+Letra_Bolsa(Bolsa_Diccionario,Cant_fichas)
    if((len(fichas_CPU))<7):
        print("La CPU no tiene fichas suficientes para continuar , el juego termino")
    return(contador_Turnos_CPU,fichas_CPU,Cant_fichas,PT_CPU)

def Actualizar_CFT(CFT,Dicc_Bolsa):
    CFT = 0
    for cant in Dicc_Bolsa.values():
        CFT = CFT + cant
    return CFT

def Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window,Dicc_rutas_letras_puntaje_partida):
    for Pos in range(len(Lista_Atril)):
        if (Lista_Atril[Pos] == ''): # Si esta posicion esta vacia:
            Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,LCOPR[0],Pos,window,Dicc_rutas_letras_puntaje_partida)

def Validar(LCOPR,CCD,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega,window):
    if Palabra_bien_colocada(LCOPR,window):
        if PrimerRonda:
            if ((7,7) in LCOPR):
                Palabra = Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega,window)
            else:
                Update_Infobox('Debes colocar una letra en la casilla "Inicio"!','#5798FD',window)
        else:
            bool = False
            for i in LCOPR:
                if i in CCD:
                    bool = True
                    break
            if bool:
                Palabra = Verificar(Palabra,LCOPR,Dicc,Dificultad,Dificil_se_juega,window)
            else:
                Update_Infobox('Coloca la palabra en una casilla valida!','#5798FD',window)
    return Palabra

def Palabra_bien_colocada(LCOPR,window):
    if len(LCOPR) > 1:
        Vertical = True
        Horizontal = True
        for i in range(2):
            if (Horizontal):
                LCOPR = sorted(LCOPR, key=lambda tup: tup[1])
                for x in range(len(LCOPR)-1):
                    sig = x + 1
                    if (LCOPR[x][0] != LCOPR[sig][0]) or ((LCOPR[x][1] + 1) != LCOPR[sig][1]):
                        Horizontal = False
            else:
                LCOPR = sorted(LCOPR, key=lambda tup: tup[0])
                for x in range(len(LCOPR)-1):
                    sig = x + 1
                    if (LCOPR[x][1] != LCOPR[sig][1]) or ((LCOPR[x][0] + 1) != LCOPR[sig][0]):
                        Vertical = False
        if Horizontal or Vertical:
            return True
        else:
            Update_Infobox('Esta palabra esta mal colocada!','#5798FD',window)
            return False
    else:
        Update_Infobox('Debes formar palabras de por lo menos 2 fichas!','#5798FD',window)
        return False

def TerminarTurno(LCOPR,LCO,CCD,Dicc,Lista_Atril,PTU,Palabra,Dificultad,Dificil_se_juega,Dicc_Puntajes,Dicc_Bolsa,CFT,Bonus,window,Dicc_rutas_letras_puntaje_partida):
    global PrimerRonda
    global HistorialUsuario
    if (Palabra == '') and (LCOPR != []): #Si no se valido antes Y en el tablero hay fichas:
        Palabra = Validar(LCOPR,CCD,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega,window)

    if (Palabra != ''):
        PPR = Calcular_Puntaje(Palabra,Dicc_Puntajes) #Puntaje por ronda
        PTU = (PTU + PPR) + Bonus
        window['PuntajeUsuario'].update(str(PTU))
        HistorialUsuario.append(Palabra +' = '+str(PPR)+' + '+str(Bonus) +' = '+ str((PPR+Bonus)))
        window['Historial_Usuario'].update(HistorialUsuario)
        Llenar_Atril(Lista_Atril,window,Dicc_Bolsa,CFT,Dicc_rutas_letras_puntaje_partida)
        PrimerRonda = False
    else:
        Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window,Dicc_rutas_letras_puntaje_partida)
    return PTU

def Actualizar_LCO(LCOPR,LCO,LCO_Usuario):
    for coord in LCOPR:
        LCO.append(coord)
        LCO_Usuario.append(coord)

def Intercambio_FichasTablero(LCOPR,Dicc,event1,event2,window,Dicc_rutas_letras_puntaje_partida):
    if event1 != event2:
        aux = Dicc[event2][0]
        Dicc[event2][0] = Dicc[event1][0]
        Dicc[event1][0] = aux
        if Coord_Ocupada(LCOPR,event2):
            window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event2][0]][0],image_size=(40,40),image_subsample=5)
            window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]][0],image_size=(40,40),image_subsample=5)
            #window[event2].update(Dicc[event2][0],button_color=('black','#FDD357'))
            #window[event1].update(Dicc[event1][0],button_color=('black','#FDD357'))
        else:
            #window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event2][1]],image_size=(40,40),image_subsample=5)
            #window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]],image_size=(40,40),image_subsample=5)
            window[event1].update(image_filename=Dicc[event1][2],image_size=(40,40),image_subsample=5)
            window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event2][0]][0],image_size=(40,40),image_subsample=5)
            LCOPR.remove(event1)
            LCOPR.append(event2)
    else:
        window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]][0],image_size=(40,40),image_subsample=5)

def Intercambio_FichasAtril(Lista_Atril,Pos_letra1,Pos_letra2,window,Dicc_rutas_letras_puntaje_partida):
    if (Pos_letra1 != Pos_letra2):
        #window[Pos_letra1].update(Lista_Atril[Pos_letra2])
        #window[Pos_letra2].update(Lista_Atril[Pos_letra1])
        if ("" ==(Lista_Atril[Pos_letra1])):
            window[Pos_letra2].update(image_filename=Dicc_rutas_letras_puntaje_partida["white"],image_size=(40,40),image_subsample=5)
            window[Pos_letra1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[Pos_letra2]][0],image_size=(40,40),image_subsample=5)
        elif ("" ==(Lista_Atril[Pos_letra2])):
            window[Pos_letra1].update(image_filename=Dicc_rutas_letras_puntaje_partida["white"],image_size=(40,40),image_subsample=5)
            window[Pos_letra2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[Pos_letra1]][0],image_size=(40,40),image_subsample=5)
        else:
            window[Pos_letra1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[Pos_letra2]][0],image_size=(40,40),image_subsample=5)
            window[Pos_letra2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[Pos_letra1]][0],image_size=(40,40),image_subsample=5)
        aux = Lista_Atril[Pos_letra2]
        Lista_Atril[Pos_letra2] = Lista_Atril[Pos_letra1]
        Lista_Atril[Pos_letra1] = aux
    else:
        window[Pos_letra1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[Pos_letra1]][0],image_size=(40,40),image_subsample=5)

def Intercambio_Fichas(Dicc,Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida):
    aux = Dicc[event1][0]
    Dicc[event1][0] = Lista_Atril[event2]
    Lista_Atril[event2] = aux
    if Dicc[event1][0] == "" :
        window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida["white"],image_size=(40,40),image_subsample=5)
        window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[event2]][0],image_size=(40,40),image_subsample=5)
    elif(Lista_Atril[event2] == ""):
        window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]][0],image_size=(40,40),image_subsample=5)
        window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida["white"],image_size=(40,40),image_subsample=5)
    else:
        window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]][0],image_size=(40,40),image_subsample=5)
        window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[event2]][0],image_size=(40,40),image_subsample=5)

    #window[event1].update(Dicc[event1][0],button_color=('black','#FDD357'))
    #window[event2].update(Lista_Atril[event2],button_color=('black','#FDD357'))

def Colocar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,Letra1,event1,event2,window,Dicc_rutas_letras_puntaje_partida):
    Dicc[event2][0] = Letra1
    #window[event2].update(Letra1,button_color=('black','#FDD357'))
    window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Letra1][0],image_size=(40,40),image_subsample=5)
    Lista_Atril[event1] = ''
    #window[event1].update('')
    window[event1].update(image_filename=Dicc_rutas_letras_puntaje_partida["white"],image_size=(40,40),image_subsample=5)
    LCOPR.append(event2)
    #Coord_Disponible(LCOPR,CCD) #Ya que LCOPR contiene unicamente las fichas actuales se tiene
    #Coord_Disponible(LCO,CCD)   #que usar LCO para completar la actualizacion/eliminacion de elementos en CCD
    #Eliminar_Elementos_Ocupados_CDD(LCO,CCD)
    #Eliminar_Elementos_Ocupados_CDD(LCOPR,CCD)
    #window[event1].update(button_color=('black','#FDD357'))
    window[event1].update(image_filename=r'ScrabbleAR_Imagenes_png\modelo_ficha.png',image_size=(40,40),image_subsample=5)

def Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida):
    Lista_Atril[event2] = Dicc[event1][0]
    window[event1].update(image_filename=Dicc[event1][2],image_size=(40,40),image_subsample=5)
    window[event2].update(image_filename=Dicc_rutas_letras_puntaje_partida[Dicc[event1][0]][0],image_size=(40,40),image_subsample=5)
    #window[event1].update('',button_color=('white',Dicc[event1][1]))
    #window[event2].update(Dicc[event1][0])
    Dicc[event1][0] = ''
    LCOPR.remove(event1)

def Acciones_Usuario(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida):
    if (not (event2 in LCO)): #Esto es para saber si por ejemplo, Se quiere intercambiar una (fichaAtril o FichaTablero) con una ficha ya colocada

        if (type(event1) == int) and (type(event2) == tuple):        #Atril X Tablero:
            if (Coord_Ocupada(LCOPR,event2)):                       #Intercambio FichaAtril X Tablero:
                Intercambio_Fichas(Dicc,Lista_Atril,event2,event1,window,Dicc_rutas_letras_puntaje_partida)
            else:                                                   #Colocar Ficha:
                Colocar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,Lista_Atril[event1],event1,event2,window,Dicc_rutas_letras_puntaje_partida)

        elif (type(event1) == tuple) and (type(event2) == int):     #Tablero X Atril:
            if (Lista_Atril[event2] != ''):                         #Intercambio FichaTablero X FichaAtril:
                Intercambio_Fichas(Dicc,Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida)
            else:                                                   #Retirar Ficha:
                Retirar_Ficha(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida)

        elif (type(event1) == tuple) and (type(event2) == tuple):   #Intercambio FichasTablero:
            Intercambio_FichasTablero(LCOPR,Dicc,event1,event2,window,Dicc_rutas_letras_puntaje_partida)

        elif (type(event1) == int) and (type(event2) == int):       #Intercambio FichasAtril:
            Intercambio_FichasAtril(Lista_Atril,event1,event2,window,Dicc_rutas_letras_puntaje_partida)
    else:
        window[event1].update(button_color=('black','#FDD357'))
        Update_Infobox('No puedes interactuar con las fichas ya colocadas!','#5798FD',window)

def Boton_Intercambiar_Fichas(LCOPR,LCO,CCD,CFT,LPI,Dicc,Dicc_Bolsa,Lista_Atril,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles,event,window,Dicc_rutas_letras_puntaje_partida):
    if (type(event) == int):
        if event in LPI:
            LPI.remove(event)
            #window[event].update(button_color=('black','#FDD357'))
            window[event].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[event]][0],image_size=(40,40),image_subsample=5)
        else:
            LPI.append(event)
            #window[event].update(button_color=('white','#57C3FD'))
            window[event].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[event]][1],image_size=(40,40),image_subsample=5)

    elif (event == "Intercambiar fichas"):
        if Boton_Intercambiar:   #Intercambia las fichas y termina
            if (LPI != []) and CFT >= len(LPI):
                for pos in LPI: #Agrego las fichas seleccionadas a la bolsa
                    Dicc_Bolsa[Lista_Atril[pos]] = Dicc_Bolsa[Lista_Atril[pos]] + 1
                for pos in LPI:  #Y de la bolsa, se le da fichas random al usuario
                    x = random.randint(0,(len(Dicc_Bolsa.keys())-1))
                    Letra = list(Dicc_Bolsa.keys())[x]
                    while (Dicc_Bolsa[Letra] <= 0):
                        x = random.randint(0,(len(Dicc_Bolsa.keys())-1))
                        Letra = list(Dicc_Bolsa.keys())[x]
                    Lista_Atril[pos] = Letra
                    Dicc_Bolsa[Lista_Atril[pos]] = Dicc_Bolsa[Lista_Atril[pos]] - 1
                    #window[pos].update(Lista_Atril[pos],button_color=('black','#FDD357'))
                    window[pos].update(image_filename=Dicc_rutas_letras_puntaje_partida[Lista_Atril[pos]][0],image_size=(40,40),image_subsample=5)

                Turnos_Disponibles = Turnos_Disponibles - 1
                Se_Intercambio_Ficha = True
                CFT = Actualizar_CFT(CFT,Dicc_Bolsa)
                window[event].update(button_color=('white','#283B5B'))
            else:
                sg.popup('No has intercambiado ninguna ficha! no pierdes el turno',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
                window[event].update(button_color=('white','#283B5B'))
            Boton_Intercambiar = False
        else: #Recien "Clickeo" el boton intercambiar Fichas
            if Turnos_Disponibles != 1:
                sg.popup('Te quedan '+str(Turnos_Disponibles)+' turnos disponibles\nSelecciona las fichas del atril que quieras cambiar!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
            else:
                sg.popup('Este es el ultimo turno en el que puedes cambiar fichas!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
            Boton_Intercambiar = True
            window[event].update(button_color=('black','#57C3FD'))
            Retirar_Ficha_Automatico(LCOPR,LCO,CCD,Dicc,Lista_Atril,window,Dicc_rutas_letras_puntaje_partida)
    elif event != 'Reloj':
        sg.popup('Debes seleccionar fichas del Atril!',title='Ayuda',background_color='#5798FD',button_color=('Black','White'),keep_on_top=True,non_blocking=True)
    return CFT,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles

def Calcular_Bonus(LCOPR,Dicc_Puntajes,Dicc):
    Bonus=0
    operacion=0
    for x in range(len(LCOPR)):
        if Dicc[LCOPR[x]][1] != 'white':
            if Dicc[LCOPR[x]][1] == 'red':
                operacion = Dicc_Puntajes[Dicc[LCOPR[x]][0]]     #se suma el valor la letra con bonus para obtener el * 2
            elif Dicc[LCOPR[x]][1] == 'yellow':
                operacion = Dicc_Puntajes[Dicc[LCOPR[x]][0]] * 2 #se suma el valor la letra con bonus 2 veces para obtener el * 3
            elif Dicc[LCOPR[x]][1] == 'blue':
                operacion = -2
            elif Dicc[LCOPR[x]][1] == 'green':
                operacion = -3
            Bonus = Bonus + operacion
    return Bonus

def Actualizar_CCD(CCD,LCO):
    Coord_Disponible(LCO,CCD)
    Eliminar_Elementos_Ocupados_CDD(LCO,CCD)

def Update_Columna_Extra(Columna_Historial,window):
    if (Columna_Historial):
        window['Columna_Historial'].update(visible=False)
        window['Columna_Conf'].update(visible=True)
    else:
        window['Columna_Conf'].update(visible=False)
        window['Columna_Historial'].update(visible=True)
def GuardoPartida(Dificultad,DiccRLPP,Dicc,CFT,Usuario,Turnos_Disponibles,PTU,HistorialUsuario,LCO,Tiempo,DiccRLPP_CPU,PT_CPU,fichas_CPU,contador_Turnos_CPU,HistorialCPU,PrimerRonda,Lista_Atril,Dicc_Bolsa,Dicc_Puntajes,tiempo_ronda,CCD,LCO_Usuario,LCO_CPU,tiempo_jugador):
    #Hago una copia de Dicc con keys string para poder guardarlas en json
    Dicc_str={}
    for key in Dicc:
        Dicc_str[str(key)]=Dicc[key]
    info_Usuario={"HistorialUsuario":HistorialUsuario,"DiccRLPP":DiccRLPP,"Usuario":Usuario,"Turnos_Disponibles":Turnos_Disponibles,"PTU":PTU,"Lista_Atril":Lista_Atril,"tiempo_ronda":tiempo_ronda,"LCO_Usuario":LCO_Usuario,"tiempo_jugador":tiempo_jugador}
    info_CPU={"HistorialCPU":HistorialCPU,"DiccRLPP_CPU":DiccRLPP_CPU,"PT_CPU":PT_CPU,"fichas_CPU":fichas_CPU,"contador_Turnos_CPU":contador_Turnos_CPU,"LCO_CPU":LCO_CPU}
    info_Tablero={"Dificultad":Dificultad,"Dicc":Dicc_str,"CFT":CFT,"LCO":LCO,"CCD":CCD,"Tiempo":Tiempo,"PrimerRonda":PrimerRonda,"Dicc_Bolsa":Dicc_Bolsa,"Dicc_Puntajes":Dicc_Puntajes}
    DiccPartida={"info_Usuario":{**info_Usuario},"info_CPU":{**info_CPU},"info_Tablero":{**info_Tablero}      }
    archivo=open("Partida_Guardada.json","w")
    Guardar=json.dump(DiccPartida,archivo)
    archivo.close()
def cargoPartida():
    archivo=open("Partida_Guardada.json","r")
    datos=json.load(archivo)
    archivo.close()
    Dicc={}

    for x in range(len(datos["info_Tablero"]["CCD"])):
        datos["info_Tablero"]["CCD"][x]=tuple(datos["info_Tablero"]["CCD"][x])
    for x in range(len(datos["info_Tablero"]["LCO"])):
        datos["info_Tablero"]["LCO"][x]=tuple(datos["info_Tablero"]["LCO"][x])
    for x in range(len(datos["info_Usuario"]["LCO_Usuario"])):
        datos["info_Usuario"]["LCO_Usuario"][x]=tuple(datos["info_Usuario"]["LCO_Usuario"][x])
    for x in range(len(datos["info_CPU"]["LCO_CPU"])):
        datos["info_CPU"]["LCO_CPU"][x]=tuple(datos["info_CPU"]["LCO_CPU"][x])

    for key in datos["info_Tablero"]["Dicc"]:
        key_dicc=key.strip("()")
        key_dicc=key_dicc.replace(",","")
        x,y=key_dicc.split(" ")
        key_dicc=tuple((int(x),int(y)))
        Dicc[key_dicc]=datos["info_Tablero"]["Dicc"][key]
    datos["info_Tablero"]["Dicc"]=Dicc
    return(datos)

#PROGRAMA PRINCIPAL
def genero_Tablero():
    global Infobox_Activa
    global temp
    global PrimerRonda
    global HistorialUsuario
    global HistorialCPU

    event_popup = sg.popup_yes_no('¿Deseas cargar la partida guardada?',title='Aviso',keep_on_top=True)
    if (event_popup == 'Yes'):
        partida_carga=True
        CCD=set()
        datos=cargoPartida()
        HistorialUsuario=datos["info_Usuario"]["HistorialUsuario"]
        tiempo_ronda=datos["info_Usuario"]["tiempo_ronda"]
        DiccRLPP=datos["info_Usuario"]["DiccRLPP"]
        Lista_Atril=datos["info_Usuario"]["Lista_Atril"]
        Usuario=datos["info_Usuario"]["Usuario"]
        Turnos_Disponibles=datos["info_Usuario"]["Turnos_Disponibles"]
        PTU=datos["info_Usuario"]["PTU"]
        LCO_Usuario=datos["info_Usuario"]["LCO_Usuario"]
        tiempo_jugador=datos["info_Usuario"]["tiempo_jugador"]
        HistorialCPU=datos["info_CPU"]["HistorialCPU"]
        DiccRLPP_CPU=datos["info_CPU"]["DiccRLPP_CPU"]
        PT_CPU=datos["info_CPU"]["PT_CPU"]
        fichas_CPU=datos["info_CPU"]["fichas_CPU"]
        contador_Turnos_CPU=datos["info_CPU"]["contador_Turnos_CPU"]
        LCO_CPU=datos["info_CPU"]["LCO_CPU"]
        Dificultad=datos["info_Tablero"]["Dificultad"]
        Dicc=datos["info_Tablero"]["Dicc"]
        CFT=datos["info_Tablero"]["CFT"]
        LCO=datos["info_Tablero"]["LCO"]
        Tiempo=datos["info_Tablero"]["Tiempo"]
        PrimerRonda=datos["info_Tablero"]["PrimerRonda"]
        Dicc_Bolsa=datos["info_Tablero"]["Dicc_Bolsa"]
        Dicc_Puntajes=datos["info_Tablero"]["Dicc_Puntajes"]
        aux_CCD=datos["info_Tablero"]["CCD"]
        Turno_Usuario=True
        for x in aux_CCD:
            CCD.add(tuple(x))
        diseño = [ [sg.Column((Layout_Tabla(Lista_Atril,Dicc_Bolsa,CFT,DiccRLPP))),
                    sg.Column(Layout_Columna()),
                    sg.Column(Layout_Columna_Historial(Usuario),key='Columna_Historial'),
                    sg.Column(Layout_Columna_Conf(Dicc_Puntajes,Dificultad,CFT),key='Columna_Conf')] ]
        window = sg.Window('Tablero',diseño ,location=(400,0),finalize=True)
        Update_Tablero2(window,Dicc)
        for coord in LCO:
            if coord in LCO_Usuario:
                window[coord].update(image_filename=DiccRLPP[Dicc[coord][0]][2],image_size=(40,40),image_subsample=5)
            elif coord in LCO_CPU:
                window[coord].update(image_filename=DiccRLPP_CPU[Dicc[coord][0]],image_size=(40,40),image_subsample=5)
        window['Historial_CPU'].update(HistorialCPU)
        window['PuntajeCPU'].update(str(PT_CPU))
        window['PuntajeUsuario'].update(str(PTU))
        window['Historial_Usuario'].update(HistorialUsuario)
    else:
        partida_carga=False
        UUsuario,Dificultad,Dicc_Puntajes,Dicc_Bolsa,Tiempo_Ronda,Tiempo,Lista_TP = Importar_Datos()
        Turno_Usuario = bool(random.getrandbits(1))
        LCO_Usuario=[] #Lista cordenadas ocuupadas usuario
        LCO_CPU=[]      #Lista cordenadas ocuupadas CPU
        DiccRLPP=rutas_letras(Dicc_Puntajes)  #Dicc Dicc_rutas_letras_puntaje_partida
        DiccRLPP_CPU=rutas_letras_CPU(Dicc_Puntajes)
        Lista_Atril = []
        Dicc = Generar_Dicc()
        CFT = 0
        CFT = Actualizar_CFT(CFT,Dicc_Bolsa) #Cantidad Fichas Totales
        fichas_CPU=""
        contador_Turnos_CPU=0
        PT_CPU=0                    #Puntaje Total CPU
        PTU = 0                     #Puntaje Total Usuario
        CCD=set()                   #Conjunto de Coordenadas  Disponibles
        LCO = []                    #Lista de Coordenadas Ocupadas
        Se_necesitan_dos = False
        Tiempo,tiempo_ronda=tiempo_dificultad(Dificultad)
        Turnos_Disponibles = 3
        Columna_Historial = True
        Desplegado = True
        diseño = [ [sg.Column((Layout_Tabla(Lista_Atril,Dicc_Bolsa,CFT,DiccRLPP))),
                    sg.Column(Layout_Columna()),
                    sg.Column(Layout_Columna_Historial(Usuario),key='Columna_Historial'),
                    sg.Column(Layout_Columna_Conf(Dicc_Puntajes,Dificultad,CFT),key='Columna_Conf')] ]
        window = sg.Window('Tablero',diseño ,location=(400,0),finalize=True)
        Dicc = Update_Tablero(window,Dicc)
        Dicc = Update_Tablero2(window,Dicc)
    tiemp_ant = ''
    Fin = False
    event1 = ''
    window['Columna_Conf'].update(visible=False)
    window['PuntosUsuario'].update('Puntos  ' + Usuario)
    if(Dificultad=="Dificil"):
        Dificil_se_juega=aleatorio_Dificil()
    else:
        Dificil_se_juega="Default"
    window.Refresh()
    tamaño_actual=window.Size
    while True:
        LPI = []                #Lista de Posiciones de Intercambio (Para Intecambiar fichas)
        LCOPR = []              #Lista de Coordenadas Ocupadas Por Ronda
        coords_Bonus = []
        puedo_intercambiar=True
        Boton_Intercambiar = False
        Se_Intercambio_Ficha = False
        if partida_carga==True:
            partida_carga=False
        else:
            tiempo_jugador=tiempo_ronda

        Mensaje_Turno(Turno_Usuario)
        while (Turno_Usuario):  #Mientras sea el turno del usuario:
            Palabra = ''
            event = window.Read(timeout=10,timeout_key='Reloj')[0]
            window['Tiempo'].update("{}:{}".format(((Tiempo//100)//60),((Tiempo//100)%60)))
            Tiempo -= 1
            tiempo_jugador = str(tiempo_jugador)
            window['Tiempo_Ronda'].update("00:{}".format(tiempo_jugador[0:2]))
            tiempo_jugador = int(tiempo_jugador)
            tiempo_jugador-=1
            #if (tamaño_actual != window.Size):
            #    tamaño_actual=window.Size
                #Aca deberian estar los cambios a la ventana que centrarian todo el contenido de esta.
            if event in (None, 'Salir'):
                event_popup = sg.popup_yes_no('Ey! estas saliendo en mitad de una partida\n¿Quieres posponerla?',title='Aviso',keep_on_top=True)
                if (event_popup == 'Yes'):
                    print("Pospone la partida")

                    GuardoPartida(Dificultad,DiccRLPP,Dicc,CFT,Usuario,Turnos_Disponibles,PTU,HistorialUsuario,LCO,Tiempo,DiccRLPP_CPU,PT_CPU,fichas_CPU,contador_Turnos_CPU,HistorialCPU,PrimerRonda,Lista_Atril,Dicc_Bolsa,Dicc_Puntajes,tiempo_ronda,list(CCD),LCO_Usuario,LCO_CPU,tiempo_jugador)
                else:
                    print("No la pospone y sale sin guardar")
                Fin = True
                puedo_intercambiar=False
                break

            if (((type(event) == int) or (type(event) == tuple)) and (Boton_Intercambiar == False)):
                if event1 == '':
                    event1 = event
                    if (type(event1) == int):
                        if ((Lista_Atril[event1] != '')):
                            #window[event1].update(button_color=('white','#57C3FD'))

                            window[event1].update(image_filename=DiccRLPP[Lista_Atril[event1]][1],image_size=(40,40),image_subsample=5)
                    elif Coord_Ocupada(LCOPR,event1):
                            window[event1].update(image_filename=DiccRLPP[Dicc[event1][0]][1],image_size=(40,40),image_subsample=5)
                    else :
                        Update_Infobox('No puedes interactuar con las fichas ya colocadas!','#5798FD',window) if Coord_Ocupada(LCO,event) else Update_Infobox('Primero selecciona una letra!','#5798FD',window)
                        event1 = ''
                else:
                    Acciones_Usuario(LCOPR,LCO,CCD,Dicc,Lista_Atril,event1,event,window,DiccRLPP)
                    event1 = ''

            elif (event == 'Validar') and (Boton_Intercambiar == False):
                Palabra = Validar(LCOPR,CCD,Dicc,Dificultad,PrimerRonda,Palabra,Dificil_se_juega,window)

            elif (((event == 'Terminar turno') or Se_Intercambio_Ficha) and (Boton_Intercambiar == False)):
                Bonus = Calcular_Bonus(LCOPR,Dicc_Puntajes,Dicc)
                PTU = TerminarTurno(LCOPR,LCO,CCD,Dicc,Lista_Atril,PTU,Palabra,Dificultad,Dificil_se_juega,Dicc_Puntajes,Dicc_Bolsa,CFT,Bonus,window,DiccRLPP)
                CFT = Actualizar_CFT(CFT,Dicc_Bolsa)
                Actualizar_LCO(LCOPR,LCO,LCO_Usuario)
                Actualizar_CCD(CCD,LCO)
                break

            elif (((event == "Intercambiar fichas") or (Boton_Intercambiar)) and (Turnos_Disponibles != 0)):
                CFT,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles = Boton_Intercambiar_Fichas(LCOPR,LCO,CCD,CFT,LPI,Dicc,Dicc_Bolsa,Lista_Atril,Boton_Intercambiar,Se_Intercambio_Ficha,Turnos_Disponibles,event,window,DiccRLPP)

            elif (event == 'Rotar') and (Desplegado):
                Update_Columna_Extra(Columna_Historial,window)
                Columna_Historial = not Columna_Historial

            elif (event == 'Mostrar'):
                if (Desplegado):
                    window['Columna_Historial'].update(visible=False)
                    window['Columna_Conf'].update(visible=False)
                    window['Mostrar'].update('>')
                else:
                    Update_Columna_Extra(not(Columna_Historial),window)
                    window['Mostrar'].update('<')
                Desplegado = not Desplegado

            if Infobox_Activa and (tiemp_ant != str(Tiempo)[3]):
                tiemp_ant = str(Tiempo)[3]
                if temp  == 0:
                    window['Infobox'].update('',text_color='Black',background_color='#A4A4A4')
                else:
                    temp = temp -1


        while (Turno_Usuario == False):
            contador_Turnos_CPU,fichas_CPU,CFT,PT_CPU=Acciones_CPU(window,CCD,LCO,Dicc,contador_Turnos_CPU,fichas_CPU,Dificultad,Dificil_se_juega,Dicc_Bolsa,CFT,Dicc_Puntajes,PT_CPU,DiccRLPP_CPU,LCO_CPU)
            break
        if Fin:
            break
        Update_Fichas_Colocadas(LCOPR,window,Dicc,DiccRLPP)
        Turno_Usuario = not Turno_Usuario
        window['CantFichas'].update('Cantidad de fichas: '+str(CFT))
    window.close()
    return(event)
#ProgramaPrincipal-------------
if __name__ == "__main__":
    sg.theme('DarkGrey2')
    genero_Tablero()
