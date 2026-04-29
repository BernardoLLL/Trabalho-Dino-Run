import pygame
from pygame.locals import *
from sys import exit
from random import choice
import config
from sprites import Dino, Nuvens, Chao, Cacto, DinoVoador

tela = pygame.display.set_mode((config.largura, config.altura))
pygame.display.set_caption('DinoRun')

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    texto_formatado = fonte.render(msg, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global pontos, colidiu
    pontos = 0
    config.velocidade_jogo = 10
    colidiu = False
    dino.rect.y = config.altura - 64 - 96//2
    dino.pulo = False
    dino_voador.rect.x = config.largura
    cacto.rect.x = config.largura
    config.escolha_obstaculo = choice([0, 1])

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(config.largura * 2 // 64):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto()
dino_voador = DinoVoador()
todas_as_sprites.add(cacto)
todas_as_sprites.add(dino_voador)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(dino_voador)

relogio = pygame.time.Clock()
pontos = 0
colidiu = False

while True:
    relogio.tick(30)
    tela.fill(config.BRANCO)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not colidiu:
                if dino.rect.y == dino.pos_y_inicial:
                    dino.pular()
            if event.key == K_r and colidiu:
                reiniciar_jogo()

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

    if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
        config.escolha_obstaculo = choice([0, 1])
        cacto.rect.x = config.largura
        dino_voador.rect.x = config.largura

    if colisoes and not colidiu:
        config.som_colisao.play()
        colidiu = True

    if colidiu:
        game_over = exibe_mensagem('GAME OVER', 40, (0,0,0))
        tela.blit(game_over, (config.largura//2 - 100, config.altura//2 - 100))
        restart = exibe_mensagem('Pressione R para reiniciar', 20, (0,0,0))
        tela.blit(restart, (config.largura//2 - 100, config.altura//2 - 50))
    else:
        pontos += 1
        todas_as_sprites.update()
        
        if pontos % 100 == 0:
            config.som_pontuacao.play()
            if config.velocidade_jogo < 25:
                config.velocidade_jogo += 1

    texto_pontos = exibe_mensagem(str(pontos), 40, (0,0,0))
    todas_as_sprites.draw(tela)
    tela.blit(texto_pontos, (520, 30))

    pygame.display.flip()
