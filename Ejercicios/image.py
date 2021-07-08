from move import PLAYER
import pygame

# Iniciamos pygame
pygame.init()

# Definimos Tamaño de la Ventana

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Creamos la Ventana
screen = pygame.display.set_mode(SIZE)
# Titulo de la Ventana
pygame.display.set_caption("MatePong")
# Control de los FPS
clock = pygame.time.Clock()
# Visibilidad del Mouse
pygame.mouse.set_visible(1)

# Definimos Colores

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED =   ( 255,   0,   0)
BLUE =  (   0,   0, 255)

BACKGROUND = pygame.image.load("background.png").convert()

# Constante de Salida
gameOver = False

# Estructura Principal 
while not gameOver:
    # Recorremos todos los eventos
    for event in pygame.event.get():
        # Comprobamos si el evento es salir paramos la ejecución
        if event.type == pygame.QUIT:
            gameOver = True

    ### Inicio Lógica del Juego ###
    ### Fin Lógica del Juego    ###

    # Fondo
    screen.blit(BACKGROUND,(0,0))
    ### Inicio Zona de Dibujo ###
    
    ### Fin Zona de Dibujo    ###

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(60)
# Salimos del Juego
pygame.quit()