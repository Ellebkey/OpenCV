'''
Se utiliza la tecla "v" para actualizar la imagen
'''

from cv2 import *
import cv2
import numpy as np


if __name__ == '__main__':

    def nothing(x):
        pass

    imagen = cv2.imread('foto.jpg')
    copia = imagen
    hsv = cv2.cvtColor(copia, cv2.COLOR_BGR2HSV)
    resultado = cv2.cvtColor(copia, cv2.COLOR_BGR2HSV)

    cv.NamedWindow('Imagen Filtrada',CV_WINDOW_AUTOSIZE)
    cv2.createTrackbar('Umbral','Imagen Filtrada',50,255,nothing)

    a = imagen.shape[0]
    b = imagen.shape[1]
    
    #metodo que actualizra la imagen cada vez que cambiamos el valor del umbral en el trackbar
    def update():
        #se actualiza valor del trackbar
        u = cv2.getTrackbarPos('Umbral','Imagen Filtrada')
        print u
        #filtro
        for y in range(0,b):
            for x in range(0,a):
                if hsv[x,y,2] >= u:
                    #Value obtiene el valor mas alto "255" si es mayor al umbral
                    resultado[x,y,2] = 255
                    #Y el minimo valor en saturacion para que sea completamente blanco
                    #Si no se pone esta linea, el color simplemente se oscurece o aclara
                    resultado[x,y,1] = 0
                else:
                    #En otro caso lo volvemos negro
                    resultado[x,y,2] = 0
        #se muestra la imagen ya filtrada
        final = cv2.cvtColor(resultado, cv2.COLOR_HSV2BGR)
        cv2.imshow('Imagen Filtrada', final)

    #Show
    update()
    while (1):
        ch = 0xFF & cv2.waitKey()
        if ch == ord(' '):
            update()
        if ch == 27:
            break
    cv2.destroyAllWindows()
