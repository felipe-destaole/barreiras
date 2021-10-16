from enum import Enum
import pygame
import os

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)


WIDTH, HEIGTH = 700, 700
WIDTH_BOARD, HEIGTH_BOARD = 450, 450
MARGEM = int((WIDTH - WIDTH_BOARD)/2)


ALTURA_BARREIRA = 10
LARGURA_BARREIRA = 80

TAMANHO_CASA = 35

# imagens
BARREIRA_VERTICAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira_v.png")),
    (ALTURA_BARREIRA, LARGURA_BARREIRA),
)

BARREIRA_HORIZONTAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira.png")),
    (LARGURA_BARREIRA, ALTURA_BARREIRA),
)

BOARD = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "novo_board.png")), (WIDTH_BOARD, HEIGTH_BOARD)
)

PECA_VERMELHA = pygame.transform.scale(pygame.image.load(os.path.join("assets", "vermelha.png")), (TAMANHO_CASA, TAMANHO_CASA))
PECA_AZUL = pygame.transform.scale(pygame.image.load(os.path.join("assets", "azul.png")), (TAMANHO_CASA, TAMANHO_CASA))


# Enums
class Turnos(Enum):
    JOGADOR_1 = 0
    JOGADOR_2 = 1

class OrientacaoBarreira(Enum):
    HORIZONTAL = BARREIRA_HORIZONTAL
    VERTICAL = BARREIRA_VERTICAL

class Direcoes(Enum):
    CIMA = 0
    BAIXO = 1
    DIREITA = 2
    ESQUERDA = 3
    
