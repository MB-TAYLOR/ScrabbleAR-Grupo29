from pattern.es import spelling,lexicon,parse

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NCS","NCP", "NNS","NP", "NNP","W"],#Borre el sus "NN" para que ande , sino , valida toda palabra  inexistente como "sus"
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}


def verificar_Medio_Dificil(palabra,existe):
    if palabra in spelling.keys() and palabra in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        if(parse(palabra).split("/")[1] in Tipo['adj']):
            existe=True
        elif(parse(palabra).split("/")[1] in Tipo['verb']):
            existe=True
    return(existe)

def verificar_Palabra(palabra,dificultad):
    existe=False
    palabra=palabra.lower()
    if(len(palabra)>=2):
        if (dificultad=="Facil"):
            if(parse(palabra).split("/")[1] in Tipo['sus']):
                existe=True
            elif (palabra in spelling.keys() or palabra in lexicon.keys()):
                existe=True
        elif(dificultad=="Medio"):
            existe=verificar_Medio_Dificil(palabra,existe)
        elif(dificultad=="Dificil"):
            existe=verificar_Medio_Dificil(palabra,existe)
    return(existe)
 #---------Porgrama Principal---
if __name__ == '__main__':
    print(verificar_Palabra("Correr","Facil"))
