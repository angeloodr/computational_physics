import math
from vpython import *
import numpy as np

c1, c2, csol = 1000, 10**6, 70
planetaR = {'mercurio': 2440 * c1 , 'venus': 6052 *c1,'terra': 6371*c1, 'marte': 3386*c1, 'jupiter':69173*c1 , 'saturno': 57316*c1 , 'sun': 695500*csol}
orbitaR = {'mercurio': 57.9 *c2, 'venus': 108.2*c2,'terra': 149.6*c2, 'marte': 227.9*c2, 'jupiter':778.5*c2 , 'saturno': 1433.4*c2 , 'sun': 0 }
orbitaT = {'mercurio': 88.0 , 'venus': 224.7,'terra': 365.3, 'marte': 687.0, 'jupiter':4331.6 , 'saturno': 10759.2 , 'sun': 0 }
coresP= {'mercurio': color.green, 'venus': color.magenta ,'terra': color.blue, 'marte': color.red, 'jupiter':color.orange , 'saturno': color.cyan , 'sun': color.yellow}
delta_t, t = 0.5, 0
planetas = []

canvas(height=  600 , width = 1000)
for planeta in ['mercurio' , 'venus' , 'terra' , 'marte' , 'jupiter' , 'saturno' , 'sun' ]:
    planetas.append(sphere(pos=vector(orbitaR[planeta],0,0), radius = planetaR[planeta], color = coresP[planeta], make_trail = True, label=planeta))

while t<10000:
    rate(100)
    for planeta in planetas[:-1]:
        planeta.pos = vector(orbitaR[planeta.label]*math.cos(2*math.pi*t/orbitaT[planeta.label]),
                             orbitaR[planeta.label]*math.sin(2*math.pi*t/orbitaT[planeta.label]),
                             0)
    t=t+delta_t