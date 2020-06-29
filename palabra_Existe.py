from pattern.es import spelling,lexicon,parse

Tipo= {'adj':["AO", "JJ","AQ","DI","DT"],
'sus':["NC", "NCS","NCP", "NNS","NP", "NNP","W"],#Borre el sus "NN" para que ande , sino , valida toda palabra  inexistente como "sus"
'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG", "VSI","VSN", "VSP","VSS" ]
}
def verificar_Facil(palabra,existe):
    if (i in spelling.keys() or i in lexicon.keys()):
        if(parse(i).split("/")[1] in Tipo['sus']):
            existe=True
        elif(parse(i).split("/")[1] in Tipo['adj']):
            existe=True
        elif(parse(i).split("/")[1] in Tipo['verb']):
            existe=True
        else:
            existe=False
    else:
        existe=False
    return(existe)
def verificar_Medio(palabra,existe):
    if palabra in spelling.keys() and palabra in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        print("Pase")
        if(parse(palabra).split("/")[1] in Tipo['verb']):
            existe=True
        elif(parse(palabra).split("/")[1] in Tipo['sus']):
            existe=True
        else:
            existe=False
    else:
        existe=False
    return(existe)
def verificar_Dificil(palabra,existe,Dificil_elegido):
    if palabra in spelling.keys() and palabra in lexicon.keys(): #Dificultad -> Medio(Sea adjetivo o verbo)
        if(Dificil_elegido=="adj"):
            if(parse(palabra).split("/")[1] in Tipo['adj']):
                existe=True
        elif(Dificil_elegido =="verb"):
            if(parse(palabra).split("/")[1] in Tipo['verb']):
                existe=True
        elif(Dificil_elegido=="sus"):
            if(parse(palabra).split("/")[1] in Tipo['sus']):
                existe=True
        else:
            existe=False
    else:
        existe=False
    return(existe)

def verificar_Palabra(palabra,dificultad,Dificil_elegido):
    existe=False
    palabra=palabra.lower()
    if(len(palabra)>=2):
        if (dificultad=="Facil"):
            if(parse(palabra).split("/")[1] in Tipo['sus']):
                existe=True
            elif (palabra in spelling.keys() or palabra in lexicon.keys()):
                existe=True
        elif(dificultad=="Medio"):
            existe=verificar_Medio(palabra,existe)
        elif(dificultad=="Dificil"):
            existe=verificar_Dificil(palabra,existe,Dificil_elegido)
    return(existe)
 #---------Porgrama Principal---
if __name__ == '__main__':
    print(verificar_Palabra("feo","Dificil","adj"))
