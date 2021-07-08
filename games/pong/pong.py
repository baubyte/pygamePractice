import pygame

# Iniciamos pygame
pygame.init()

# Definimos Tamaño de la Ventana

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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
# Tamaño Jugadores
MATE_WIDTH = 15
MATE_HEIGHT = 90
# Cordenadas Y Velocidad Jugador 1
MATE_ONE_COORD_X = 50
MATE_ONE_COORD_Y = (SCREEN_HEIGHT/2) - (MATE_HEIGHT/2)
MATE_ONE_SPEED_Y = 0

# Cordenadas Y Velocidad Jugador 2
MATE_TWO_COORD_X = SCREEN_WIDTH - MATE_HEIGHT
MATE_TWO_COORD_Y = (SCREEN_HEIGHT/2) - (MATE_HEIGHT/2)
MATE_TWO_SPEED_Y = 0

# Cordenadas Y Velocidad Pelota
BALL_RADIUS = 10
BALL_COORD_X = (SCREEN_WIDTH/2)
BALL_COORD_Y = (SCREEN_HEIGHT/2)
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Constante de Salida
gameOver = False

# Estructura Principal 
while not gameOver:
    # Recorremos todos los eventos
    for event in pygame.event.get():
        # Comprobamos si el evento es salir paramos la ejecución
        if event.type == pygame.QUIT:
            gameOver = True
        # Eventos del Teclado
        # Al presionar las teclas movemos los jugadores
        if event.type == pygame.KEYDOWN:
            # Verificamos las Teclas que se están pulsando
            # Jugador 1
            if event.key == pygame.K_w and MATE_ONE_COORD_Y > 0:
                MATE_ONE_SPEED_Y = -3
            if event.key == pygame.K_s and MATE_ONE_COORD_Y < (SCREEN_HEIGHT-MATE_HEIGHT):
                MATE_ONE_SPEED_Y = 3
            
            # Jugador 2
            if event.key == pygame.K_UP and MATE_TWO_COORD_Y > 0:
                MATE_TWO_SPEED_Y = -3
            if event.key == pygame.K_DOWN and MATE_TWO_COORD_Y < (SCREEN_HEIGHT-MATE_HEIGHT):
                MATE_TWO_SPEED_Y = 3
        # Al soltar la tecla dejamos de mover
        if event.type == pygame.KEYUP:
            # Verificamos las Teclas que se están soltando
            # Jugador 1
            if event.key == pygame.K_w:
                MATE_ONE_SPEED_Y = 0
            if event.key == pygame.K_s:
                MATE_ONE_SPEED_Y = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                MATE_TWO_SPEED_Y = 0
            if event.key == pygame.K_DOWN:
                MATE_TWO_SPEED_Y = 0

    ### Inicio Lógica del Juego ###
    # Verificamos la Posición de la pelota
    if BALL_COORD_Y > (SCREEN_HEIGHT-BALL_RADIUS) or BALL_COORD_Y < BALL_RADIUS:
        BALL_SPEED_Y *= -1
    # Si sale del lado derecho
    if BALL_COORD_X > (SCREEN_WIDTH) or BALL_COORD_X < (SCREEN_HEIGHT-SCREEN_HEIGHT):
        BALL_COORD_X = (SCREEN_WIDTH/2)
        BALL_COORD_Y = (SCREEN_HEIGHT/2)
        # Si sale Invierte la Dirección
        BALL_SPEED_X *= -1
        BALL_SPEED_Y *= -1
    
    # Modifica las coordenadas para dar movimiento a los mates
    # Movemos el Jugador 1
    MATE_ONE_COORD_Y += MATE_ONE_SPEED_Y
    # Verificamos que no salda de la Pantalla
    if MATE_ONE_COORD_Y < (SCREEN_HEIGHT-SCREEN_HEIGHT) or MATE_ONE_COORD_Y > (SCREEN_HEIGHT-MATE_HEIGHT):
        MATE_ONE_SPEED_Y = 0
    # Movemos el Jugador 2
    MATE_TWO_COORD_Y += MATE_TWO_SPEED_Y
    # Verificamos que no salda de la Pantalla
    if MATE_TWO_COORD_Y < (SCREEN_HEIGHT-SCREEN_HEIGHT) or MATE_TWO_COORD_Y > (SCREEN_HEIGHT-MATE_HEIGHT):
        MATE_TWO_SPEED_Y = 0

    # Movimientos Pelota
    BALL_COORD_X += BALL_SPEED_X
    BALL_COORD_Y += BALL_SPEED_Y
    # Verificamos que no salga de la Pantalla

    ### Fin Lógica del Juego    ###

    # Color de Fondo
    screen.fill(BLACK)
    ### Inicio Zona de Dibujo ###
    # Jugador 1 
    mateOne = pygame.draw.rect(screen, WHITE, (MATE_ONE_COORD_X,MATE_ONE_COORD_Y,MATE_WIDTH,MATE_HEIGHT))
    # Jugador 2
    mateTwo = pygame.draw.rect(screen, WHITE, (MATE_TWO_COORD_X,MATE_TWO_COORD_Y,MATE_WIDTH,MATE_HEIGHT))
    # Pelota
    ball = pygame.draw.circle(screen,WHITE, (BALL_COORD_X, BALL_COORD_Y), BALL_RADIUS)

    # Colisiones 
    if ball.colliderect(mateOne) or ball.colliderect(mateTwo):
        BALL_SPEED_X *= -1
    ### Fin Zona de Dibujo    ###

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(60)
# Salimos del Juego
pygame.quit()