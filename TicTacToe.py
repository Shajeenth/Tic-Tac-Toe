import pygame

state = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]

class TicTacToe:
    board = pygame.image.load('tic_tac_toe.png')    
    img_x = pygame.image.load('x.png')
    img_o = pygame.image.load('o.png')
    ind_x = pygame.image.load('x_indicator.png')
    ind_o = pygame.image.load('o_indicator.png')
    xwin = pygame.image.load('Xwin.png')
    owin = pygame.image.load('Owin.png')

    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.o_win = False
        self.x_win = False

    # These functions return 0, 1 or 2
    def check_horizontal(self):
        for i in self.state:
            print(i)
            if all(element == 1 for element in i):
                return 1
            elif all(element == 2 for element in i):
                return 2
        return 0
    
    def check_vertical(self):
        pass

    def check_diagonal(self):
        pass
    
    def display(self, screen):
        screen.blit(self.board, (0,0))
        self.update_board(screen)
             
    def update_board(self, screen):
        for i, line in enumerate(self.state):
            for j, cell in enumerate(line):
                if cell == 1:
                    screen.blit(self.img_x, (j*100, i*100))
                elif cell == 2:
                    screen.blit(self.img_o, (j*100, i*100))


        # Display the state
        if state[0] == 1:
            screen.blit(self.img_x, (0, 0))
        if state[1] == 1:
            screen.blit(self.img_x, (100, 0))
        if state[2] == 1:
            screen.blit(self.img_x, (200, 0))
        if state[3] == 1:
            screen.blit(self.img_x, (0, 100))
        if state[4] == 1:
            screen.blit(self.img_x, (100, 100))
        if state[5] == 1:
            screen.blit(self.img_x, (200, 100))
        if state[6] == 1:
            screen.blit(self.img_x, (0, 200))
        if state[7] == 1:
            screen.blit(self.img_x, (100, 200))
        if state[8] == 1:
            screen.blit(self.img_x, (200, 200))
        if state[0] == 2:
            screen.blit(self.img_o, (0, 0))
        if state[1] == 2:
            screen.blit(self.img_o, (100, 0))
        if state[2] == 2:
            screen.blit(self.img_o, (200, 0))
        if state[3] == 2:
            screen.blit(self.img_o, (0, 100))
        if state[4] == 2:
            screen.blit(self.img_o, (100, 100))
        if state[5] == 2:
            screen.blit(self.img_o, (200, 100))
        if state[6] == 2:
            screen.blit(self.img_o, (0, 200))
        if state[7] == 2:
            screen.blit(self.img_o, (100, 200))
        if state[8] == 2:
            screen.blit(self.img_o, (200, 200))

    def if_o_win(self):
        if self.board[0] == 2 and self.board[3] == 2 and self.board[6] == 2:
            self.o_win = True
        elif self.board[1] == 2 and self.board[4] == 2 and self.board[7] == 2:
            self.o_win = True
        elif self.board[2] == 2 and self.board[5] == 2 and self.board[8] == 2:
            self.o_win = True
        elif self.board[0] == 2 and self.board[1] == 2 and self.board[2] == 2:
            self.o_win = True
        elif self.board[3] == 2 and self.board[4] == 2 and self.board[5] == 2:
            self.o_win = True
        elif self.board[6] == 2 and self.board[7] == 2 and self.board[8] == 2:
            self.o_win = True
        elif self.board[0] == 2 and self.board[4] == 2 and self.board[8] == 2:
            self.o_win = True
        elif self.board[2] == 2 and self.board[4] == 2 and self.board[6] == 2:
            self.o_win = True
        elif self.board[0] == 2 and self.board[2] == 2 and self.board[6] == 2:
            self.o_win = True
        elif self.board[0] == 2 and self.board[2] == 2 and self.board[6] == 2:
            self.o_win = True
        elif self.board[0] == 2 and self.board[2] == 2 and self.board[6] == 2:
            self.o_win = True

    def if_x_win(self):
        if self.board[0] == 1 and self.board[3] == 1 and self.board[6] == 1:
            self.x_win = True
        elif self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1:
            self.x_win = True
        elif self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1:
            self.x_win = True
        elif self.board[0] == 1 and self.board[1] == 1 and self.board[2] == 1:
            self.x_win = True
        elif self.board[3] == 1 and self.board[4] == 1 and self.board[5] == 1:
            self.x_win = True
        elif self.board[6] == 1 and self.board[7] == 1 and self.board[8] == 1:
            self.x_win = True
        elif self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1:
            self.x_win = True
        elif self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1:
            self.x_win = True
        elif self.board[0] == 1 and self.board[2] == 1 and self.board[6] == 1:
            self.x_win = True
        elif self.board[0] == 1 and self.board[2] == 1 and self.board[6] == 1:
            self.x_win = True
        elif self.board[0] == 1 and self.board[2] == 1 and self.board[6] == 1:
            self.x_win = True

