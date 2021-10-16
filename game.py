import pygame
import os
from peao import Peao
from barreira import Barreira, BarreirasFantasma
from settings import *
from pygame import mouse

pygame.init()

pygame.display.set_caption("Barreirinhas")


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

        self.barreiras_fantasmas = [
            BarreirasFantasma(
                OrientacaoBarreira.VERTICAL,
                (WIDTH / 4, (HEIGTH + HEIGTH_BOARD + MARGEM) / 2),
            ),
            BarreirasFantasma(
                OrientacaoBarreira.HORIZONTAL,
                (WIDTH * 3 / 4, (HEIGTH + HEIGTH_BOARD + MARGEM) / 2),
            ),
            BarreirasFantasma(OrientacaoBarreira.VERTICAL, (WIDTH / 4, (MARGEM) / 2)),
            BarreirasFantasma(
                OrientacaoBarreira.HORIZONTAL, (WIDTH * 3 / 4, (MARGEM) / 2)
            ),
        ]

        self.turno = Turnos.JOGADOR_1

    def run(self):
        self.win = pygame.display.set_mode((self.w, self.h))
        clock = pygame.time.Clock()
        clock.tick()
        running = True
        while running:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                running = False
            

            if self.turno == Turnos.JOGADOR_1:
                peca = self.pecas[0]

            if self.turno == Turnos.JOGADOR_2:
                peca = self.pecas[1]

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down(peca)

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up()

            self.update_position()
            self.draw()

    def mouse_button_down(self, peca):
        pos = pygame.mouse.get_pos()
        moveu = peca.mover(pos, self.pecas, self.barreiras)
        if moveu:
            self.proximo_jogador()
        for i in range(0, len(self.barreiras_fantasmas)):
            if self.is_over(pos, self.barreiras_fantasmas[i]):
                self.barreiras_fantasmas[i].drag = True
    
    def mouse_button_up(self):
        pos = pygame.mouse.get_pos()
        for i in range(0, len(self.barreiras_fantasmas)):
            if self.is_over(pos, self.barreiras_fantasmas[i]):
                self.barreiras_fantasmas[i].drag = False

    def update_position(self):
        # Obtem a posicao atual do mouse
        mouse_pos = mouse.get_pos()

        for i in range(0, len(self.barreiras_fantasmas)):
            # Se a variavel imagem_selecionada estiver "ativa" (True), atualiza a posicao da imagem
            if self.barreiras_fantasmas[i].drag:
                # Define as posicoes X e Y da imagem, posiciona a imagem com o mouse centralizado
                self.barreiras_fantasmas[i].x = mouse_pos[0] - self.barreiras_fantasmas[i].tamanho[0]/2
                self.barreiras_fantasmas[i].y = mouse_pos[1] - self.barreiras_fantasmas[i].tamanho[1]/2

    def draw(self):
        self.win.fill(BRANCO)
        self.win.blit(BOARD, (MARGEM, MARGEM))
        for peca in self.pecas:
            peca.draw(self.win)

        for barreira in self.barreiras:
            barreira.draw(self.win)

        for barreira in self.barreiras_fantasmas:
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

    def is_over(self, mouse_pos, barreira_fantasma: BarreirasFantasma):
        # Verifica a posicao no eixo X
        if mouse_pos[0] > barreira_fantasma.x and mouse_pos[0] < barreira_fantasma.x + barreira_fantasma.tamanho[0]:
            # Verifica a posicao no eixo Y
            if mouse_pos[1] > barreira_fantasma.y and mouse_pos[1] < barreira_fantasma.y + barreira_fantasma.tamanho[1]:
                return True
        return False

if __name__ == "__main__":
    Game().run()
    pass
