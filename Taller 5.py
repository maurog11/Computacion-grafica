import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


# Punto 1
def subimg(pos, title, img):
    grilla = int(str(22) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def brillo(img, fac):
    return img * fac + (1 - fac)

imagen = io.imread('tarde.jpg') / 255

con = np.copy( imagen )

subimg(1, 'Imagen Original', imagen)
subimg(2, 'Brillo 0.2', brillo( con, 0.2 ))
subimg(3, 'Brillo 0.5', brillo( con, 0.5 ))
subimg(4, 'Brillo 0.8', brillo( con, 0.8 ))

plt.show()

# Punto 2 
def subimg(pos, title, img):
    grilla = int(str(33) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def brillo(img, fac):
    return img * fac + (1 - fac)

def canal(img, can, fac):
    img_2 = np.copy(img)
    for i in range(0,3):
        if i != can:
            img_2[:,:,i] = 0

    return brillo(img_2, fac)

imagen = io.imread('tarde.jpg') / 255

imagen_2 = np.copy( imagen )

subimg(1, 'Canal Rojo-Brillo 0.2', canal( imagen_2, 0, 0.2 ))
subimg(2, 'Canal Rojo-Brillo 0.5', canal( imagen_2, 0, 0.5 ))
subimg(3, 'Canal Rojo-Brillo 0.8', canal( imagen_2, 0, 0.8 ))
subimg(4, 'Canal Verde-Brillo 0.2', canal( imagen_2, 1, 0.2 ))
subimg(5, 'Canal Verde-Brillo 0.5', canal( imagen_2, 1, 0.5 ))
subimg(6, 'Canal Verde-Brillo 0.2', canal( imagen_2, 1, 0.8 ))
subimg(7, 'Canal Azul-Brillo 0.2', canal( imagen_2, 2, 0.2 ))
subimg(8, 'Canal Azul-Brillo 0.5', canal( imagen_2, 2, 0.5 ))
subimg(9, 'Canal Azul-Brillo 0.8', canal( imagen_2, 2, 0.8 ))

plt.show()

# Punto 3 
def subimg(pos, title, img):
    grilla = int(str(22) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def contra(img, fac):
    return img + fac

imagen = io.imread('tarde.jpg') / 255

con = np.copy( imagen )

subimg(1, 'Imagen Original', imagen)
subimg(2, 'Contraste 1', contra( con, 0.1 ))
subimg(3, 'Contraste 2', contra( con, 0.2 ))
subimg(4, 'Contraste 3', contra( con, 0.3 ))

plt.show()

# Punto 4 
image = cv2.imread('tarde.jpg')
imageOut = image[60:220,280:480]

cv2.imshow('Imagen entrada',image)
cv2.imshow('Imagen salida',imageOut)
cv2.waitKey(0)

# Punto 5 
img = cv2.imread('tarde.jpg',0)
ret,var1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,var2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
 
titles = ['Imagen Original','Binarizada','Bina_Inv']
images = [img, var1, var2]
miArray = np.arange(3)
for i in miArray:
  plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()

# Punto 6
image = cv2.imread('tarde.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] #filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),45,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen entrada',image)
cv2.imshow('Imagen salida',imageOut)
cv2.waitKey(0)

# Punto 7
def Mihisto(imagen):
    image_histo = np.trunc(np.around(imagen *255,0))
    return (image_histo)
# Llamado histograma
image_histo = Mihisto(imagen)
plt.figure("Histograma")
plt.hist(image_histo.ravel(), 256, [0,256])
plt.show()