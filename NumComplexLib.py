from math import *

def SumaComplejos(n1,n2):
    sumareales = n1[0] + n2[0]
    sumaimaginarios = n1[1] + n2[1]
    return sumareales, sumaimaginarios

def ProductoComplejos(n1,n2):
    productoreal= (n1[0]*n2[0]) + (-1*(n1[1]*n2[1]))
    productoimaginario= (n1[0]*n2[1]) + (n1[1]*n2[0])
    return productoreal, productoimaginario

def RestaComplejos(n1,n2):
    restareales = n1[0] - n2[0]
    restaimaginarios = n1[1] - n2[1]
    return restareales, restaimaginarios

def DivisionComplejos(n1,n2):
    conjugado = -1 * n2[1]
    dividiendoreal = (n1[0]*n2[0]) + (-1*(n1[1]*conjugado))
    dividiendoimaginario = (n1[0]*conjugado) + (n1[1]*n2[0])
    divisortotal = (n2[0]**2) - (-1*(n2[1]**2))
    return dividiendoreal, dividiendoimaginario, divisortotal

def ModuloComplejos(n1):
    numraiz = (n1[0]**2)+(n1[1]**2)
    modulo = sqrt(numraiz)
    isInt= int(modulo) == modulo
    if isInt == True:
        return (int(modulo))
    else:
        return numraiz

def ConjugadoComplejos(n1):
    conjugado = -1*n1[1]
    return n1[0], conjugado

def FaseComplejos(n1):
    fase = degrees(atan(n1[1]/n1[0]))
    if n1[0] >= 0 and n1[1] >= 0:
        return fase
    elif n1[0] < 0 and n1[1] < 0:
        fase = fase + 180
        return fase
    elif n1[0] < 0 and n1[1] >= 0:
        fase = 180 - (-1*fase)
        return fase
    else:
        fase = 360 - (-1*fase)
        return fase

def RepresentacionPolar (n1):
    modulo = ModuloComplejos(n1)
    fase = FaseComplejos(n1)
    return modulo, fase

def RepresentacionCartesiana (n1):
    a = n1[0] * cos(radians(n1[1]))
    b = n1[0]* sin(radians(n1[1]))
    return a, b
