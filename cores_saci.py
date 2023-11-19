from typing import List

cor= list()
amostra = list()

def addbranco():
    cor.append("white")
    amostra.append("branco")

def addvermelho():
    cor.append("red" )
    amostra.append("vermelho")

def addazul():
    cor.append("blue")
    amostra.append("azul")
def addrosa():
    cor.append("pink")
    amostra.append("rosa")
def addverde():
    cor.append("green")
    amostra.append("verde")
def addamarelo():
    cor.append("yellow")
    amostra.append("amarelo")
def addroxo():
    cor.append("purple")
    amostra.append("roxo")
def addturquesa():
    cor.append("turquoise")
    amostra.append("lilas")
def addlaranja():
    cor.append("orange")
    amostra.append("laranja")
def addmarrom():
    cor.append("brown")
    amostra.append("marrom")
def addvioleta():
    cor.append("violet")
    amostra.append("violeta")
def addpreto():
    cor.append("black")
    amostra.append("preto")

def apagar():

    if len(cor) > 0:
        for c in range(0,len(cor)) :
            cor.pop()
            amostra.pop()

def getcores():
    return (cor)

def getamostra():
    return(amostra)

