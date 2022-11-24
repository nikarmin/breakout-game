import pygame as pg

class Bolinha(pg.sprite.Sprite):
    def __init__(self, cor, larg, alt) -> None:
        super().__init__()
        self.image = pg.Surface([alt, larg])
        pg.draw.rect(self.image, cor, [0,0, larg, alt])
        self.rect = self.image.get_rect()
        self.velocity = [4, 4]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def balancar(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]