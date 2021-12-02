from Mi_libreria import *
from skimage import io

ImagenRGB = io.imread("pereira.jpg")/255

print("Tamaño de la imagen",ImagenRGB.shape)

plt.figure("Figura RGB")

ImagenOriginal = np.copy(ImagenRGB)
plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(ImagenOriginal)

ImagenRed = np.copy(ImagenRGB)
ImagenRed[:,:,1]=0
ImagenRed[:,:,2]=0
plt.subplot(2,2,2)
plt.title("Capa Roja")
plt.imshow(ImagenRed)

ImagenGreen = np.copy(ImagenRGB)
ImagenGreen[:,:,0]=0
ImagenGreen[:,:,2]=0
plt.subplot(2,2,3)
plt.title("Capa Verde")
plt.imshow(ImagenGreen)

ImagenBlue = np.copy(ImagenRGB)
ImagenBlue[:,:,0]=0
ImagenBlue[:,:,1]=0
plt.subplot(2,2,4)
plt.title("Capa Azul")
plt.imshow(ImagenBlue)

plt.figure("Figura CMYK")
ImagenCyan = np.copy(ImagenRGB)
ImagenCyan[:,:,1]=1
ImagenCyan[:,:,2]=1
plt.subplot(2,2,1)
plt.title("Capa Cyan")
plt.imshow(ImagenCyan)

ImagenMagenta = np.copy(ImagenRGB)
ImagenMagenta[:,:,0]=1
ImagenMagenta[:,:,2]=1
plt.subplot(2,2,2)
plt.title("Capa Magenta")
plt.imshow(ImagenMagenta)

ImagenYellow= np.copy(ImagenRGB)
ImagenYellow[:,:,2]=0
plt.subplot(2,2,3)
plt.title("Capa Amarilla")
plt.imshow(ImagenYellow)


plt.show()