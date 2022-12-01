import pygame as pg

class Tijolo (pg.sprite.Sprite):
    def __init__(self, cor, largura, altura):
        super().__init__()
        self.image = pg.Surface([largura, altura])
        pg.draw.rect(self.image, cor, [0,0,largura,altura])
        self.rect = self.image.get_rect()