from vpython import color, sphere, vector
from math import pi, sin, cos
import numpy as np

circleradius = 10
sphereradius = 1

for theta in np.linspace(0,2*pi, 14):
    sphere(pos = vector(circleradius*cos(theta),circleradius*sin(theta),0) , radius = sphereradius, color = vector(1,1,0))

    sphere(pos = vector(0,circleradius*cos(theta),circleradius*sin(theta)) , radius = sphereradius, color = vector(1,0,1))

    sphere(pos = vector(circleradius*sin(theta),0,circleradius*cos(theta)) , radius = sphereradius, color = vector(0,1,1))
