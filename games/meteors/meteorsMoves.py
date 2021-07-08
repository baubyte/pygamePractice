import pygame, random


# Definimos Colores

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED =   ( 255,   0,   0)
BLUE =  (   0,   0, 255)
# Definimos Tamaño de la Ventana
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

class Meteor(pygame.sprite.Sprite):
    """Clase para crear los sprites
    para generar los meteoros

    Args:
        pygame ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        # Sacamos el Fondo
        self.image.set_colorkey(BLACK)
        # Coordenadas de la Imagen
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y +=1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -10
            self.rect.x = random.randrange(SCREEN_WIDTH)

class Player(pygame.sprite.Sprite):
    """Clase para crear los sprites
    para generar el jugador

    Args:
        pygame ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        # Sacamos el Fondo
        self.image.set_colorkey(BLACK)
        # Coordenadas de la Imagen
        self.rect = self.image.get_rect()

    def update(self):
        # Obtenemos la posición del mouse
        mousePosition = pygame.mouse.get_pos()
        self.rect.x = mousePosition[0]
        self.rect.y = mousePosition[1]


# Iniciamos pygame
pygame.init()

# Creamos la Ventana
screen = pygame.display.set_mode(SIZE)
# Titulo de la Ventana
pygame.display.set_caption("Sprite")
# Control de los FPS
clock = pygame.time.Clock()
# Visibilidad del Mouse
pygame.mouse.set_visible(0)


# Constante de Salida
gameOver = False
score = 0

# Lista del Grupo de Sprites
meteors = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

# Creamos los meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    # Agregamos la instancia de Meteor a la lista de sprites
    meteors.add(meteor)
    allSprites.add(meteor)
# Jugador
player = Player()
allSprites.add(player)

# Estructura Principal 
while not gameOver:
    # Recorremos todos los eventos
    for event in pygame.event.get():
        # Comprobamos si el evento es salir paramos la ejecución
        if event.type == pygame.QUIT:
            gameOver = True

    ### Inicio Lógica del Juego ###

    # Movimiento de los Sprites
    allSprites.update()

    # Colisiones
    meteorsHit = pygame.sprite.spritecollide(player, meteors, True)

    for meteor in meteorsHit:
        score += 1
        print(score)
    ### Fin Lógica del Juego    ###

    # Fondo
    screen.fill(WHITE)
    ### Inicio Zona de Dibujo ###
    # Dibujamos los sprites
    allSprites.draw(screen)
    ### Fin Zona de Dibujo    ###

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(60)
# Salimos del Juego
pygame.quit()