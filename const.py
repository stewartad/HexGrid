import math

# Window Dimensions
WIN_W = 800
WIN_H = 600
CENTER_X = WIN_W / 2
CENTER_Y = WIN_H / 2

# Map Dimensions
MAP_W = 400
MAP_H = 400
MAP_X = 0
MAP_Y = 0
HEXES_ACROSS = 11
HEXES_DOWN = 8

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_BLUE = (64, 64, 224)
PINK = (236,8,223)
CLEAR = (0, 0, 0, 0)
DARKGRAY = (64,  64,  64)
GRAY = (128, 128, 128)
LIGHTGRAY = (212, 208, 200)

# Hex Dimensions
HEX_SIDE = 40
HEX_H = math.ceil(math.sin(math.radians(30)) * HEX_SIDE)
HEX_R = math.ceil(math.cos(math.radians(30)) * HEX_SIDE)
HEX_RECT_W = HEX_SIDE + (2 * HEX_H)
HEX_RECT_H = 2 * HEX_R
HEX_GRID = [['T', 'T', 'T', 'T'],
            ['T', 'T', 'T', 'T'],
            ['T', 'T', 'T', 'T'],
            ['T', 'T', 'T', 'T']]