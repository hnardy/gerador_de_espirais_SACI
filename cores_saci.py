from typing import List

cor= list()

def addbranco():
    cor.append("white")


def addvermelho():
    cor.append("red" )

def addazul():
    cor.append("blue")

def addrosa():
    cor.append("pink")

def addverde():
    cor.append("green")

def addamarelo():
    cor.append("yellow")

def addroxo():
    cor.append("purple")

def addturquesa():
    cor.append("turquoise")

def addlaranja():
    cor.append("orange")

def addmarrom():
    cor.append("brown")

def addvioleta():
    cor.append("violet")

def addpreto():
    cor.append("black")


def apagar():
    for c in range(0,len(cor)) :
        cor.pop()

def getcores():
    return (cor)


