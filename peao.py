import pygame
import os

WIN_WIDTH, WIN_HEIGTH = 900, 900
MARGEM = int(WIN_WIDTH*.1)
TAMANHO_CASA = 60 
TAMANHO_BARREIRA = 20

PECA_VERMELHA = pygame.transform.scale(pygame.image.load(os.path.join("assets", "vermelha.png")), (TAMANHO_CASA, TAMANHO_CASA))
PECA_AZUL = pygame.transform.scale(pygame.image.load(os.path.join("assets", "azul.png")), (TAMANHO_CASA, TAMANHO_CASA))

VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

pecas = {'vermelha': PECA_VERMELHA, 'azul': PECA_AZUL}
cores = {'vermelha': VERMELHO, 'azul': AZUL}
jogadores = [(4,0), (4,8)]

class Peao:
    def __init__(self, cor: str, numero_jogador: int):
        self.cor = cores[cor]
        self.img = pecas[cor]
        self.x, self.y = jogadores[numero_jogador]
        print(transform_coord((self.x - 1, self.y)))
    
    def draw(self, win):
        coords = transform_coord((self.x, self.y))
        win.blit(self.img, coords)
        
    def movimentos_possiveis(self):
        movimentos = []
        # cima
        if self.x - 1 >= 0:
            movimentos.append((self.x - 1, self.y))
        # baixo
        if self.x + 1 <= 8:
            movimentos.append((self.x + 1, self.y))
        # esquerda
        if self.y - 1 >= 0:
            movimentos.append((self.x, self.y - 1))
        # direita
        if self.y + 1 <= 8:
            movimentos.append((self.x, self.y + 1))
        
        return movimentos

    def desenhar_movimentos(self, win):
        for movimento in self.movimentos_possiveis():
            pos_x = MARGEM + (TAMANHO_BARREIRA + TAMANHO_CASA)/2 + movimento[0] * (TAMANHO_CASA + TAMANHO_BARREIRA)
            pos_y = MARGEM + (TAMANHO_BARREIRA + TAMANHO_CASA)/2 + movimento[1] * (TAMANHO_CASA + TAMANHO_BARREIRA)
            pygame.draw.circle(win, self.cor, (pos_x, pos_y), 10)
    
    def mover(self, pos: tuple):
        # convertendo posição do mouse para coordenada no tabuleiro
        casa_x = (pos[0] - MARGEM) // (TAMANHO_BARREIRA + TAMANHO_CASA)
        casa_y = (pos[1] - MARGEM) // (TAMANHO_BARREIRA + TAMANHO_CASA)
        
        if not 0 <= casa_x <= 8 or not 0 <= casa_y <= 8:
            return
        
        movimentos_possiveis = self.movimentos_possiveis()
        nova_pos = (casa_x, casa_y)
        
        if not nova_pos in movimentos_possiveis:
            return
        
        self.x, self.y = nova_pos
        print((casa_x,casa_y))
        return True

        
        
        
def transform_coord(coord: tuple) -> tuple:
    pos_x = MARGEM + TAMANHO_BARREIRA/2 + coord[0] * (TAMANHO_CASA + TAMANHO_BARREIRA)
    pos_y = MARGEM + TAMANHO_BARREIRA/2 + coord[1] * (TAMANHO_CASA + TAMANHO_BARREIRA)
    return (pos_x, pos_y)