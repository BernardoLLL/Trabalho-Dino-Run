import pygame
import os

pygame.init()
pygame.mixer.init()

# Caminhos
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

# Configurações de Tela
largura = 640
altura = 480
BRANCO = (255, 255, 255)

# Carregamento de Assets Globais
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png'))
# Usamos o convert_alpha() após a criação da tela no main.py ou aqui se preferir.

# Sons
som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'death_sound.wav'))
som_colisao.set_volume(0.6)
som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'score_sound.wav'))
som_pontuacao.set_volume(0.5)

# Variáveis globais de controle (serão acessadas via import)
velocidade_jogo = 10
escolha_obstaculo = 0