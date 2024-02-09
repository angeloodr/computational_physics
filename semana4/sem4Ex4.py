from vpython import *
from math import sin, cos

def movHor (x, t, v0x):
    return x + v0x*t

def movVer(y, t, v0y, a=-9.8):
    return y + v0y*t + (a/2)*(t**2)

delta_t=0.05
t=0
v0=10
x, y = 0,0

box(pos=vector(0,0,-1),
    size = vector(5,5,0.5),
    color = color.red,
    opacity = 0.4)

particle = sphere(pos=vector(x,y,0),
                  radius = 2,
                  color=color.cyan,
                  make_trail = True)

theta = float(input("insira o valor do angulo de lançamento: "))
v0x = v0*cos(theta)
v0y = v0*sin(theta)

while t<5:
    rate(100)
    x=movHor(x,t,v0x)
    y=movVer(y,t,v0y)
    particle.pos = vector(x,y,0)
    t=t+delta_t