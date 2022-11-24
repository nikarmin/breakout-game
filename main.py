import pygame as pg
import bolinha as bola

# pegando as teclas
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT, K_SPACE
)

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
pg.display.set_caption("Breakout Game")

# definindo fonte
fonte = pg.font.Font('assets/bit.ttf', 30)

# menu - sair
txtSair = fonte.render('Sair', False, (255, 255, 255), (0, 0, 0))
pSair = (screen.get_width() / 2 - txtSair.get_width() / 2, (screen.get_height() * 2) / 3 - txtSair.get_height() / 2)
btnSair = txtSair.get_rect(topleft=pSair)

# menu - jogar
txtJogar = fonte.render('Jogar', False, (255, 255, 255), (0, 0, 0))
pJogar = (screen.get_width() / 2 - txtJogar.get_width() / 2, (screen.get_height() * 2) / 4 - txtJogar.get_height() / 2)
btnJogar = txtJogar.get_rect(topleft=pJogar)

# menu - logo
fonte = pg.font.Font('assets/bit.ttf', 50)

txtLogo = fonte.render('BreakOut', False, (255, 255, 255), (0, 0, 0))
pLogo = screen.get_width() / 2 - txtLogo.get_width() / 2, screen.get_height() / 3  - txtLogo.get_height() / 2

# testando a barrinha
LARGURA_BARRINHA = 108
ALTURA_BARRINHA  = 20
barra = barrinha.Barrinha(AZUL)
barra.rect.x = X // 2 - LARGURA_BARRINHA // 2
barra.rect.y = Y - 65

clock = pg.time.Clock()
FPS = 60

# CLASSE DOS TIJOLOS

class Brick(pg.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

# CLASSE DA BOLA


# altura e largura dos tijolinhos
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16

# definindo bolinha
bolinha = bola.Bolinha(RED, 10, 10)
bolinha.rect.x = Y
bolinha.rect.y = X
    
# adicionando nas sprites

lista_sprites.add(barra)
lista_sprites.add(bolinha)

def main():
    running = True
    clock.tick(FPS)
    while running:
        screen.fill(PRETO)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if btnJogar.collidepoint(event.pos):
                            jogar()
                            running = False
                            #print('Botão "jogar" apertado!')
                            # colocar evento para iniciar a partida
                        if btnSair.collidepoint(event.pos):
                            running = False
        
        #lista_sprites.update()
                            
        screen.blit(txtLogo, pLogo)
        screen.blit(txtJogar, pJogar)
        screen.blit(txtSair, pSair)

        #pg.draw.line(screen, GREY, [0, 19], [X, 19], 40)

        #lista_sprites.draw(screen)

        pg.display.update()
        pg.display.flip()
    
    # finaliza o pygame
    pg.quit()

# método 'jogar'
def jogar():
    running = True
    clock.tick(FPS)
    while running:
        screen.fill(PRETO)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        lista_sprites.update()
        pg.draw.line(screen, GREY, [0, 19], [X, 19], 40)

        lista_sprites.draw(screen)

        pg.display.update()
        pg.display.flip()
    
    # finaliza o pygame

# método 'perdeu'
    
def perdeu():
    # arrumar
    screen.fill(PRETO)
    fonte = pg.font.Font('assets/minecraft.ttf', 100)
    txtPerdeu = fonte.render('Voce perdeu!', False, (255, 0, 0), (0, 0, 0))
    pPerdeu = (screen.get_width() / 2 - txtPerdeu.get_width() / 2, (screen.get_height() * 2) / 4 - txtPerdeu.get_height() / 2)

    # usuário escolher se quer retornar ou sair

    screen.blit(txtPerdeu, pPerdeu)
    screen.blit(txtSair, pSair)
    screen.blit(txtJogar, pJogar)

    pg.display.update()
    pg.display.flip()

if __name__ == '__main__':
    main()