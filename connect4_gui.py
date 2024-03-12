import pygame
from connect4_functions import NUM_COL,NUM_ROW

SQUARESIZE = 100
BLACK = (0,0,0)
PURPLE = (25,8,86)
width = NUM_COL * SQUARESIZE
height = (NUM_ROW+1) * SQUARESIZE
size = (width,height)
RADIUS = int(SQUARESIZE/2 - 6)

def init_gui():
    pygame.init()
    screen = pygame.display.set_mode(size)
    return screen

def draw_board(board, screen):
    for i in range(NUM_COL):
        for j in range(NUM_ROW):
            pygame.draw.rect(screen, PURPLE, (i*SQUARESIZE,j*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circ(screen,BLACK,)


