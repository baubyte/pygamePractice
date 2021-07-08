import pygame, random, os

# Direcotrio del Archivo
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
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
        self.image = pygame.image.load(os.path.join(THIS_FOLDER, 'meteor.png')).convert()
        # Sacamos el Fondo
        self.image.set_colorkey(BLACK)
        # Coordenadas de la Imagen
        self.rect = self.image.get_rect()
    

class Player(pygame.sprite.Sprite):
    """Clase para crear los sprites
    para generar el jugador

    Args:
        pygame ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(THIS_FOLDER, 'player.png')).convert()
        # Sacamos el Fondo
        self.image.set_colorkey(BLACK)
        # Coordenadas de la Imagen
        self.rect = self.image.get_rect()

    def update(self):
        # Obtenemos la posición del mouse
        mousePosition = pygame.mouse.get_pos()
        self.rect.x = mousePosition[0]
        self.rect.y = 510

class Laser(pygame.sprite.Sprite):
    """Clase para crear los sprites
    para generar el laser

    Args:
        pygame ([type]): [description]
    """
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(THIS_FOLDER, 'laser.png')).convert()
        # Sacamos el Fondo
        self.image.set_colorkey(BLACK)
        # Coordenadas de la Imagen
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5

# Iniciamos pygame
pygame.init()

# Creamos la Ventana
screen = pygame.display.set_mode(SIZE)
# Titulo de la Ventana
pygame.display.set_caption("Meteor Shoot")
# Control de los FPS
clock = pygame.time.Clock()
# Visibilidad del Mouse
pygame.mouse.set_visible(0)


# Constante de Salida
gameOver = False
score = 0

# Lista del Grupo de Sprites
meteors = pygame.sprite.Group()
lasers = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

# Creamos los meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(SCREEN_WIDTH-20)
    meteor.rect.y = random.randrange(SCREEN_HEIGHT-150)

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
        
        # Al hacer click el botón del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y - 20
            # Agregamos el laser a la lista de sprites
            allSprites.add(laser)
            # Agregamos el laser a la lista de laseres
            lasers.add(laser)
    ### Inicio Lógica del Juego ###

    # Movimiento de los Sprites
    allSprites.update()

    # Colisiones
    for laser in lasers:
        meteorsHit = pygame.sprite.spritecollide(laser, meteors, True)
        # Eliminamos el Laser
        for meteor in meteorsHit:
            allSprites.remove(laser)
            lasers.remove(laser)
            score += 1
            print(score)
        # Si sobrepasa el laser
        if laser.rect.y < -10:
            allSprites.remove(laser)
            lasers.remove(laser)
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