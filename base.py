import pygame as pg

pg.init()

x = 893
y = 1000
size = (x, y)

# define a janela

screen = pg.display.set_mode(size)
pg.display.set_caption("Breakout game")

# para controlar o tempo

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

    all_sprites_list.update()

    screen.fill(BLACK)

    pg.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)

    pg.display.flip()

# finaliza o pygame
pg.quit()