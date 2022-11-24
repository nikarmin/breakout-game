import pygame as pg

pg.init()

largura_barrinha = 108
altura_barrinha  = 20

class Barrinha(pg.sprite.Sprite):

    def __init__(self, cor):
        super().__init__()
        self.image = pg.Surface([largura_barrinha, altura_barrinha])
        pg.draw.rect(self.image, cor, [0, 0, largura_barrinha, altura_barrinha])
        self.rect = self.image.get_rect()

    def irParaDireita(self, pixels, xTela):
        self.rect.x += pixels # posicionamos a barrinha alguns pixels à direita
        # se a barrinha chegou ao limite direito da tela, ela não avança mais
        if self.rect.x > xTela - largura_barrinha :
            self.rect.x = xTela - largura_barrinha

    def irParaEsquerda(self, pixels, xTela):
        self.rect.x -= pixels # posicionamos a barrinha alguns pixels à esquerda
        # se a barrinha chegou ao limite esquerdo da tela, posicionamos ela no inicio da tela
        if self.rect.x < 0:
            self.rect.x = 0