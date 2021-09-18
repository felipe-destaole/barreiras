import pygame
import os
from peao import Peao

pygame.init()

BRANCO = (255,255,255)

WIDTH, HEIGTH = 900, 900
BOARD = pygame.transform.scale(pygame.image.load(os.path.join("assets", "board.png")), (WIDTH, HEIGTH))

class Game:
    def __init__(self):
        self.w = WIDTH
        self.h = HEIGTH
        self.pecas = [Peao('azul', 0), Peao('vermelha', 1)]
    
    def run(self):
        self.win = pygame.display.set_mode((self.w,self.h))
        clock = pygame.time.Clock()
        clock.tick()
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            self.draw()
    
    def draw(self):
        self.win.blit(BOARD, (0,0))
        for peca in self.pecas:
            peca.draw(self.win)
        pygame.display.update()


if __name__ == '__main__':
    Game().run()
    pass
    