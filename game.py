import pygame
import os
from peao import Peao
from enum import Enum

pygame.init()

BRANCO = (255,255,255)

WIDTH, HEIGTH = 900, 900
BOARD = pygame.transform.scale(pygame.image.load(os.path.join("assets", "board.png")), (WIDTH, HEIGTH))

class Turnos(Enum):
    JOGADOR_1 = 0
    JOGADOR_2 = 1
    

class Game:
    def __init__(self):
        self.w = WIDTH
        self.h = HEIGTH
        self.pecas = [Peao('azul', 0), Peao('vermelha', 1)]
        self.turno = Turnos.JOGADOR_1
    
    def run(self):
        self.win = pygame.display.set_mode((self.w,self.h))
        clock = pygame.time.Clock()
        clock.tick()
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            
            if self.turno == Turnos.JOGADOR_1:
                peca = self.pecas[0]
                
            if self.turno == Turnos.JOGADOR_2:
                peca = self.pecas[1]
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                peca.mover(pos)
                
            self.draw()
            # self.mover(0,0)
    
    def draw(self):
        self.win.blit(BOARD, (0,0))
        for peca in self.pecas:
            peca.draw(self.win)
        
        if self.turno == Turnos.JOGADOR_1:
            peca = self.pecas[0]
            
        if self.turno == Turnos.JOGADOR_2:
            peca = self.pecas[1]
            
        peca.desenhar_movimentos(self.win)
        pygame.display.update()


if __name__ == '__main__':
    Game().run()
    pass
    