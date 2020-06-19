import itertools as it
from pattern.es import spelling,lexicon,parse
import json

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}
##Verificar si la palabra es verbo o adjetivo parse() -> VB - JJ Dificultad -> Medio,Dificil
#if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Facil (Existe en lexicon y spelling) Hacer parse , si no es sut hacerla valida , si es sustantivo verificar si esta en spellin o lexicon si esta en alguna de las 2 es valida sino , es invalida


def palabra_larga(lista_palabras):
    max=0
    palabra_max=""
    for x in lista_palabras:
        if(len(x)>=max):
            max=len(x)
            palabra_max=x
    return(palabra_max)
def Medio_Dificil(i,palabras_existentes):
    if i in spelling.keys() and i in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        for x in range(len(Tipo['verb'])):
            if(x <= (len(Tipo['adj'])-1) ):
                if(parse(i).split("/")[1]==Tipo['adj'][x]):
                    palabras_existentes.append(i)
            if(parse(i).split("/")[1]==Tipo['verb'][x]):
                palabras_existentes.append(i)
def existe_palabra(letras,dificultad):
    palabras = set()
    print(letras)
    for i in range(2,len(letras)+1):
        palabras.update((map("".join, it.permutations(letras, i))))
    palabras_existentes=[]
    for i in palabras:
        if (dificultad=="Facil"):
            for x in range(len(Tipo['sus'])):
                if(parse(i).split("/")[1]!=Tipo['sus'][x]):
                    palabras_existentes.append(i)
                elif (i in spelling.keys() or i in lexicon.keys()):
                        palabras_existentes.append(i)
        elif(dificultad=="Medio"):
            Medio_Dificil(i,palabras_existentes)
        elif(dificultad=="Dificil"):
            Medio_Dificil(i,palabras_existentes)
    print(palabras)
    print(palabras_existentes)
    return(palabra_larga(palabras_existentes))


  #---------Porgrama Principal---
if __name__ == '__main__':
    print(existe_palabra("rrcroe","Medio"))
