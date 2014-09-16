from cv2 import *
import cv2
import numpy as np



if __name__ == '__main__':

    imagen = cv2.imread('foto.jpg')
    copia = imagen
    #Se debe converir de BGR a HSV en lugar de RGB 
    #porque por alguna razon opencv coloca mal los indices
    hsv = cv2.cvtColor(copia, cv2.COLOR_BGR2HSV)
    resultado = hsv[:]

    a = imagen.shape[0]
    b = imagen.shape[1]

    
    for x in range(a):
        for y in range(b):
            resultado[x,y]=hsv[x,y]


    p=[hsv[0,0,0]]*25

    
    #Filtro
    for x in range(1,a-1):
        for y in range(1,b-1):
            #Se utiliza el indice 2 del tercer valor ya que ese coresponde al Value
            p[0] = hsv[x-1,y-1,2]
            p[1] = hsv[x,y-1,2]
            p[2] = hsv[x+1,y-1,2]
            p[3] = hsv[x-1,y,2]
            p[4] = hsv[x,y,2]
            p[5] = hsv[x+1,y-1,2]
            p[6] = hsv[x-1,y+1,2]
            p[7] = hsv[x,y+1,2]
            p[8] = hsv[x+1,y+1,2]

            promedio = [p[0],p[1],p[1],p[2],p[3],p[3],p[4],p[4],p[4],p[4],p[5],p[5],p[6],p[7],p[7],p[8]]
            promedio.sort()

            #asignamos al pixel actual el valor que queda enmedio de todos ya ordenados
            resultado[x,y,2] = promedio[7] 

    #Transformamos de vuelta de HSV a RGB para mostrar el resultado del filtro
    final = cv2.cvtColor(resultado, cv2.COLOR_HSV2BGR)

    #Show
    cv.NamedWindow('Imagen Original',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Original', imagen)
    cv.NamedWindow('Imagen Filtrada',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Filtrada', final)
    cv2.waitKey()
