import pygame as pg
import bolinha   # importando o arquivo da bolinha
import barrinha  # importando o arquivo da barrinha
import tijolo    # importando o arquivo dos tijolos

# pegando as teclas
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT, K_SPACE
)

pg.init()       # iniciando o jogo
pg.mixer.init()  # iniciando o mixer (para sons)

# definindo largura e altura da tela
X = 800
Y = 700
size = (X, Y)

# definindo cores
AZUL = (0, 97, 148)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (212, 210, 212)
VERMELHO = (162, 8, 0)
LARANJA = (183, 119, 0)
VERDE = (0, 127, 33)
AMARELO = (197, 199, 37)

pontuacao = 0 # pontuacao do jogo
velocity = 4
bolas = 1

# definindo o grupo das sprites que serão exibidas na tela
lista_sprites = pg.sprite.Group()

# define a janela
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

# definindo a barrinha
LARGURA_BARRINHA = 108
ALTURA_BARRINHA = 20
barra = barrinha.Barrinha(AZUL, LARGURA_BARRINHA, ALTURA_BARRINHA)
barra.rect.x = X // 2 - LARGURA_BARRINHA // 2
barra.rect.y = Y - 65

clock = pg.time.Clock()
FPS = 60

# definindo bolinha
bolinha = bolinha.Bolinha((221, 142, 0), 20, 20)
bolinha.rect.x = X // 2 - 5
bolinha.rect.y = Y // 2 - 5

# definindo a lista de tijolos
lista_tijolos = pg.sprite.Group()

# altura e largura dos tijolinhos
LARGURA_TIJOLO = 55
ALTURA_TIJOLO  = 16
x_gap = 7
y_gap = 5
LARGURA_PAREDE = 16

def bricks():
    for coluna in range(8):
        for linha in range(14):
            if coluna < 2:
                if linha == 0:
                    brick = tijolo.Tijolo(VERMELHO, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
                else:
                    brick = tijolo.Tijolo(VERMELHO, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE + LARGURA_TIJOLO + x_gap + (linha - 1) * (LARGURA_TIJOLO + x_gap)
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
            if 1 < coluna < 4:
                if linha == 0:
                    brick = tijolo.Tijolo(LARANJA, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO) 
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
                else:
                    brick = tijolo.Tijolo(LARANJA, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE + LARGURA_TIJOLO + x_gap + (linha - 1) * (LARGURA_TIJOLO + x_gap)
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO) 
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
            if 3 < coluna < 6:
                if linha == 0:
                    brick = tijolo.Tijolo(VERDE, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
                else:
                    brick = tijolo.Tijolo(VERDE, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE + LARGURA_TIJOLO + x_gap + (linha - 1) * (LARGURA_TIJOLO + x_gap)
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
            if 5 < coluna < 8:
                if linha == 0:
                    brick = tijolo.Tijolo(AMARELO, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)
                else:
                    brick = tijolo.Tijolo(AMARELO, LARGURA_TIJOLO, ALTURA_TIJOLO)
                    brick.rect.x = LARGURA_PAREDE + LARGURA_TIJOLO + x_gap + (linha - 1) * (LARGURA_TIJOLO + x_gap)
                    brick.rect.y = 215 + coluna * (y_gap + ALTURA_TIJOLO)
                    lista_sprites.add(brick)
                    lista_tijolos.add(brick)

parede_de_tijolos = bricks()

# adicionando as sprites nas listas
lista_sprites.add(barra)
lista_sprites.add(bolinha)

def main():
    running = True
    clock.tick(FPS)
    while running:
        screen.fill(PRETO)

        screen.blit(txtLogo, pLogo)
        screen.blit(txtJogar, pJogar)
        screen.blit(txtSair, pSair)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if btnJogar.collidepoint(event.pos):
                        jogar(pontuacao, bolas)
                        running = False
                        #print('Botão "jogar" apertado!')
                        # colocar evento para iniciar a partida
                    if btnSair.collidepoint(event.pos):
                        running = False

        pg.display.update()
        pg.display.flip()

    # finaliza o pygame
    pg.quit()

# método 'jogar'
def jogar(pontuacao, bolinhas):
    step = 0
    
    running = True
    clock.tick(FPS)

    font = pg.font.Font('assets/minecraft.ttf', 20)
    string = "bolas : " + str(bolinhas)
    contBolas = font.render(string, True, BRANCO, (0, 0, 0))
    contBolas_posicao = contBolas.get_rect()
    contBolas_posicao.center = (50, 360)

    while running:
        screen.fill(PRETO)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            barra.irParaEsquerda(2)
        if teclas[pg.K_RIGHT]:
            barra.irParaDireita(2, X)

        lista_sprites.update()

        if bolinha.rect.y < 40:
            bolinha.velocity[1] = -bolinha.velocity[1]

        if bolinha.rect.x >= X - LARGURA_PAREDE - 10:
            bolinha.velocity[0] = -bolinha.velocity[0]

        if bolinha.rect.x <= LARGURA_PAREDE:
            bolinha.velocity[0] = -bolinha.velocity[0]

        if bolinha.rect.y > Y:
            bolinha.rect.x = X // 2 - 5
            bolinha.rect.y = Y // 2 - 5
            bolinha.velocity[1] = bolinha.velocity[1]
            bolinhas += 1
            if bolinhas == 4:
                font = pg.font.Font('assets/minecraft.ttf', 70)
                text = font.render("Voce perdeu!", 1, VERMELHO)
                text_rect = text.get_rect(center=(X / 2, Y / 3))
                screen.blit(text, text_rect)
                screen.blit(txtSair, pSair)
                screen.blit(txtJogar, pJogar)
                pg.display.update()
                pg.time.wait(2000)
                pg.quit()

        if pg.sprite.collide_mask(bolinha, barra):
            bolinha.rect.x += bolinha.velocity[0]
            bolinha.rect.y -= bolinha.velocity[1]
            bolinha.balancar()

        colisoes_com_tijolo = pg.sprite.spritecollide(bolinha, lista_tijolos, False)
        for tijolo in colisoes_com_tijolo:
            bolinha.balancar()
            if len(colisoes_com_tijolo) > 0:
                step += 1
                for i in range (0, 448, 28):
                    if step == i:
                        bolinha.velocity[0] += 1
                        bolinha.velocity[1] += 1
            if 380.5 > tijolo.rect.y > 338.5:
                pontuacao += 1 
                tijolo.kill()
            elif 338.5 > tijolo.rect.y > 294:
                pontuacao += 3
                tijolo.kill()
            elif 294 > tijolo.rect.y > 254.5:
                pontuacao += 5
                tijolo.kill()
            else:
                pontuacao += 7
                tijolo.kill()
            if len(lista_tijolos) == 0:
                texto = "Vitória"
                texto_pontuacao = "Você fez " + pontuacao + " pontos!"
                ganhou = font.render(texto, True, AZUL, (0, 0, 0))
                pontos = font.render(texto_pontuacao, True, BRANCO, (0, 0, 0))
                

        pg.draw.line(screen, CINZA, [0, 19], [X, 19], 40)

        string = "bolas : " + str(bolas)
        contBolas = font.render(string, True, BRANCO, (0, 0, 0))
        screen.blit(contBolas, contBolas_posicao)

        lista_sprites.draw(screen)

        pg.display.update()
        pg.display.flip()

    # finaliza o pygame


if __name__ == '__main__':
    main()
