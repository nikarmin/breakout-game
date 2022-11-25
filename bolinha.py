import pygame as pg
from random import randint


class Bolinha(pg.sprite.Sprite):
    def __init__(self, cor, larg, alt):
        super().__init__()
        self.largura = larg
        self.altura = alt
        self.image = pg.Surface([self.largura, self.altura])
        self.image.fill(cor)
        self.image.set_colorkey(cor)
        pg.draw.rect(self.image, cor, [0, 0, self.largura, self.altura])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def balancar(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[-8, 8]
