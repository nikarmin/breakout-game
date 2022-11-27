import pygame as pg

velocity = 1

class Bolinha(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        pg.draw.rect(self.image, color, [
                     0, 0, width, height], border_radius=100)
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def balancar(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]