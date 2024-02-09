import numpy as np
import matplotlib.pyplot as plt

def symmetrize(a):
    """
    Return a symmetrized version of NumPy array a.

    Values 0 are replaced by the array value at the symmetric
    position (with respect to the diagonal), i.e. if a_ij = 0,
    then the returned array a' is such that a'_ij = a_ji.

    Diagonal values are left untouched.

    a -- square NumPy array, such that a_ij = 0 or a_ji = 0, 
    for i != j.
    """
    return a + a.T - np.diag(a.diagonal())

beta0 = -2.5 #eV
hC = 0
hCunicaC = 0.9
hCduplaC = 1.1
hOdoise = 2
hCunicaO = 0.8

natomos= 5

#INICIO determinante secular => mat
mat = np.zeros((natomos,natomos))
'''cada um desses parametros mostram a ligação entre os coeficientes das
ligações dos atomos e também dos atomos isolados para formação da matriz secular 
A ideia aqui é formar a matriz triangular superior com todos os atomos e depois só simetrizar'''
mat[0][0] = hOdoise*beta0 #O0
mat[0][1] = hCunicaO*beta0  #O0C1
mat[0][4] = hCunicaO*beta0  #O0C4

mat[1][1] = hC*beta0 #C1
mat[1][2] = hCduplaC*beta0 #C1C2

mat[2][2] = hC*beta0 #C2
mat[2][3] = hCunicaC*beta0 #C2C3

mat[3][3] = hC*beta0 #C3
mat[3][4] = hCduplaC*beta0 #C3C4

mat[4][4] = hC*beta0 #C4

mat = symmetrize(mat)
for linha in mat:
    print(linha)
#FIM determinante secular => mat

#calcule os níveis de energia, => autovalor
autovalor , autovetor =  np.linalg.eig(mat) #calculo dos autovalores e autovetores utilizando o metodo do numpy
print(autovalor) # vetor dos niveis de energia da molecula

autovetor = autovetor.T #Essa transposição é só para cada atomo ficar em uma coluna e cada linha ser relacionada
                        # ao aotovalor de energia. Importante para organizar os vetores de acordo com os niveis de ene

#INICIO Esboce os orbitais moleculares Hinghesst Ocupies Molecular Orbiltal => falar o valor da energia)
#  e Lowest Unocupied Molecular Orbital. => falar o nivel de energia que não tem eletrons
index = np.argsort(autovalor)
autoval , autovec= [], []
for i in index:
    autoval.append(autovalor[i])
    autovec.append(autovetor[i])

print(autoval) #autovalores ordenados
print(autovec) #autovetores ordenados em relação aos niveis crescentes de energia 

#FIM Esboce os orbitais moleculares Hinghesst Ocupies Molecular Orbiltal => falar o valor da energia)
#  e Lowest Unocupied Molecular Orbital. => falar o nivel de energia que não tem eletrons

#INICIO as ordens de ligações => c11*c12*numero de eletrons no nivel de energia (lig entre atomo entre os atomos 1 e 2) 
neletrons = [ 2, 2, 2 ] 
ordemDeLig = np.zeros(natomos-1)
for i in range(len(neletrons)):
    for j, linhaDosAutvec in enumerate (autovetor) :
        ordemDeLig[j] += (linhaDosAutvec[i] * linhaDosAutvec[i+1] * neletrons[i]) 
    # A ordem de ligação é calculada multiplicando os valores dos autoveltores relacionados aos atomos que fazem a ligação e o
    # numero de életrons que temos temos em cada nivel de energia da molecula. Vamos acumulando esses valores numa variável que indica
    # o valor da ordem de ligação entre os átomos nos diferentes níveis de energia. 

plt.plot(ordemDeLig)
plt.show()
#FIM  

# INICIO as populações eletrônicas => vai ser o valor do da casela do auto vetor elevado ao quadrado.
popEletronica = []
for lin in autovetor:
    popEletronica.append(sum(lin[:len(neletrons)]**2)) #nesse caso, cada linha é pra cada atomo
    # aqui estamos somando os valores da linha dos autovetores correspondente a cada átomo. 
    # Somente estamos considerando os valores cujo quais correspondem aos níveis de energia ocupados
plt.plot(popEletronica)
plt.show()
#FIM 

#determinante secular => mat
#calcule os níveis de energia, => autovalor
#DIRETO NO CANVA diagrama de níveis & preenchimento eletrônico destes níveis => 
#       considerar que a molecula é um atomo e prencher os niveis de energia de forma normal com os 9 eletrons
#       cada nivel de energia preenchese com 2 eletrons
#as ordens de ligações => c11*c12*numero de eletrons no nivel de energia (lig entre atomo entre os atomos 1 e 2) 
# as populações eletrônicas => vai ser o valor do da casela do auto vetor elevado ao quadrado. cada atomo tá numa coluna da
#        matriz dos autovetores
#Esboce os orbitais moleculares Hinghesst Ocupies Molecular Orbiltal => falar o valor da energia)
#  e Lowest Unocupied Molecular Orbital. => falar o nivel de energia que não tem eletrons