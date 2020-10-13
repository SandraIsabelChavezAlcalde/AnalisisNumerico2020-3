#Realizado por Sandra Chavez, Santiago Romero, Ricardo Bernal

#Librerias#
import cv2
import numpy as np
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt


########Extraer puntos de la imagen##########3
imagen = cv2.imread('pp.png')
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
_,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

contornos, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contornos,1,(252,126,103),3)
puntos= contornos[1]
print (puntos)
print('Numero de puntos:',len(puntos))
cv2.imshow('Contorno del perro',imagen)
x=[734]
y=[734]
for i in range (len(puntos)):
    x.append(puntos[i][0][0])

for i in range (len(puntos)):
    y.append(puntos[i][0][1])



if cv2.waitKey(5000) == ord('a'):
   print ("###############Pasando a interpolacion########################")
######################################
plt.scatter(x,y)
plt.show()