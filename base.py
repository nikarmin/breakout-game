import pygame as pg

import barrinha # importando o arquivo da barrinha

pg.init()
pg.mixer.init()

# definindo largura e altura da tela
X = 800
Y = 700
size = (X, Y)

# definindo cores
AZUL = (0, 97, 148)
PRETO = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

lista_sprites = pg.sprite.Group()

# define a janela
screen = pg.display.set_mode(size)
pg.display.set_caption("Breakout game")

# testando a barrinha
LARGURA_BARRINHA = 108
ALTURA_BARRINHA  = 20
barra = barrinha.Barrinha(AZUL)
barra.rect.x = X // 2 - LARGURA_BARRINHA // 2
barra.rect.y = Y - 65

lista_sprites.add(barra)

clock = pg.time.Clock()
FPS = 60

# CLASSE DOS TIJOLOS

class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

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

    lista_sprites.update()
    screen.fill(PRETO)

    pg.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)

    lista_sprites.draw(screen)
    pg.display.update()
    pg.display.flip()
    
# finaliza o pygame
pg.quit()