'''
neste progama calculamos a integral da função I_I0 por meio do metodo de gauss
nesse método utilizamos amostragem de forma não homegênea da função para realizar o calculo
'''

xmin, xmax = -5, 5
Ngausiana = 50
import math
from gaussxw import gaussxw

def varU ( x, z=3, lamb=1): 
    return x * (2/(lamb*z))**(1/2)

def funcC (t):
    return math.cos(1/2 * math.pi * t**2)

def funcS (t):
    return math.sin(1/2 * math.pi * t**2)

def integra(func, liminf = varU(xmin), limsup = varU(xmax)):
    x, w = gaussxw(Ngausiana)
    xp = 0.5*(limsup- liminf)*x + 0.5*(limsup- liminf)
    wp = 0.5*(limsup - liminf)*w
    soma = 0
    for k in range(Ngausiana):
        soma+= wp[k]*func(xp[k])
    
    return soma

def I_I0 ():
    return ((1/8) *((2* integra(funcC) + 1)**2 + (2*integra(funcS)+ 1)**2))

print(I_I0())

