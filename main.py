import pygame as pg
from barrinha import Barrinha
from bolinha import Bolinha
from tijolinho import Tijolinho

# import time as tm
# import RPi.GPIO as gp
# high = gp.HIGH
# low = gp.LOW
# p0 = 17

# gp.setmode(gp.BCM)
# gp.setup(p0, gp.OUT, initial=high)

pg.init()
pg.mixer.init()

pg.mixer.music.load("./sounds/background_grandefamilia.mp3")
pg.mixer.music.play(loops=-1)

AZUL = (0, 97, 148)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (212, 210, 212)
VERMELHO = (162, 8, 0)
LARANJA = (183, 119, 0)
VERDE = (0, 127, 33)
AMARELO = (197, 199, 37)

pontos = 0
bolas = 3

X = 800
Y = 600

size = (800, 600)
screen = pg.display.set_mode(size)

pg.display.set_caption("Breakout Game")

# definindo fonte
fonte = pg.font.Font('assets/bit.ttf', 30)

# menu - sair
txtSair = fonte.render('Sair', False, (255, 255, 255), (0, 0, 0))
pSair = (screen.get_width() / 2 - txtSair.get_width() / 2,
         (screen.get_height() * 2) / 3 - txtSair.get_height() / 2)
btnSair = txtSair.get_rect(topleft=pSair)

# menu - jogar
txtJogar = fonte.render('Jogar', False, (255, 255, 255), (0, 0, 0))
pJogar = (screen.get_width() / 2 - txtJogar.get_width() / 2,
          (screen.get_height() * 2) / 4 - txtJogar.get_height() / 2)
btnJogar = txtJogar.get_rect(topleft=pJogar)

# menu - logo
fonte = pg.font.Font('assets/bit.ttf', 50)

txtLogo = fonte.render('BreakOut', False, (255, 255, 255), (0, 0, 0))
pLogo = screen.get_width() / 2 - txtLogo.get_width() / \
    2, screen.get_height() / 3 - txtLogo.get_height() / 2


lista_sprites = pg.sprite.Group()

LARGURA_BARRINHA = 108
ALTURA_BARRINHA = 20

jogador = Barrinha(AZUL, LARGURA_BARRINHA, ALTURA_BARRINHA)
jogador.rect.x = X // 2 - LARGURA_BARRINHA // 2
jogador.rect.y = Y - 65

bolinha = Bolinha((221, 142, 0), 20, 20)
bolinha.rect.x = X // 2 - 5
bolinha.rect.y = Y // 2 - 5

todos_tijolinhos = pg.sprite.Group()

for i in range(7):
    tijolinho = Tijolinho(LARANJA, 80, 30)
    tijolinho.rect.x = 60 + i * 100
    tijolinho.rect.y = 60
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)


for i in range(7):
    tijolinho = Tijolinho(AZUL, 80, 30)
    tijolinho.rect.x = 60 + i * 100
    tijolinho.rect.y = 100
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)

for i in range(7):
    tijolinho = Tijolinho(VERDE, 80, 30)
    tijolinho.rect.x = 60 + i * 100
    tijolinho.rect.y = 140
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)

for i in range(7):
    tijolinho = Tijolinho(AMARELO, 80, 30)
    tijolinho.rect.x = 60 + i * 100
    tijolinho.rect.y = 180
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)

for i in range(7):
    tijolinho = Tijolinho(VERMELHO, 80, 30)
    tijolinho.rect.x = 60 + i * 100
    tijolinho.rect.y = 220
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)

lista_sprites.add(jogador)
lista_sprites.add(bolinha)

cronometro = pg.time.Clock()

def main():
    jogando = True
    pontos = 0
    bolas = 3

    while jogando:
        screen.fill(PRETO)

        # screen.blit(txtLogo, pLogo)
        # screen.blit(txtJogar, pJogar)
        # screen.blit(txtSair, pSair)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                jogando = False
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         if btnJogar.collidepoint(event.pos):
            #             jogar(bolas, pontos)
            #             jogando = False
            #             #print('Botão "jogar" apertado!')
            #             # colocar evento para iniciar a partida
            #         if btnSair.collidepoint(event.pos):
            #             jogando = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            jogador.irEsquerda(5)
        if keys[pg.K_RIGHT]:
            jogador.irDireita(5)

        lista_sprites.update()

        if bolinha.rect.x >= 790:
            bolinha.velocity[0] = -bolinha.velocity[0]
        if bolinha.rect.x <= 0:
            bolinha.velocity[0] = -bolinha.velocity[0]
        if bolinha.rect.y > 590:
            bolinha.velocity[1] = -bolinha.velocity[1]
            bolas -= 1
            #gp.output(p0, high)
            if bolas == 0:
                font = pg.font.Font('assets/bit.ttf', 74)
                text = font.render("GAME OVER", 1, BRANCO)
                text_rect = text.get_rect(center=(X / 2, Y / 2))
                screen.blit(text, text_rect)
                pg.display.flip()
                pg.time.wait(3000)
                jogando = False

        if bolinha.rect.y < 40:
            bolinha.velocity[1] = -bolinha.velocity[1]

        if pg.sprite.collide_mask(bolinha, jogador):
            bolinha.rect.x -= bolinha.velocity[0]
            bolinha.rect.y -= bolinha.velocity[1]
            bolinha.bounce()

        lista_colisao_tijolinhos = pg.sprite.spritecollide(
            bolinha, todos_tijolinhos, False)

        for tijolinho in lista_colisao_tijolinhos:
            bolinha.bounce()
            pontos += 1
            tijolinho.kill()
            if len(todos_tijolinhos) == 0:
                font = pg.font.Font('assets/bit.ttf', 74)
                text.font.render("WIN", 1, BRANCO)
                text_rect = text.get_rect(center=(X / 2, Y / 2))
                screen.blit(text, text_rect)
                pg.display.flip()
                pg.time.wait(3000)
                jogando = False

        screen.fill(PRETO)

        font = pg.font.Font('assets/bit.ttf', 20)
        text = font.render("Pontos: " + str(pontos), True, BRANCO, (0, 0, 0))
        screen.blit(text, (20, 360))
        text = font.render("Vidas: " + str(bolas), True, BRANCO, (0, 0, 0))
        screen.blit(text, (20, 400))

        lista_sprites.draw(screen)
        pg.display.flip()

        cronometro.tick(60)

        pg.display.update()
       # pg.display.flip()

    # finaliza o pygame
    pg.quit()


# def jogar(bolas, pontos):
#     # for event in pg.event.get():
#     #     if event.type == pg.QUIT:
#     #         jogando = False
#     jogando = True
#     while jogando:
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT]:
#             jogador.irEsquerda(5)
#         if keys[pg.K_RIGHT]:
#             jogador.irDireita(5)

#         lista_sprites.update()

#         if bolinha.rect.x >= 790:
#             bolinha.velocity[0] = -bolinha.velocity[0]
#         if bolinha.rect.x <= 0:
#             bolinha.velocity[0] = -bolinha.velocity[0]
#         if bolinha.rect.y > 590:
#             bolinha.velocity[1] = -bolinha.velocity[1]
#             bolas -= 1
#             #gp.output(p0, high)
#             if bolas == 0:
#                 font = pg.font.Font('assets/bit.ttf', 74)
#                 text = font.render("GAME OVER", 1, BRANCO)
#                 text_rect = text.get_rect(center=(X / 2, Y / 2))
#                 screen.blit(text, text_rect)
#                 pg.display.flip()
#                 pg.time.wait(3000)
#                 jogando = False

#         if bolinha.rect.y < 40:
#             bolinha.velocity[1] = -bolinha.velocity[1]

#         if pg.sprite.collide_mask(bolinha, jogador):
#             bolinha.rect.x -= bolinha.velocity[0]
#             bolinha.rect.y -= bolinha.velocity[1]
#             bolinha.bounce()

#         lista_colisao_tijolinhos = pg.sprite.spritecollide(
#             bolinha, todos_tijolinhos, False)

#         for tijolinho in lista_colisao_tijolinhos:
#             bolinha.bounce()
#             pontos += 1
#             tijolinho.kill()
#             if len(todos_tijolinhos) == 0:
#                 font = pg.font.Font('assets/bit.ttf', 74)
#                 text.font.render("WIN", 1, BRANCO)
#                 text_rect = text.get_rect(center=(X / 2, Y / 2))
#                 screen.blit(text, text_rect)
#                 pg.display.flip()
#                 pg.time.wait(3000)
#                 jogando = False

#         screen.fill(PRETO)

#         font = pg.font.Font('assets/bit.ttf', 20)
#         text = font.render("Pontos: " + str(pontos), True, BRANCO, (0, 0, 0))
#         screen.blit(text, (20, 360))
#         text = font.render("Vidas: " + str(bolas), True, BRANCO, (0, 0, 0))
#         screen.blit(text, (20, 400))

#         lista_sprites.draw(screen)
#         pg.display.flip()

#         cronometro.tick(60)


# def menu(jogando):
#     screen.fill(PRETO)
#     screen.blit(txtLogo, pLogo)
#     screen.blit(txtJogar, pJogar)
#     screen.blit(txtSair, pSair)

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 if btnJogar.collidepoint(event.pos):
#                     jogar(jogando, bolas, pontos)
#                     pg.quit()
#                 # print('Botão "jogar" apertado!')
#                 # colocar evento para iniciar a partida
#                 if btnSair.collidepoint(event.pos):
#                     pg.quit()

#     pg.display.update()
#     pg.display.flip()


# while jogando:
#     # menu(jogando)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             jogando = False

#     keys = pg.key.get_pressed()
#     if keys[pg.K_LEFT]:
#         jogador.irEsquerda(5)
#     if keys[pg.K_RIGHT]:
#         jogador.irDireita(5)

#     lista_sprites.update()

#     if bolinha.rect.x >= 790:
#         bolinha.velocity[0] = -bolinha.velocity[0]
#     if bolinha.rect.x <= 0:
#         bolinha.velocity[0] = -bolinha.velocity[0]
#     if bolinha.rect.y > 590:
#         bolinha.velocity[1] = -bolinha.velocity[1]
#         bolas -= 1
#         #gp.output(p0, high)
#         if bolas == 0:
#             font = pg.font.Font('assets/bit.ttf', 74)
#             text = font.render("GAME OVER", 1, BRANCO)
#             text_rect = text.get_rect(center=(X / 2, Y / 2))
#             screen.blit(text, text_rect)
#             pg.display.flip()
#             pg.time.wait(3000)
#             jogando = False

#     if bolinha.rect.y < 40:
#         bolinha.velocity[1] = -bolinha.velocity[1]

#     if pg.sprite.collide_mask(bolinha, jogador):
#         bolinha.rect.x -= bolinha.velocity[0]
#         bolinha.rect.y -= bolinha.velocity[1]
#         bolinha.bounce()

#     lista_colisao_tijolinhos = pg.sprite.spritecollide(
#         bolinha, todos_tijolinhos, False)

#     for tijolinho in lista_colisao_tijolinhos:
#         bolinha.bounce()
#         pontos += 1
#         tijolinho.kill()
#         if len(todos_tijolinhos) == 0:
#             font = pg.font.Font('assets/bit.ttf', 74)
#             text.font.render("WIN", 1, BRANCO)
#             text_rect = text.get_rect(center=(X / 2, Y / 2))
#             screen.blit(text, text_rect)
#             pg.display.flip()
#             pg.time.wait(3000)
#             jogando = False

#     screen.fill(PRETO)

#     font = pg.font.Font('assets/bit.ttf', 20)
#     text = font.render("Pontos: " + str(pontos), True, BRANCO, (0, 0, 0))
#     screen.blit(text, (20, 360))
#     text = font.render("Vidas: " + str(bolas), True, BRANCO, (0, 0, 0))
#     screen.blit(text, (20, 400))

#     lista_sprites.draw(screen)
#     pg.display.flip()

#     cronometro.tick(60)

# pg.quit()


# def menu():
#     screen.fill(PRETO)
#     screen.blit(txtLogo, pLogo)
#     screen.blit(txtJogar, pJogar)
#     screen.blit(txtSair, pSair)

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 if btnJogar.collidepoint(event.pos):
#                     jogar(bolas, pontos)
#                     pg.quit()
#                 # print('Botão "jogar" apertado!')
#                 # colocar evento para iniciar a partida
#                 if btnSair.collidepoint(event.pos):
#                     pg.quit()

#     pg.display.update()
#     pg.display.flip()

# finaliza o pygame
# pg.quit()


# def jogar(jogando, bolas, pontos):
#     keys = pg.key.get_pressed()

#     if keys[pg.K_LEFT]:
#         jogador.irEsquerda(5)

#     if keys[pg.K_RIGHT]:
#         jogador.irDireita(5)

#     lista_sprites.update()

#     if bolinha.rect.x >= 790:
#         bolinha.velocity[0] = -bolinha.velocity[0]
#     if bolinha.rect.x <= 0:
#         bolinha.velocity[0] = -bolinha.velocity[0]
#     if bolinha.rect.y > 590:
#         bolinha.velocity[1] = -bolinha.velocity[1]
#         bolas += 1
#     #gp.output(p0, high)
#         if bolas == 4:
#             font = pg.font.Font('assets/bit.ttf', 74)
#             text = font.render("MORREU :(", 1, BARRINHA)
#             screen.blit(text, (250, 300))
#             pg.display.flip()
#             pg.time.wait(3000)
#             jogando = False

#     if bolinha.rect.y < 40:
#         bolinha.velocity[1] = -bolinha.velocity[1]

#     if pg.sprite.collide_mask(bolinha, jogador):
#         bolinha.rect.x -= bolinha.velocity[0]
#         bolinha.rect.y -= bolinha.velocity[1]
#         bolinha.bounce()

#     lista_colisao_tijolinhos = pg.sprite.spritecollide(
#         bolinha, todos_tijolinhos, False)
#     for tijolinho in lista_colisao_tijolinhos:
#         bolinha.bounce()
#         pontos += 1
#         tijolinho.kill()
#         if len(todos_tijolinhos) == 0:
#             font = pg.font.Font('assets/bit.ttf', 74)
#             text.font.render("MANDOU MUITO :)", 1, BARRINHA)
#             screen.blit(text, (200, 300))
#             pg.display.flip()
#             pg.time.wait(3000)
#             jogando = False

#     screen.fill(PRETO)

#     font = pg.font.Font('assets/bit.ttf', 20)
#     text = font.render("Pontos: " + str(pontos), True, BRANCO, (0, 0, 0))
#     screen.blit(text, (20, 360))
#     text = font.render("bolas: " + str(bolas), True, BRANCO, (0, 0, 0))
#     screen.blit(text, (20, 400))

#     lista_sprites.draw(screen)
#     pg.display.flip()

#     cronometro.tick(60)

if __name__ == '__main__':
    main()