import pygame as pg

class Barrinha(pg.sprite.Sprite):

    def __init__(self, cor, largura, altura):
        super().__init__()
        self.largura = largura
        self.altura = altura
        self.image = pg.Surface([self.largura, self.altura])
        pg.draw.rect(self.image, cor, [0, 0, self.largura, self.altura])
        self.rect = self.image.get_rect()

    def irParaDireita(self, pixels, xTela):
        self.rect.x += pixels # posicionamos a barrinha alguns pixels à direita
        # se a barrinha chegou ao limite direito da tela, ela não avança mais
        if self.rect.x > xTela - self.largura :
            self.rect.x = xTela - self.largura

    def irParaEsquerda(self, pixels):
        self.rect.x -= pixels # posicionamos a barrinha alguns pixels à esquerda
        # se a barrinha chegou ao limite esquerdo da tela, posicionamos ela no inicio da tela
        if self.rect.x < 0:
            self.rect.x = 0