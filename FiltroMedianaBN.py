from cv2 import *
import cv2
import numpy as np



if __name__ == '__main__':
    #imread crea una matriz con los valores de cada pixel de la imagen
    #La imagen a color tiene 3 valores (RGB)
    #lo converti a escala de grices porque asi cada pixel tiene un valor y es mas facil asi :D
    imagen = cv2.imread('foto.jpg',0)
    print imagen
    resultado = imagen[:]

    #obtenemos el ancho y largo para los ciclos
    a = imagen.shape[0]
    b = imagen.shape[1]

    cv.NamedWindow('Imagen Original',CV_WINDOW_AUTOSIZE)
    cv2.imshow('Imagen Original', imagen)

    #se copia la imagen
    for x in range(a):
        for y in range(b):
            resultado[x,y]=imagen[x,y] 

    
    pixel=[imagen[0,0]]*25
 
    #aqui es donde se obtienen los pixeles alrededor del actual para despues ordenarlos y obtener el de la mitad
    for x in range(2,a-2):
        for y in range(2,b-2):
            pixel[0] = imagen[x-2,y+2]
            pixel[1] = imagen[x-1,y+2]
            pixel[2] = imagen[x,y+2]
            pixel[3] = imagen[x+1,y+2]
            pixel[4] = imagen[x+2,y+2]
            pixel[5] = imagen[x-2,y+1]
            pixel[6] = imagen[x-1,y+1]
            pixel[7] = imagen[x,y+1]
            pixel[8] = imagen[x+1,y+1]
            pixel[9] = imagen[x+2,y+1]
            pixel[10] = imagen[x-2,y]
            pixel[11] = imagen[x-1,y]
            pixel[12] = imagen[x,y]
            pixel[13] = imagen[x+1,y]
            pixel[14] = imagen[x+2,y]
            pixel[15] = imagen[x-2,y-1]
            pixel[16] = imagen[x-1,y-1]
            pixel[17] = imagen[x,y-1]
            pixel[18] = imagen[x+1,y-1]
            pixel[19] = imagen[x+2,y-1]
            pixel[20] = imagen[x-2,y-2]
            pixel[21] = imagen[x-1,y-2]
            pixel[22] = imagen[x,y-2]
            pixel[23] = imagen[x+1,y-2]
            pixel[24] = imagen[x+2,y-2]

            pixel.sort()  #se ordena los valores
            resultado[x,y]=pixel[12] #asignamos al pixel actual el valor que queda enmedio de todos ya ordenados

    
    #se muestra imagen ya filtrada
    cv.NamedWindow('Imagen Filtro Mediana', CV_WINDOW_AUTOSIZE)
    cv2.imshow('<Imag></Imag>en Filtro Mediana', resultado)
    cv2.waitKey()