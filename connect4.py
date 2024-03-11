import numpy as np
from connect4_functions import create_board, drop_piece, is_valid_location, get_next_open_row

NUM_ROW = 6
NUM_COL = 7

board = create_board()
game_over = False
turn = 0

while not game_over:
    #Player 1
    if turn == 0:
        col = int(input("Player 1, Make your selection (0-6): "))
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)

    else:
        col = int(input("Player 2, Make your selection (0-6): "))
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)


    turn+=1
    turn = turn%2



