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


    pixel=[hsv[0,0,0]]*25

    #Filtro
    for x in range(2,a-2):
        for y in range(2,b-2):
            #Se utiliza el indice 2 del tercer valor ya que ese coresponde al Value
            pixel[0] = hsv[x-2,y+2,2]
            pixel[1] = hsv[x-1,y+2,2]
            pixel[2] = hsv[x,y+2,2]
            pixel[3] = hsv[x+1,y+2,2]
            pixel[4] = hsv[x+2,y+2,2]
            pixel[5] = hsv[x-2,y+1,2]
            pixel[6] = hsv[x-1,y+1,2]
            pixel[7] = hsv[x,y+1,2]
            pixel[8] = hsv[x+1,y+1,2]
            pixel[9] = hsv[x+2,y+1,2]
            pixel[10] = hsv[x-2,y,2]
            pixel[11] = hsv[x-1,y,2]
            pixel[12] = hsv[x,y,2]
            pixel[13] = hsv[x+1,y,2]
            pixel[14] = hsv[x+2,y,2]
            pixel[15] = hsv[x-2,y-1,2]
            pixel[16] = hsv[x-1,y-1,2]
            pixel[17] = hsv[x,y-1,2]
            pixel[18] = hsv[x+1,y-1,2]
            pixel[19] = hsv[x+2,y-1,2]
            pixel[20] = hsv[x-2,y-2,2]
            pixel[21] = hsv[x-1,y-2,2]
            pixel[22] = hsv[x,y-2,2]
            pixel[23] = hsv[x+1,y-2,2]
            pixel[24] = hsv[x+2,y-2,2]

            promedio = (sum(pixel))/25
 
            #asignamos al pixel actual el valor resultante del promedio
            resultado[x,y,2] = promedio 

    #Transformamos de vuelta de HSV a RGB para mostrar el resultado del filtro
    final = cv2.cvtColor(resultado, cv2.COLOR_HSV2BGR)

    #Show
    cv.NamedWindow('Imagen Original',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Original', imagen)
    cv.NamedWindow('Imagen Filtrada',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Filtrada', final)
    cv2.waitKey()
