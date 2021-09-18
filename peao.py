import pygame
import os

WIN_WIDTH, WIN_HEIGTH = 900, 900
MARGEM = int(WIN_WIDTH*.1)
TAMANHO_CASA = 60 
TAMANHO_BARREIRA = 20
VERMELHA = pygame.transform.scale(pygame.image.load(os.path.join("assets", "vermelha.png")), (TAMANHO_CASA, TAMANHO_CASA))
AZUL = pygame.transform.scale(pygame.image.load(os.path.join("assets", "azul.png")), (TAMANHO_CASA, TAMANHO_CASA))

cores = {'vermelha': VERMELHA, 'azul': AZUL}
jogadores = [(4,0), (4,8)]

class Peao:
    def __init__(self, cor: str, numero_jogador: int):
        self.img = cores[cor]
        self.x, self.y = jogadores[numero_jogador]
    
    def draw(self, win):
        pos_x = MARGEM + TAMANHO_BARREIRA/2 + self.x * (TAMANHO_CASA + TAMANHO_BARREIRA)
        pos_y = MARGEM + TAMANHO_BARREIRA/2 + self.y * (TAMANHO_CASA + TAMANHO_BARREIRA)
        win.blit(self.img, (pos_x, pos_y))