import numpy as np


def generate_board():
    board = np.zeros((12,8))
    return board

board = generate_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        selection = int(input("Player 1, make your selection (0-12): "))
    