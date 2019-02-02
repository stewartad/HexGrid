import pygame
from const import *


class Map:
    def __init__(self, x, y, w, h):
        self.image = pygame.Surface((w, h))
        self.rect = pygame.Rect(x, y, w, h)
        self.image.fill(GRAY)

    # draws a hex in a rectangle in which the top-left corner is at (x, y)
    def draw_hex(self, x, y, border_color=BLACK, fill_color=WHITE, border_width=3):
        col = int(x / (HEX_SIDE + HEX_H)) % 2
        vertices = [(x, y + HEX_R + (col * HEX_R)),
                    (x + HEX_H, y + (col * HEX_R)),
                    (x + HEX_H + HEX_SIDE, y + (col * HEX_R)),
                    (x + (2 * HEX_H) + HEX_SIDE, y + HEX_R + (col * HEX_R)),
                    (x + HEX_H + HEX_SIDE, y + (2 * HEX_R) + (col * HEX_R)),
                    (x + HEX_H, y + (2 * HEX_R) + (col * HEX_R))]
        pygame.draw.polygon(self.image, fill_color, vertices)
        pygame.draw.polygon(self.image, border_color, vertices, border_width)

    # draws a grid of hexes
    def draw_map(self, cols, rows):
        for i in range(rows):
            for j in range(cols):
                self.draw_hex(j * (HEX_SIDE + HEX_H), i * HEX_RECT_H)
