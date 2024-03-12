import numpy as np

NUM_ROW = 6
NUM_COL = 7


def create_board():
    board = np.zeros((NUM_ROW,NUM_COL))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board,col):
    for i in range(NUM_ROW):
        if board[i][col] == 0:
            return i
        
def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # Horizontal check
    for c in range(NUM_COL-3):
        for r in range(NUM_ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(NUM_COL):
        for r in range(NUM_ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Positive diagonal check
    for c in range(NUM_COL-3):
        for r in range(NUM_ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Negative diagonal check
    for c in range(NUM_COL-3):
        for r in range(3, NUM_ROW):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def init_game():
    board = create_board()
    game_over = False
    turn = 0
    return board, game_over, turn



