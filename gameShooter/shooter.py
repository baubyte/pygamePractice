import pygame, random, os


# Direcotrio del Archivo
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Definimos Tamaño de la Ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Definimos Colores
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
# Definimos la Ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Establecemos el Titulo de la Ventana
pygame.display.set_caption("Shooter")
# Definimos el Reloj
clock = pygame.time.Clock()

# Dibujar Texto en la Pantalla
def drawText(surface, text, size, x, y):
    # Fuente
	font = pygame.font.SysFont("serif", size)
    # Banderizamos el texto
	text_surface = font.render(text, True, WHITE)
    # Recta
	text_rect = text_surface.get_rect()
    # Posición
	text_rect.midtop = (x, y)
    # Pintamos el texto
	surface.blit(text_surface, text_rect)

# Crear Meteoros
def createMeteor():
    meteor = Meteor()
    # Agregamos a todos los sprites
    allSprites.add(meteor)
    # Agregamos a los sprites de meteoros
    meteors.add(meteor)

# Crear Explosion
def createExplosion(rect):
    # Reproducimos la Explosion
    explosionSound.play()
    explosion = Explosion(rect.center)
    # Agregamos la explosion a todos los sprites
    allSprites.add(explosion)
# Dibujar Escudo
def drawShieldBar(surface, x, y, percentage):
    # Tamaño de Barra
	BAR_LENGTH = 100
	BAR_HEIGHT = 10
    # Llenado de la barra
	fill = (percentage / 100) * BAR_LENGTH
    # Borde de la Barra
	border = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    # Llenado de la barra
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    # Dibujamos la barra
	pygame.draw.rect(surface, GREEN, fill)
    # Dibujamos el borde
	pygame.draw.rect(surface, WHITE, border, 2)

# Pantalla de Game Over
def showGameOverScreen():
    screen.blit(BACKGROUND, [0,0])
    drawText(screen, "Shooter", 65, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    drawText(screen, "Espacio:Disparar / Mover: Flecha Izq. Flecha Der.", 27, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    drawText(screen, "Presione Enter Para Comenzar", 27, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    waiting = False

class Player(pygame.sprite.Sprite):
    """Clase del Jugador del Video Juego

    Args:
        pygame ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(THIS_FOLDER, "assets/player.png")).convert()
        # Sacamos el Color de fondo
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Posición
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        # Velocidad
        self.speedX = 0
        # Escudo
        self.shield = 100

    def update(self):
        # Velocidad 0
        self.speedX = 0
        # Si se Presiono alguna Tecla
        keystate = pygame.key.get_pressed()
        # Si pulso la izquierda
        if keystate[pygame.K_LEFT]:
            self.speedX = -5
        # Si pulso la derecha
        if keystate[pygame.K_RIGHT]:
            self.speedX = 5
        # Movemos el jugador
        self.rect.x += self.speedX
        # Para no salir de la Pantalla
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        allSprites.add(bullet)
        bullets.add(bullet)
        laserSound.play()

class Meteor(pygame.sprite.Sprite):
    """Clase que permite crear los sprites de los meteoros

    Args:
        pygame ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.image = random.choice(mateorsImages)
        self.image.set_colorkey(BLACK)
        # Obtenemos la recta
        self.rect = self.image.get_rect()
        # Definimos una posición
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        # Velocidad Aleatoria
        self.speedY = random.randrange(1, 10)
        self.speedX = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.speedY
        self.rect.x += self.speedX
        # Si paso el alto de la ventana o si salio de la ventana desde la izquierda
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -40 or self.rect.right > SCREEN_WIDTH + 40:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-140,-100)
            self.speedY = random.randrange(1, 10)
            #self.speedX = random.randrange(-5, 5)

class Bullet(pygame.sprite.Sprite):
    """Clase para generar los proyectiles

    Args:
        pygame ([type]): [description]
    """
    def __init__(self, x, y):
        super().__init__()
        # Cargammos la imagen
        self.image = pygame.image.load(os.path.join(THIS_FOLDER, "assets/laser1.png"))
        # Sacamos el Color de fondo
        self.image.set_colorkey(BLACK)
        # Recta del Objeto
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedY = -10

    def update(self):
        self.rect.y += self.speedY
        # Si sale de la ventana lo limpiamos eliminamos la instancia del objeto
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    """Clase para el spite de explocion

    Args:
        pygame ([type]): [description]
    """
    def __init__(self, center):
        super().__init__()
        self.image = explosionsAnimations[0]
        # Recara
        self.rect = self.image.get_rect()
        # Centramos la imagen
        self.rect.center = center
        # Frame
        self.frame = 0
        # Sacar el punto exacto para la mostrar la explosion
        self.lastUpdate = pygame.time.get_ticks()
        # VELOCIDAD DE LA EXPLOSION
        self.frameRate = 50 

    def update(self):
        # El punto actual
        now = pygame.time.get_ticks()
        # Si lo que transcurrio mas de los 60 para mostrar la explosion
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            # Ingrementamos la variable para ir pasando de imagen en imagen
            self.frame += 1
            # Si ya pasaron todas las imágenes si asi lo limpiamos
            if self.frame == len(explosionsAnimations):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosionsAnimations[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Imágenes de los Meteoros
mateorsImages = []
meteorsFiles = os.listdir(os.path.join(THIS_FOLDER, "assets/meteors"))
for meteorFile in meteorsFiles:
	mateorsImages.append(pygame.image.load(os.path.join(THIS_FOLDER, "assets/meteors/{}".format(meteorFile))).convert())

# Imágenes de Explosion
explosionsAnimations = []
explosionsAnimationsFiles = os.listdir(os.path.join(THIS_FOLDER, "assets/explosions"))
for explosionAnimationFile in explosionsAnimationsFiles:
	img = pygame.image.load(os.path.join(THIS_FOLDER, "assets/explosions/{}".format(explosionAnimationFile))).convert()
    # Sacamos el fondo negro
	img.set_colorkey(BLACK)
    # Escalamos la imagen
	imgScale = pygame.transform.scale(img, (70,70))
    # Agremos a la lista de animacion
	explosionsAnimations.append(imgScale)

# Imagen de Fondo
BACKGROUND = pygame.image.load(os.path.join(THIS_FOLDER, "assets/background.png")).convert()
# Cargar sonidos
laserSound = pygame.mixer.Sound(os.path.join(THIS_FOLDER, "assets/laser5.ogg"))
laserSound.set_volume(0.1)
explosionSound = pygame.mixer.Sound(os.path.join(THIS_FOLDER, "assets/explosion.wav"))
explosionSound.set_volume(0.1)
pygame.mixer.music.load(os.path.join(THIS_FOLDER, "assets/music.ogg"))
pygame.mixer.music.set_volume(0.1)

# Reproducir Música de Fondo -1 para que repita simpre
pygame.mixer.music.play(loops=-1)

# Correr el Juego
running = True
# Fin de Juego
gameOver = True

while running:
    #FPS
    clock.tick(60)
    if gameOver:
        showGameOverScreen()
        gameOver = False
        # Sprites
        allSprites = pygame.sprite.Group()
        meteors = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        # Creamos los meteoros
        for i in range(8):
            createMeteor()
        player = Player()
        allSprites.add(player)
        # Marcador
        score = 0
    # Revisamos los Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                showGameOverScreen()

    # Movimiento de los Sprites
    allSprites.update()
	#Verificamos las colisiones del meteoro con el laser
    hits = pygame.sprite.groupcollide(meteors, bullets, True, True)
    for hit in hits:
        score += 5
        # Animacion de Explosion
        createExplosion(hit.rect)
        #Volvemos a crear los meteoros
        createMeteor()
    # Verificamos las colisiones del jugador con el meteoro
    hits = pygame.sprite.spritecollide(player, meteors, True,pygame.sprite.collide_mask)
    for hit in hits:
        player.shield -= 25
        # Animacion de Explosion
        createExplosion(hit.rect)
        #Volvemos a crear los meteoros
        createMeteor()
        if player.shield <= 0:
            gameOver = True
    # Fondo
    screen.blit(BACKGROUND,(0,0))
    ### Inicio Zona de Dibujo ###
    # Dibujamos los sprites
    allSprites.draw(screen)
    # Dibujamos el marcador
    drawText(screen, str(score), 25, SCREEN_WIDTH // 2, 10)
    # Escudo.
    drawShieldBar(screen, 5, 5, player.shield)
    ### Fin Zona de Dibujo    ###
    # Actualizar Pantalla
    pygame.display.flip()
# Salimos del Juego
pygame.quit()