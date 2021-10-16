import pygame
import os
from enum import Enum
from settings import *


class Barreira:
    def __init__(self, orientacao: OrientacaoBarreira, coordenadas: tuple):
        self.x, self.y = coordenadas
        self.orientacao = orientacao
        self.img = orientacao.value

    def draw(self, win):
        coords = self.converter_coords((self.x, self.y))
        win.blit(self.img, coords)

    def converter_coords(self, coords: tuple):
        if self.orientacao == OrientacaoBarreira.HORIZONTAL:
            pos_x = (
                MARGEM
                + ALTURA_BARREIRA / 2
                + (TAMANHO_CASA + ALTURA_BARREIRA) * coords[0]
            )
            pos_y = (
                MARGEM
                + ALTURA_BARREIRA / 2
                + (TAMANHO_CASA + ALTURA_BARREIRA) * coords[1]
                + TAMANHO_CASA
            )
            return (pos_x, pos_y)
        if self.orientacao == OrientacaoBarreira.VERTICAL:
            pos_x = (
                MARGEM
                + ALTURA_BARREIRA / 2
                + (TAMANHO_CASA + ALTURA_BARREIRA) * coords[0]
                - ALTURA_BARREIRA
            )
            pos_y = (
                MARGEM
                + ALTURA_BARREIRA / 2
                + (TAMANHO_CASA + ALTURA_BARREIRA) * coords[1]
            )
            return (pos_x, pos_y)


class BarreirasFantasma:
    def __init__(self, orientacao: OrientacaoBarreira, coordenadas: tuple):
        self.x, self.y = coordenadas
        self.orientacao = orientacao
        self.img = orientacao.value
        self.drag = False
        self.tamanho = (
            [LARGURA_BARREIRA, ALTURA_BARREIRA]
            if orientacao == OrientacaoBarreira.HORIZONTAL
            else [ALTURA_BARREIRA, LARGURA_BARREIRA]
        )

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
