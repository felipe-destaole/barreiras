import pygame
import os

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---ALTURA_BARREIRA = 20
WIN_WIDTH, WIN_HEIGTH = 900, 900
MARGEM = int(WIN_WIDTH * 0.1)
TAMANHO_CASA = 60
ALTURA_BARREIRA = 20
LARGURA_BARREIRA = 140

# BARREIRA_VERTICAL_FANTASMA = pygame.transform.scale(
#     pygame.image.load(os.path.join("assets", "Barreira_v.png")),
#     (ALTURA_BARREIRA, LARGURA_BARREIRA),
# )
BARREIRA_VERTICAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira_v.png")),
    (ALTURA_BARREIRA, LARGURA_BARREIRA),
).convert_alpha()

# BARREIRA_HORIZONTAL_FANTASMA = pygame.transform.scale(
#     pygame.image.load(os.path.join("assets", "Barreira.png")),
#     (LARGURA_BARREIRA, ALTURA_BARREIRA),
# )
BARREIRA_HORIZONTAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Barreira.png")),
    (LARGURA_BARREIRA, ALTURA_BARREIRA),
).convert_alpha()


# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -

rectangle = BARREIRA_VERTICAL
new_rect = BARREIRA_VERTICAL
rectangle_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    new_rect = BARREIRA_VERTICAL
                    mouse_x, mouse_y = event.pos
                    offset_x = new_rect.x - mouse_x
                    offset_y = new_rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                new_rect.x = mouse_x + offset_x
                new_rect.y = mouse_y + offset_y

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    screen.blit(screen, RED, rectangle)
    screen.blit(screen, RED, new_rect)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()