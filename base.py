import pygame as pg

import barrinha # importando o arquivo da barrinha

<<<<<<< HEAD
x = 893
y = 1000
size = (x, y)

# define a janela

screen = pg.display.set_mode(size)
pg.display.set_caption("Breakout game")

# para controlar o tempo
=======
pg.init()
pg.mixer.init()

# definindo largura e altura da tela
X = 800
Y = 700

# definindo cores
AZUL = (0, 97, 148)
PRETO = (0, 0, 0)

lista_sprites = pg.sprite.Group()

# define a janela
screen = pg.display.set_mode((X, Y))
pg.display.set_caption("Breakout game")

# testando a barrinha
LARGURA_BARRINHA = 108
ALTURA_BARRINHA  = 20
barra = barrinha.Barrinha(AZUL)
barra.rect.x = X // 2 - LARGURA_BARRINHA // 2
barra.rect.y = Y - 65

lista_sprites.add(barra)
>>>>>>> b7e3a7a2c8259250701ef6f5ee8b6a4f90a2e5ee

clock = pg.time.Clock()
FPS = 60

# cores

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (8, 97, 148)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

paddle_width = 54
paddle_height = 20

all_sprites_list = pg.sprite.Group()

# CLASSE DOS TIJOLOS

class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

# CLASSE DA BARRINHA

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width

# CLASSE DA BOLA

# altura e largura dos tijolinhos
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16

# carregando uma imagem do disco

def main():
    clock.tick(FPS)
    running = True
    while running:
        for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

<<<<<<< HEAD
    all_sprites_list.update()

    screen.fill(BLACK)

    pg.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)

=======
    screen.fill(PRETO)
    lista_sprites.draw(screen)
    pg.display.update()
>>>>>>> b7e3a7a2c8259250701ef6f5ee8b6a4f90a2e5ee
    pg.display.flip()
    
# finaliza o pygame
pg.quit()