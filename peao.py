from barreira import Barreira, OrientacaoBarreira
import pygame
from settings import *

pecas = {'vermelha': PECA_VERMELHA, 'azul': PECA_AZUL}
cores = {'vermelha': VERMELHO, 'azul': AZUL}
jogadores = [(1,3), (4,8)]

class Peao:
    def __init__(self, cor: str, numero_jogador: int):
        self.numero_jogador = numero_jogador
        self.cor = cores[cor]
        self.img = pecas[cor]
        self.x, self.y = jogadores[numero_jogador]
        self.outras = []
        self.barreiras = {'v': [], 'h':[]}
    
    def draw(self, win):
        coords = transform_coord((self.x, self.y))
        win.blit(self.img, coords)
        
    def movimentos_possiveis(self, pecas, barreiras: list[Barreira]):
        self.pos_outras(pecas)
        self.pos_barreiras(barreiras)
        movimentos = []
        # cima
        if self.x - 1 >= 0:
            movimentos.append(self.verificar_casa(Direcoes.ESQUERDA, (self.x - 1, self.y)))
        # baixo
        if self.x + 1 <= 8:
            movimentos.append(self.verificar_casa(Direcoes.DIREITA, (self.x + 1, self.y)))
        # esquerda
        if self.y - 1 >= 0:
            movimentos.append(self.verificar_casa(Direcoes.CIMA, (self.x, self.y - 1)))
        # direita
        if self.y + 1 <= 8:
            movimentos.append(self.verificar_casa(Direcoes.BAIXO, (self.x, self.y + 1)))
        
        return movimentos

    def desenhar_movimentos(self, win, pecas: list, barreiras: list[Barreira]):
        for movimento in self.movimentos_possiveis(pecas, barreiras):
            if not movimento: continue
            pos_x = MARGEM + (ALTURA_BARREIRA + TAMANHO_CASA)/2 + movimento[0] * (TAMANHO_CASA + ALTURA_BARREIRA)
            pos_y = MARGEM + (ALTURA_BARREIRA + TAMANHO_CASA)/2 + movimento[1] * (TAMANHO_CASA + ALTURA_BARREIRA)
            pygame.draw.circle(win, self.cor, (pos_x, pos_y), 7)
    
    def mover(self, pos: tuple, pecas, barreiras: list[Barreira]):
        # convertendo posição do mouse para coordenada no tabuleiro
        casa_x = (pos[0] - MARGEM) // (ALTURA_BARREIRA + TAMANHO_CASA)
        casa_y = (pos[1] - MARGEM) // (ALTURA_BARREIRA + TAMANHO_CASA)
        
        if not 0 <= casa_x <= 8 or not 0 <= casa_y <= 8:
            return
        
        movimentos_possiveis = self.movimentos_possiveis(pecas, barreiras)
        nova_pos = (casa_x, casa_y)
        
        if not nova_pos in movimentos_possiveis:
            return
        
        self.x, self.y = nova_pos
        # print((casa_x,casa_y))
        return True
    
    def pos_outras(self, pecas):
        self.outras = []
        for peca in pecas:
            if peca.numero_jogador != self.numero_jogador:
                self.outras.append((peca.x, peca.y))
        
    def pos_barreiras(self, barreiras: list[Barreira]):
        self.barreiras = {'v': [], 'h':[]}
        for barreira in barreiras:
            if barreira.orientacao == OrientacaoBarreira.VERTICAL:
                self.barreiras['v'].append((barreira.x, barreira.y))
            else:
                self.barreiras['h'].append((barreira.x, barreira.y))
    
    def verificar_casa(self, direcao: Direcoes, casa):
        # print(1, casa)  
        casa = self.verificar_barreira(direcao, casa)   
        casa = self.verificar_casa_vazia(direcao, casa) 
        # print(2, casa)  
        return casa
        
    def verificar_casa_vazia(self, direcao: Direcoes, casa: tuple):
        if not casa in self.outras:
            return casa
        
        x, y = casa
        if direcao == Direcoes.ESQUERDA and x + 1 <= 8:
            return (x - 1, y)
            
        if direcao == Direcoes.DIREITA and x - 1 >= 0:
            return (x + 1, y)
        
        if direcao == Direcoes.CIMA and y + 1 <= 8:
            return (x, y - 1)
            
        if direcao == Direcoes.BAIXO and y - 1 >= 0:
            return (x, y + 1)
    
    def verificar_barreira(self, direcao: Direcoes, casa):    
        if direcao == Direcoes.CIMA and ((self.x, self.y-1) in self.barreiras['h'] or (self.x-1, self.y-1) in self.barreiras['h']):
            return
        if direcao == Direcoes.BAIXO and ((self.x, self.y) in self.barreiras['h'] or (self.x-1, self.y) in self.barreiras['h']):
            return
        if direcao == Direcoes.ESQUERDA and ((self.x, self.y) in self.barreiras['v'] or (self.x, self.y-1) in self.barreiras['v']):
            return
        if direcao == Direcoes.DIREITA and ((self.x+1, self.y) in self.barreiras['v'] or (self.x+1, self.y-1) in self.barreiras['v']):
            return
        return casa
        
def transform_coord(coord: tuple) -> tuple:
    pos_x = MARGEM + ALTURA_BARREIRA/2 + coord[0] * (TAMANHO_CASA + ALTURA_BARREIRA)
    pos_y = MARGEM + ALTURA_BARREIRA/2 + coord[1] * (TAMANHO_CASA + ALTURA_BARREIRA)
    return (pos_x, pos_y)


