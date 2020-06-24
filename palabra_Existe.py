import itertools as it
from pattern.es import spelling,lexicon,parse

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NCS","NCP", "NNS","NP", "NNP","W"],#Borre el sus "NN" para que ande
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}


def verificar_Medio_Dificil(palabra,existe):
    if palabra in spelling.keys() and palabra in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        for x in range(len(Tipo['verb'])):
            if(x <= (len(Tipo['adj'])-1) ):
                if(parse(palabra).split("/")[1]==Tipo['adj'][x]):
                    existe=True
            if(parse(palabra).split("/")[1]==Tipo['verb'][x]):
                existe=True
    return(existe)

def verificar_Palabra(palabra,dificultad):
    existe=False
    palabra=palabra.lower()
    if(len(palabra)>=2):
        if (dificultad=="Facil"):
            for x in range(len(Tipo['sus'])):
                if(parse(palabra).split("/")[1]==Tipo['sus'][x]):
                    existe=True
                elif (palabra in spelling.keys() or palabra in lexicon.keys()):
                        existe=True
        elif(dificultad=="Medio"):
            verificar_Medio_Dificil(palabra,existe)
        elif(dificultad=="Dificil"):
            verificar_Medio_Dificil(palabra,existe)
    return(existe)


 #---------Porgrama Principal---
if __name__ == '__main__':
    print(verificar_Palabra("si","Facil"))
