# variáveis de estado x e y e t
import math

# variaveis e constantes primarias
x, y, t = 0, 0, 0
theta = math.pi/3
v_i = 10 #m/s
passos  = 5000
dt = 0.0001

#variaveis e constantes secundárias
v_iy = v_i * math.sin(theta)
v_ix = v_i * math.cos(theta)

# funções do programa
def posicaoX(x, t, v_x = v_ix):
    return v_x * t + x

def posicaoY(y, t, v_y = v_iy, g=-9.8):
    return y + v_y * t + ((g/2) * t**2)

def posicaoRelativaY(x, y, phi=math.pi/6):
    return y-x*math.tan(phi)

# calculo das variáveis no tempo
for step in range(passos):
    t = t + step * dt
    x = posicaoX(x,t)
    y = posicaoY(y,t)
    posRel = posicaoRelativaY(x,y)
    print(" x= ",x," y= ",y," t=",t, " posY relativa = ",posRel)
    if posRel < 0:
        print('O projetíl atinge o chão em t=',t-(step*dt))
        break