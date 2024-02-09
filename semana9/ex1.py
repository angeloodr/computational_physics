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
hN = 1.5
hCC = 1
hCduplaC = 1.1
hcunicaN = 0.8
natomos= 9

#INICIO determinante secular => mat
mat = np.zeros((natomos,natomos))
mat[0][0] = hN*beta0 #atomo N
mat[0][1] = hcunicaN*beta0   #lig N-C
mat[0][8] = hcunicaN*beta0  #lig N-C
mat[1][2] = hCduplaC*beta0 #lig c=c
mat[2][3] = hCC*beta0 #li C-c
mat[3][4] = hCC*beta0 
mat[3][8] = hCduplaC*beta0
mat[4][5] = hCduplaC*beta0
mat[5][6] = hCC*beta0
mat[6][7] = hCduplaC*beta0
mat[7][8] = hCC*beta0
mat = symmetrize(mat)
for linha in mat:
    print(linha)
#FIM determinante secular => mat

#calcule os níveis de energia, => autovalor
autovalor , autovetor =  np.linalg.eig(mat)
autovetor = autovetor.T #cada atomo está em uma coluna, a linha é ligada ao aotovalor de energia

#INICIO Esboce os orbitais moleculares Hinghesst Ocupies Molecular Orbiltal => falar o valor da energia)
#  e Lowest Unocupied Molecular Orbital. => falar o nivel de energia que não tem eletrons
index = np.argsort(autovalor)
autoval , autovec= [], []
for i in index:
    autoval.append(autovalor[i])
    autovec.append(autovetor[i])

print(autoval,'\n',autovec)
print('\n')
#FIM Esboce os orbitais moleculares Hinghesst Ocupies Molecular Orbiltal => falar o valor da energia)
#  e Lowest Unocupied Molecular Orbital. => falar o nivel de energia que não tem eletrons

#INICIO as ordens de ligações => c11*c12*numero de eletrons no nivel de energia (lig entre atomo entre os atomos 1 e 2) 
neletrons = [ 2, 2, 2, 2, 2 ] 
ordemDeLig = np.zeros(natomos-1)
for i in range(5):
    for j, linhaDosAutvec in enumerate (autovetor) :
        ordemDeLig[j] += (linhaDosAutvec[i] * linhaDosAutvec[i+1] * neletrons[i]) 
    #no fim das contas teremos uma matriz com ordem de ligação entre dois atomos em cada nivel de energia. 
    #podemos apresentar como um heatmap que basicamente replica a matriz. 

plt.plot(ordemDeLig)
plt.axes().set_xticks([0,1,2,3,4,5,6,7])
plt.show()
#FIM  

# INICIO as populações eletrônicas => vai ser o valor do da casela do auto vetor elevado ao quadrado. cada atomo tá numa coluna da
#        matriz dos autovetores
popEletronica = []
for lin in autovetor:
    popEletronica.append(sum(lin[:5]**2)) #nesse caso, cada linha é pra cada atomo
plt.plot(popEletronica)
#plt.colorbar()
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