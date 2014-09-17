from cv2 import *
import cv2
import numpy as np

if __name__ == '__main__':

    imagen = cv2.imread('foto.jpg')
    copia = imagen
    #en lugar de copiar resultado de hsv las creo por separado sino hay un desface en los pixeles
    hsv = cv2.cvtColor(copia, cv2.COLOR_BGR2HSV)
    resultado = cv2.cvtColor(copia, cv2.COLOR_BGR2HSV)

    a = imagen.shape[0]
    b = imagen.shape[1]

    p=[hsv[0,0,0]]*9


    #Filtro
    for y in range(1,b-1):
        for x in range(1,a-1):
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

            p.sort()  
            #asignamos el valor minimo, mayor si se quiere el maximo
            resultado[x,y,2]=p[0]

    #Transformamos de vuelta de HSV a RGB para mostrar el resultado del filtro
    final = cv2.cvtColor(resultado, cv2.COLOR_HSV2BGR)

    cv.NamedWindow('Imagen Original',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Original', imagen)
    cv.NamedWindow('Imagen Filtrada',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Filtrada', final)
    cv2.waitKey()
