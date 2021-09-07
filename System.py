import pygame
img_x = pygame.image.load('x.png')
img_o = pygame.image.load('o.png')
ind_x = pygame.image.load('x_indicator.png')
ind_o = pygame.image.load('o_indicator.png')
xwin = pygame.image.load('Xwin.png')
owin = pygame.image.load('Owin.png')

state = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]

class Game:
    def __init__(self):
        self.board = pygame.image.load('tic_tac_toe.png')
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.o_win = False
        self.x_win = False

    def check_horizontal(self):
        pass
    
    def check_vertical(self):
        pass

    def check_diagonal(self):
        pass
    
    def display(self, screen):
        screen.blit(self.board, (0,0))

        # Display the state
        if state[0] == 1:
            screen.blit(img_x, (0, 0))
        if state[1] == 1:
            screen.blit(img_x, (100, 0))
        if state[2] == 1:
            screen.blit(img_x, (200, 0))
        if state[3] == 1:
            screen.blit(img_x, (0, 100))
        if state[4] == 1:
            screen.blit(img_x, (100, 100))
        if state[5] == 1:
            screen.blit(img_x, (200, 100))
        if state[6] == 1:
            screen.blit(img_x, (0, 200))
        if state[7] == 1:
            screen.blit(img_x, (100, 200))
        if state[8] == 1:
            screen.blit(img_x, (200, 200))
        if state[0] == 2:
            screen.blit(img_o, (0, 0))
        if state[1] == 2:
            screen.blit(img_o, (100, 0))
        if state[2] == 2:
            screen.blit(img_o, (200, 0))
        if state[3] == 2:
            screen.blit(img_o, (0, 100))
        if state[4] == 2:
            screen.blit(img_o, (100, 100))
        if state[5] == 2:
            screen.blit(img_o, (200, 100))
        if state[6] == 2:
            screen.blit(img_o, (0, 200))
        if state[7] == 2:
            screen.blit(img_o, (100, 200))
        if state[8] == 2:
            screen.blit(img_o, (200, 200))

    def if_o_win(self, board):
        if board[0] == 2 and board[3] == 2 and board[6] == 2:
            self.o_win = True
        elif board[1] == 2 and board[4] == 2 and board[7] == 2:
            self.o_win = True
        elif board[2] == 2 and board[5] == 2 and board[8] == 2:
            self.o_win = True
        elif board[0] == 2 and board[1] == 2 and board[2] == 2:
            self.o_win = True
        elif board[3] == 2 and board[4] == 2 and board[5] == 2:
            self.o_win = True
        elif board[6] == 2 and board[7] == 2 and board[8] == 2:
            self.o_win = True
        elif board[0] == 2 and board[4] == 2 and board[8] == 2:
            self.o_win = True
        elif board[2] == 2 and board[4] == 2 and board[6] == 2:
            self.o_win = True
        elif board[0] == 2 and board[2] == 2 and board[6] == 2:
            self.o_win = True
        elif board[0] == 2 and board[2] == 2 and board[6] == 2:
            self.o_win = True
        elif board[0] == 2 and board[2] == 2 and board[6] == 2:
            self.o_win = True

    def if_x_win(self, board):
        if board[0] == 1 and board[3] == 1 and board[6] == 1:
            self.x_win = True
        elif board[1] == 1 and board[4] == 1 and board[7] == 1:
            self.x_win = True
        elif board[2] == 1 and board[5] == 1 and board[8] == 1:
            self.x_win = True
        elif board[0] == 1 and board[1] == 1 and board[2] == 1:
            self.x_win = True
        elif board[3] == 1 and board[4] == 1 and board[5] == 1:
            self.x_win = True
        elif board[6] == 1 and board[7] == 1 and board[8] == 1:
            self.x_win = True
        elif board[0] == 1 and board[4] == 1 and board[8] == 1:
            self.x_win = True
        elif board[2] == 1 and board[4] == 1 and board[6] == 1:
            self.x_win = True
        elif board[0] == 1 and board[2] == 1 and board[6] == 1:
            self.x_win = True
        elif board[0] == 1 and board[2] == 1 and board[6] == 1:
            self.x_win = True
        elif board[0] == 1 and board[2] == 1 and board[6] == 1:
            self.x_win = True

