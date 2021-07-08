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

class Game(object):
    """Clase principal del Juego

    Args:
        pygame ([type]): [description]
    """
    def __init__(self) -> None:
        self.gameOver = False
        self.score = 0
        self.meteors = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group() 
        # Creamos los meteoros
        for i in range(50):
            meteor = Meteor()
            meteor.rect.x = random.randrange(900)
            meteor.rect.y = random.randrange(600)
            # Agregamos la instancia de Meteor a la lista de sprites
            self.meteors.add(meteor)
            self.allSprites.add(meteor)
        
        # Jugador
        self.player = Player()
        self.allSprites.add(self.player)
    
    def processEvents(self):
        # Recorremos todos los eventos
        for event in pygame.event.get():
            # Comprobamos si el evento es salir paramos la ejecución
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.gameOver:
                    self.__init__()
        return False

    def runLogic(self):
        if not self.gameOver:
            # Movimiento de los Sprites
            self.allSprites.update()
            # Colisiones
            meteorsHit = pygame.sprite.spritecollide(self.player, self.meteors, True)
            for meteor in meteorsHit:
                self.score += 1
                print(self.score)
            if len(self.meteors) == 0:
                self.gameOver = True

    def displayFrame(self,screen):
        # Fondo
        screen.fill(WHITE)
        if self.gameOver:
            font = pygame.font.SysFont("serif", 25) # Fuente
            text = font.render("Gamer Over Click para Continuar", True, BLACK) # Texto
            centerX = (SCREEN_WIDTH // 2)-(text.get_width() // 2) # Posicion en Pantalla
            centerY = (SCREEN_HEIGHT // 2)- (text.get_height() // 2) # Posicion en Pantalla
            screen.blit(text,(centerX,centerY)) # Mostrar texto en Pantalla

        if not self.gameOver:
            # Dibujamos los sprites
            self.allSprites.draw(screen)
        # Actualizar Pantalla
        pygame.display.flip()

# Funcion Principal
def main():
    pygame.init()
    # Creamos la Ventana
    screen = pygame.display.set_mode(SIZE)
    # Titulo de la Ventana
    pygame.display.set_caption("Game Class")
    # Control de los FPS
    clock = pygame.time.Clock()
    # Visibilidad del Mouse
    pygame.mouse.set_visible(0)
    # Constante de Salida
    done = False
    
    game = Game()
    
    while not done:
        done = game.processEvents()
        game.runLogic()
        game.displayFrame(screen)
        clock.tick(60)
    # Salimos del Juego
    pygame.quit()

if __name__ == "__main__":
    main()