''' Adaptado por Sandra Chavez '''


import numpy as np
import random
#Aqui se generan los arreglos que componen la matriz
def generarArreglos(n): 
    matriz= ([[0 for j in range(n)] for i in range(n)])
    res= ([0 for i in range(n)])
    return np.array(matriz), np.array(res)


#Aqui se genera la matriz
def generarMatrices():
    for i in range (n):
        for j in range (n):
            matriz[i][j]=round(random.randint(1,10),4)
        res[i]=round(random.randint(1,10),4)

#Aqui se evaluan los valores de la matriz por le método de Cramer
def sol_cramer(A,B,R=[]):
    operaciones=0
    mAuxiliar = A.copy() 

    for i in range(0,len(B)):
        for j in range(0,len(B)):
            operaciones +=1
            mAuxiliar[j][i]=B[j]
            if i>0:
                mAuxiliar[j][i-1]=A[j][i-1]
                operaciones +=1
        R.append(round(np.linalg.det(mAuxiliar)/np.linalg.det(A),8))
    return R,operaciones

#ejercicio 10x10
matriz=np.array(([[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3]]))
res= np.array(([2,2,4,2,2,2,6,2,2,1]))
n=10

 
print("resolver A*x = B")
print(np.array(matriz), "X = ", res)

print("Solucion por Cramer")
resultado, op = sol_cramer(matriz,res)
print(resultado)
print("Operaciones totales",op)

'''
referencias:
    algoritmo sacado de -https://youtu.be/DQN4tjbGDfw '''