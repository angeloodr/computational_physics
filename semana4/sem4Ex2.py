from vpython import *
box(pos=vector(0,0,-1),
    size = vector(5,5,0.5),
    color = color.red,
    opacity = 0.4)
particle = sphere(pos=vector(5,0,0),
                  radius = 0.3,
                  color=color.cyan,
                  make_trail = True)
v = vector(-0.5,0,0)
delta_t=0.05
t=0
while t<20:
    rate(100)
    particle.pos = particle.pos + v *delta_t
    t=t+delta_t