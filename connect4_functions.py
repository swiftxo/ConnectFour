import numpy as np

def create_board():
    board = np.zeros((NUM_ROW,NUM_COL))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] == piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    for i in range(NUM_ROW):
        if board[i][col] == 0:
            return i