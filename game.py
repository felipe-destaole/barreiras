import pygame
import os
from peao import Peao
from barreira import Barreira, OrientacaoBarreira
from enum import Enum

pygame.init()

BRANCO = (255, 255, 255)

WIDTH, HEIGTH = 900, 900
BOARD = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "board.png")), (WIDTH, HEIGTH)
)
pygame.display.set_caption("Barreirinhas")

ALTURA_BARREIRA = 20
LARGURA_BARREIRA = 140

BARREIRA_VERTICAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira_v.png")),
    (ALTURA_BARREIRA, LARGURA_BARREIRA),
)
BARREIRA_HORIZONTAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira.png")),
    (LARGURA_BARREIRA, ALTURA_BARREIRA),
)
class Turnos(Enum):
    JOGADOR_1 = 0
    JOGADOR_2 = 1


class Game:
    def __init__(self):
        self.w = WIDTH
        self.h = HEIGTH
        self.pecas = [Peao("azul", 0), Peao("vermelha", 1)]
        self.barreiras = [
            Barreira(OrientacaoBarreira.VERTICAL, (1, 1)),
            Barreira(OrientacaoBarreira.VERTICAL, (3, 5)),
            Barreira(OrientacaoBarreira.HORIZONTAL, (1, 2)),
        ]
        
        self.drag_v_1 = False
        self.drag_v_2 = False
        self.drag_h_1 = False
        self.drag_h_2 = False
        
        self.turno = Turnos.JOGADOR_1

    def run(self):
        self.win = pygame.display.set_mode((self.w, self.h))
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
                moveu = peca.mover(pos, self.pecas, self.barreiras)
                if moveu:
                    self.proximo_jogador()

            self.draw()

    def adicionar_barreira(self, keys_pressed):
        # self.
        self.barreiras.append(Barreira())

    def draw(self):
        self.win.blit(BOARD, (0, 0))
        for peca in self.pecas:
            peca.draw(self.win)

        for barreira in self.barreiras:
            barreira.draw(self.win)

        if self.turno == Turnos.JOGADOR_1:
            peca = self.pecas[0]

        if self.turno == Turnos.JOGADOR_2:
            peca = self.pecas[1]

        peca.desenhar_movimentos(self.win, self.pecas, self.barreiras)
        pygame.display.update()

    def proximo_jogador(self):
        if self.turno == Turnos.JOGADOR_1:
            self.turno = Turnos.JOGADOR_2
            return
        self.turno = Turnos.JOGADOR_1


if __name__ == "__main__":
    Game().run()
    pass
