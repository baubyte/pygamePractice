import pygame, sys, random

# Iniciamos pygame
pygame.init()

# Definimos Colores

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red =   ( 255,   0,   0)
blue =  (   0,   0, 255)

# Definimos Tamaño de la Ventana
size = (800, 500)

# Creamos la Ventana
screen = pygame.display.set_mode(size)
# Control de los FPS
clock = pygame.time.Clock()

# Coordenadas 
coordList = []
for i in range(60):
    x = random.randint(0,  800)
    y = random.randint(0,  500)
    coordList.append([x,y])

# Velocidad
speedX = 3
speedY = 3

# Estructura Principal 
while True:
    # Recorremos todos los eventos
    for event in pygame.event.get():
        # Comprobamos si el evento es salir paramos la ejecución
        if event.type == pygame.QUIT:
            sys.exit()

    ### Inicio Lógica del Juego ###

    ### Fin Lógica del Juego    ###


    ### Inicio Zona de Dibujo ###
    # Color de Fondo
    screen.fill(white)
    for coord in coordList:
        pygame.draw.circle(screen, red, coord,2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0

    ### Fin Zona de Dibujo    ###

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(30)