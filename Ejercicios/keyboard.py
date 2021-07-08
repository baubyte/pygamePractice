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
coordX = 10
coordY = 10

# Velocidad
speedX = 3
speedY = 3

# Visibilidad del Mouse
pygame.mouse.set_visible(0)

# Estructura Principal 
while True:
    # Recorremos todos los eventos
    for event in pygame.event.get():
        # Comprobamos si el evento es salir paramos la ejecución
        if event.type == pygame.QUIT:
            sys.exit()
        # Eventos del Teclado
        if event.type == pygame.KEYDOWN:
            # Verificamos las Teclas que se están pulsando
            if event.key == pygame.K_LEFT:
                speedX = -3
            if event.key == pygame.K_RIGHT:
                speedX = 3
            if event.key == pygame.K_UP:
                speedY = -3
            if event.key == pygame.K_DOWN:
                speedY = 3
        if event.type == pygame.KEYUP:
            # Verificamos las Teclas que se están pulsando
            if event.key == pygame.K_LEFT:
                speedX = 0
            if event.key == pygame.K_RIGHT:
                speedX = 0
            if event.key == pygame.K_DOWN:
                speedY = 0
            if event.key == pygame.K_UP:
                speedY = 0

    ### Inicio Lógica del Juego ###
    
    ### Fin Lógica del Juego    ###


    ### Inicio Zona de Dibujo ###
    # Color de Fondo
    screen.fill(white)
    coordX += speedX
    coordY += speedY
    # Dibujamos un cuadrado
    pygame.draw.rect(screen, red,(coordX,coordY,100,100))
    ### Fin Zona de Dibujo    ###

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(60)