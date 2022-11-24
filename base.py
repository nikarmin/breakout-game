import pygame as pg

pg.init()

x = 1280
y = 720

# define a janela

screen = pg.display.set_mode((x, y), pg.RESIZABLE)
pg.display.set_caption("Breakout game")

# carregando uma imagem do disco, neste caso, png


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pg.display.flip()

# finaliza o pygame
pg.quit()