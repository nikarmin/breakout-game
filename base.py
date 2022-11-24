import pygame as pg

import barrinha # importando o arquivo da barrinha

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


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(PRETO)
    lista_sprites.draw(screen)
    pg.display.update()
    pg.display.flip()
    
# finaliza o pygame
pg.quit()