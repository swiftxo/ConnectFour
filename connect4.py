from connect4_functions import init_game, winning_move, print_board, drop_piece, is_valid_location, get_next_open_row
from connect4_gui import init_gui, draw_board, pygame
import sys


def main():
    board, game_over, turn = init_game()
    screen = init_gui()
    draw_board(board, screen)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
            #Player 1
                if turn == 0:
                    col = int(input("Player 1, Make your selection (0-6): "))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,1)
                        if winning_move(board,1):
                            print("Player 1 Wins!")
                            game_over = True
                            

                else:
                    col = int(input("Player 2, Make your selection (0-6): "))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,2)

                        if winning_move(board,2):
                            print("Player 2 Wins!")
                            game_over = True
                            
                turn+=1
                turn = turn%2
           
if __name__ == "__main__":
    main()
