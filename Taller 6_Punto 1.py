from Libreria import *

MiVentana = pygame
Rojo = (255,0,0)
Amarillo = (255,255,0)
Azul = (0,0,255)
Verde = (0,255,0)
Blanco = (255,255,255)
Morado = (87,35,100)
Magenta = (207,52,118)
Naranja = (255,128,0)
Negro = (0,0,0)

pygame.init()
MiVentana = pygame.display.set_mode((800,650))
pygame.display.set_caption("Punto 1") 

Rectangulo(MiVentana, Verde,[325,90],[475,175]) # Cabeza
Rectangulo(MiVentana, Verde,[353,175],[447,190]) # Cuello
Rectangulo(MiVentana, Verde,[370,150],[430,165]) # Boca
LineaBres(MiVentana, Verde,[385,150],[385,165]) # Dientes
LineaBres(MiVentana, Verde,[400,150],[400,165]) # Dientes
LineaBres(MiVentana, Verde,[415,150],[415,165]) # Dientes
CirculoBres(MiVentana, Verde, 360, 120, 20) # Ojos
CirculoBres(MiVentana, Verde, 440, 120, 20) # Ojos
CirculoBres(MiVentana, Verde, 360, 120, 8) # Ojos
CirculoBres(MiVentana, Verde, 440, 120, 8) # Ojos
Rectangulo(MiVentana, Negro,[350,120],[368,130]) #pestaña
Rectangulo(MiVentana, Negro,[430,120],[448,130]) #pestaña
Rectangulo(MiVentana, Verde,[392,45],[408,90]) # Antena
CirculoBres(MiVentana, Verde, 400, 31, 15) # Antena

Rectangulo(MiVentana, Verde,[300,190],[500,380]) # Cuerpo
Rectangulo(MiVentana, Verde,[325,215],[475,255]) # Pecho
CirculoBres(MiVentana, Verde, 360, 340, 10) # botones cuerpo
CirculoBres(MiVentana, Verde, 400, 340, 10) # botones cuerpo
CirculoBres(MiVentana, Verde, 440, 340, 10) # botones cuerpo

Rectangulo(MiVentana, Verde,[280,205],[300,215]) # Brazo Derecho
CirculoBres(MiVentana, Verde, 262, 210, 18) # Externo Hombro Derecho
CirculoBres(MiVentana, Verde, 262, 210, 7) # Interno Hombro Derecho
Rectangulo(MiVentana, Verde,[255,228],[270,238]) # Brazo Derecho
Rectangulo(MiVentana, Verde,[253,238],[273,335]) # Brazo Derecho
Rectangulo(MiVentana, Verde,[259,335],[266,345]) # Brazo Derecho
CirculoBres(MiVentana, Verde, 263, 355, 10) # Mano Derecho
Rectangulo(MiVentana, Verde,[242,355],[252,390]) # Mano Derecho
Rectangulo(MiVentana, Verde,[274,355],[284,390]) # Mano Derecho
Rectangulo(MiVentana, Verde,[500,205],[520,215]) # Brazo Izquierdo
CirculoBres(MiVentana, Verde, 538, 210, 18) # Externo Hombro Izquierdo
CirculoBres(MiVentana, Verde, 538, 210, 7) # Interno Hombro Izquierdo
Rectangulo(MiVentana, Verde,[530,228],[545,238]) # Brazo Izquierdo
Rectangulo(MiVentana, Verde,[528,238],[548,335]) # Brazo Izquierdo
Rectangulo(MiVentana, Verde,[534,335],[541,345]) # Brazo Izquierdo
CirculoBres(MiVentana, Verde, 538, 355, 10) # Mano Izquierdo
Rectangulo(MiVentana, Verde,[517,355],[527,390]) # Mano Izquierda
Rectangulo(MiVentana, Verde,[549,355],[559,390]) # Mano Izquierda
Rectangulo(MiVentana, Verde,[330,380],[360,470]) # Pierna Derecha
Rectangulo(MiVentana, Verde,[440,380],[470,470]) # Pierna Izquierda
TrianguloRectangulo(MiVentana, Verde, [440,510], 90, -30, 0)
TrianguloRectangulo(MiVentana, Verde, [360,510], 90, -110, 1)
LineaBres(MiVentana, Verde,[330,470],[330,483])
LineaBres(MiVentana, Verde,[470,470],[470,483])
TrianguloEquilatero(MiVentana, Verde, [345,240], 20)
TrianguloEquilatero(MiVentana, Verde, [375,240], 20)
TrianguloEquilatero(MiVentana, Verde, [405,240], 20)
TrianguloEquilatero(MiVentana, Verde, [435,240], 20)

pygame.display.update()
time.sleep(5)