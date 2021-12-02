from Mi_libreria import *
from skimage import io

MiImagen=io.imread("pereira.jpg")/255
plt.figure("Imagen de Pereira")
plt.imshow(MiImagen, vmin=0, vmax=1)
ImgInvertida=255-MiImagen
plt.figure("Imagen Invertida")
plt.imshow(ImgInvertida, vmin=0, vmax=1)
print(MiImagen.shape) # Tamaño de la imagen 
print(MiImagen)
plt.show()

