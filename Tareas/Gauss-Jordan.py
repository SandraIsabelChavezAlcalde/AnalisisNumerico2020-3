'''Adaptado y mejorado por Sandra Chavez '''


# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

import numpy as np

# INGRESO
operaciones=0
A = np.array([[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3],[1,1,3,3,3,3,3,3,3,3]])

B = np.array([[2],[2],[4],[2],[2],[2],[6],[2],[2],[1]])

# PROCEDIMIENTO
casicero = 1e-15 # Considerar como 0
# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

# Matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    operaciones +=1
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
        operaciones +=1
AB1 = np.copy(AB)

# eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i+1
    operaciones +=1
    for k in range(adelante,n,1):
        operaciones +=1
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

# elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    operaciones +=1
    for k in range(atras,0-1,-1):
        operaciones +=1
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    # diagonal a unos
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcolumna])
X = np.transpose([X])


# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminacion hacia adelante')
print(AB2)
print('eliminación hacia atrás')
print(AB)
print('solución de X: ')
print(X)
print('Operaciones totales:')
print(operaciones)

''' Referencias
Adaptado de :
http://blog.espol.edu.ec/analisisnumerico/3-4-gauss-jordan-metodo/
 '''

