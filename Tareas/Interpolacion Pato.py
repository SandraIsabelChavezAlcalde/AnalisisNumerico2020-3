##Tarea por Sandra Isabel Chavez
import numpy as np
import scipy.interpolate as sp
import cv2
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt

########Extraer puntos de la imagen##########3
imagen = cv2.imread('pato.png')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
contornos, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,contornos,1,(103,123,252),3)
puntos= contornos[1]
print('Numero de puntos:',len(puntos))
cv2.imshow('Contorno del Pato',imagen)
if cv2.waitKey(5000) == ord('a'):
   print ("###############Pasando a interpolacion########################")
######################################


#############Division 1###################33
xa =  [0 ,1   ,2 ,4   ,6 ,7   ,10,12.5,15  ,20,22  ,23]
ya =  [12,12.5,13,14.7,14,13.5,14,14  ,13.5,11,10.7,10.3]
plt.plot(xa,ya)

x = np.linspace( min(xa), max(xa), 1000)
tck = sp.splrep(xa, ya, s=0)
ysp = sp.splev(x, tck)
###############################################

# Division 2
xl =  [0,0.5  ,1.5 ,2.2 ,3 ,3.5 ,6.5   ,7   ,8   ,9 ]
yl =  [12,11.5,11.5,11.5,12,11.7,11.7  ,11.3,10.2,10]
plt.plot(xl,yl)

xx = np.linspace( min(xl), max(xl), 1000)
tck = sp.splrep(xl, yl, s=0)
ysp = sp.splev(xx, tck)
plt.plot(xl,yl,'o')
plt.plot(xx,ysp)

###############################################
# Division 3
x2 = [7.5,7.6,8  ,8.3,8.7,9 ]
y2 = [0.3,0.8,1.5,4  ,8  ,10]
plt.plot(x2,y2)

xx = np.linspace( min(x2), max(x2), 1000)
tck = sp.splrep(x2, y2, s=0)
ysp = sp.splev(xx, tck)
plt.plot(x2,y2,'o')
plt.plot(xx,ysp)
###############################################


# Division 4
x3 = [7.5, 8.1,9.2,9.8,10.9,11.5,12.5,12.7,13.5,13.6,14.2,15,16 ,18.4,19 ,21.7,23]
y3 = [0.3,0   ,0.4,1  ,1.7 ,3   ,4  ,5.4,6.3   ,7.6 ,8.8,8.7,8.4,9.6 ,9.6,10  ,10.3]
plt.plot(x3,y3)


xx = np.linspace( min(x3), max(x3), 1000)
tck = sp.splrep(x3, y3, s=0)
ysp = sp.splev(xx, tck)
plt.plot(xl,yl,'o')
plt.plot(xx,ysp)
###############################################
print("Numero de puntos luego de interpolacion: ",len(xl)+len(x2)+len(x3))
plt.axis([0,25,0,15])
plt.title("Imagen Luego de Interpolación")
plt.show()
