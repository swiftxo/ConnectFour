def draw_board(board, screen):
    for i in range(NUM_COL):
        for j in range(NUM_ROW):
            pygame.draw.rect(screen, PURPLE, (i*SQUARESIZE,j*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            if board[j][i] == 0:
                pygame.draw.circle(screen,BLACK, (i*SQUARESIZE+SQUARESIZE/2, j*SQUARESIZE+SQUARESIZE+SQUARESIZE/2) , RADIUS)
            elif board[j][i] == 1:
                pygame.draw.circle(screen,RED, (i*SQUARESIZE+SQUARESIZE/2, j*SQUARESIZE+SQUARESIZE+SQUARESIZE/2) , RADIUS)
            elif board[j][i] == 2:
                pygame.draw.circle(screen,YELLOW, (i*SQUARESIZE+SQUARESIZE/2, j*SQUARESIZE+SQUARESIZE+SQUARESIZE/2) , RADIUS)
            pygame.display.update()