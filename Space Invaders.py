import pygame,sys
from pygame.locals import *
from random import randint

ancho = 900
alto = 480
reloj = pygame.time.Clock()
listaEnemigo = []
Negro = [0,0,0]
Blanco = [255,255,255]

class Menu():
	def menuInicial(self,venta):
		venta.fill(Negro)
		ImagenInicial = pygame.image.load('images/inicio.png')
		venta.blit(ImagenInicial, [0,0])
		pygame.display.update()
		reloj.tick(15)
		intro = True
		while intro:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >=407 and y>=407 and x<=577 and y<=450):
						SpaceInvader(venta)

class NaveEspacial(pygame.sprite.Sprite):
    """Clase de las naves"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('C:/Users/mauri/OneDrive/Imágenes/Space invaders/nave.jpg')
        self.ImagenExplosion = pygame.image.load("images/explosion.jpg")
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30

        self.listaDisparo = []
        self.Vida = True
        self.salud = 3

        self.velocidad = 20

        self.sonidoDisparo = pygame.mixer.Sound("sonidos/balas.ogg")
        self.sonidoExplosion = pygame.mixer.Sound("sonidos/bomba.wav")

    def MovimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__Movimiento()

    def MovimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__Movimiento()

     
    def __Movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 870:
                self.rect.right = 840
    
    def Disparar(self, x, y):
        MiProyectil = Proyectil(x,y,'C:/Users/mauri/OneDrive/Imágenes/Space invaders/disparoa.jpg',True)
        self.listaDisparo.append(MiProyectil)

    def Destruccion(self):
	    self.sonidoExplosion.play()
	    self.Vida = False
	    self.velocidad = 0
	    self.ImagenNave = self.ImagenExplosion

    def Dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
        
class Proyectil(pygame.sprite.Sprite):
        def __init__(self, posx, posy, ruta, personaje):
            pygame.sprite.Sprite.__init__(self)

            self.imagenProyectil = pygame.image.load(ruta)

            self.rect = self.imagenProyectil.get_rect()

            self.velocidadDisparoPersonaje = 4
            self.velocidadDisparoEnemigo = 2

            self.rect.top = posy
            self.rect.left = posx

            self.disparoPersonaje = personaje


        def Trayectoria(self):
            if self.disparoPersonaje == True:
                self.rect.top = self.rect.top - self.velocidadDisparoPersonaje
            else:
                self.rect.top = self.rect.top + self.velocidadDisparoEnemigo

        def Dibujar(self, superficie):
            superficie.blit(self.imagenProyectil, self.rect)

class Enemigo(pygame.sprite.Sprite):
        def __init__(self, posx, posy, distancia):
            pygame.sprite.Sprite.__init__(self)

            self.imagenA = pygame.image.load('C:/Users/mauri/OneDrive/Imágenes/Space invaders/MarcianoA.jpg')
            self.imagenB = pygame.image.load('C:/Users/mauri/OneDrive/Imágenes/Space invaders/MarcianoB.jpg')

            self.listaImagenes = (self.imagenA, self.imagenB)
            self.posImagen = 0

            self.imagenInvasor = self.listaImagenes[self.posImagen]
            self.rect = self.imagenInvasor.get_rect()

            self.listaDisparo = []
            self.velocidad = 1
            self.rect.top = posy
            self.rect.left = posx

            self.rangoDisparo = 1
            self.tiempoCambio = 1

            self.conquista = False

            self.derecha = True
            self.contador = 0
            self.maxDescenso = self.rect.top + 40

            self.limiteDerecha = posx + distancia
            self.limiteIzquierda = posx - distancia
            

        def Dibujar(self, superficie):
            self.imagenInvasor = self.listaImagenes[self.posImagen]
            superficie.blit(self.imagenInvasor, self.rect)

        def Comportamiento(self, tiempo):
            if self.conquista == False:
                self.__Movimientos()
                self.__Ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen += 1
                self.tiempoCambio += 1

                if self.posImagen > len(self.listaImagenes)- 1:
                    self.posImagen = 0

        def __Movimientos(self):
            if self.contador <3:
                self.__movimientoLateral()
            else:
                self.__Descenso()
        
        def __Descenso(self):
            if self.maxDescenso == self.rect.top:
                self.contador = 0
                self.maxDescenso = self.rect.top + 40 
            else:
                self.rect.top += 1
        
        def __movimientoLateral(self):
            if self.derecha == True:
                self.rect.left = self.rect.left + self.velocidad
                if self.rect.left > 500:
                    self.derecha = False
                    self.contador +=1
            else:
                self.rect.left = self.rect.left - self.velocidad
                if self.rect.left < 0:
                    self.derecha = True


        def __Ataque(self):
            if (randint(0,300) < self.rangoDisparo):
                self.__Disparo()

        def __Disparo(self):
            x,y = self.rect.center
            miProyectil = Proyectil(x,y,'C:/Users/mauri/OneDrive/Imágenes/Space invaders/disparob.jpg',False)
            self.listaDisparo.append(miProyectil)

def detenerTodo():
	for enemigo in listaEnemigo:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)
		listaEnemigo.remove(enemigo)

def cargarEnemigos():
	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,100,40,'images/marcianoA.jpg', 'images/marcianoB.jpg')
		listaEnemigo.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,0,40,'images/Marciano2A.jpg', 'images/Marciano2B.jpg')
		listaEnemigo.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Enemigo(posx,-100,40,'images/Marciano3A.jpg', 'images/Marciano3B.jpg')
		listaEnemigo.append(enemigo)
		posx = posx + 200

class gameOver():
	def cargarGameOver(self, venta):
		venta.fill(Negro)
		game_over = pygame.image.load('images/game_over.png')
		venta.blit(game_over, [-15,0])
		pygame.display.flip()
		intro = True
		while intro:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >=365 and y>=301 and x<=564 and y<=347):
						detenerTodo()
						SpaceInvader(venta)
					if(x >=369 and y>=365 and x<=563 and y<=419):
						creditos = Creditos()
						creditos.mostrarCreditos(venta)
					if(x >=384 and y>=436 and x<=546 and y<=473):
						sys.exit()

class Creditos():
	def mostrarCreditos(self, ventana):
		creditos = pygame.image.load('images/creditos.png')
		ventana.blit(creditos,[0,0])
		pygame.display.flip()
		credit = True;
		while credit:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >= 717 and y>=18 and x<=827 and y<=57):
						game_over = gameOver()

class Ganador():
	def mostrarGanador(self,ventana):
		ventana.fill(Negro)
		game_over = pygame.image.load('images/ganador.png').convert_alpha()
		ventana.blit(game_over, [0,20])
		pygame.display.flip()
		ganador = True
		while ganador:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >= 380 and y>=400 and x<=511 and y<=436):
						detenerTodo()
						SpaceInvader(ventana)
					if(x >= 417 and y>=461 and x<=476 and y<=488):
						sys.exit()

def SpaceInvader(Ventana):
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    gameover = gameOver()
    ImagenFondo = pygame.image.load('images/Fondo.jpg')
	#VIDAS
    vida1 = pygame.image.load('images/vida.png')
    vida2 = pygame.image.load('images/vida.png')
    vida3 = pygame.image.load('images/vida.png')
    
    pygame.mixer.music.load('sonidos/intro.mp3')
    pygame.mixer.music.play(3)
    puntaje = 0
    Fuente=pygame.font.Font(None,34)
    pygame.display.flip()
    reloj.tick(0.8)
    juego = True
    jugador = NaveEspacial(ancho,alto)
    detenerTodo()
    cargarEnemigos()

    while juego:
	    reloj.tick(300)
	    t_puntaje = 'Score: {0000}'.format(puntaje)
	    txt_puntaje = Fuente.render(t_puntaje, True, Blanco)
	    tiempo = int (pygame.time.get_ticks()/1000)

	    for evento in pygame.event.get():
		    if evento.type == QUIT:
			    pygame.quit()

		    if juego == True:
			    if evento.type == pygame.KEYDOWN:
				    if evento.key == K_LEFT:
					    jugador.movimientoIzquierda()

				    elif evento.key == K_RIGHT:
					    jugador.movimientoDerecha()

				    elif evento.key == K_s:
					    x,y = jugador.rect.center
					    jugador.disparar(x,y)

	    Ventana.blit(ImagenFondo, (0,0))
	    jugador.dibujar(Ventana)		
		

	    if len(jugador.listaDisparo)>0:
		    for x in jugador.listaDisparo:
			    x.dibujar(Ventana)
			    x.trayectoria()

			    if x.rect.top < -10:
				    jugador.listaDisparo.remove(x)
			    else:
				    for enemigo in listaEnemigo:
					    if x.rect.colliderect(enemigo.rect):
						    listaEnemigo.remove(enemigo)
						    jugador.listaDisparo.remove(x)
						    puntaje += 40


	    if len(listaEnemigo) > 0:
		    for enemigo in listaEnemigo:
			    enemigo.comportamiento(tiempo)
			    enemigo.dibujar(Ventana)

			    if enemigo.rect.colliderect(jugador.rect):
				    gameover.cargarGameOver(Ventana)
				    detenerTodo()

			    if len(enemigo.listaDisparo)>0:
				    for x in enemigo.listaDisparo:
					    x.dibujar(Ventana)
					    x.trayectoria()

					    if x.rect.colliderect(jugador.rect):
						    enemigo.listaDisparo.remove(x)
						    jugador.salud -=1
							
							
					    if x.rect.top > 900:
						    enemigo.listaDisparo.remove(x)
					    else:
						    for disparo in jugador.listaDisparo:
							    if x.rect.colliderect(disparo.rect):
								    jugador.listaDisparo.remove(disparo)
								    enemigo.listaDisparo.remove(x)
								    puntaje += 40
	    if len(listaEnemigo) == 0:
		    ganador = Ganador()
		    ganador.mostrarGanador(Ventana)
		    juego = False

	    if(jugador.salud == 3):
		    Ventana.blit(vida1, (780,570))
		    Ventana.blit(vida2, (820,570))
		    Ventana.blit(vida3, (860,570))
	    if(jugador.salud == 2):
		    Ventana.blit(vida1, (820,570))
		    Ventana.blit(vida2, (860,570))
	    if(jugador.salud ==1):
		    Ventana.blit(vida1, (860,570))
	    if(jugador.salud == 0):
		    gameover.cargarGameOver(Ventana)
		    detenerTodo()

			
	    Ventana.blit(txt_puntaje, [10,578])
	    pygame.display.update()

if __name__ == '__main__':
	ventana = pygame.display.set_mode((ancho,alto))
	menu = Menu()
	menu.menuInicial(ventana)