import pygame


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
        self.turn = 0

    def move(self, pos):
        i, j = pos
        self.state[i][j] = 2 if self.turn == 0 else 1
        self.next_turn()

    def next_turn(self):
        self.turn = (self.turn + 1) % 2

    def check_horizontal(self):
        # Can be refactored
        for i in self.state:
            if all(element == 1 for element in i):
                return 1
            elif all(element == 2 for element in i):
                return 2
        return 0
    
    def check_vertical(self):
        for i in range(len(self.state)):
            col = [row[i] for row in self.state]
            if all(element == col[0] for element in col):
                return col[0]
        return 0
            
    def check_diagonal(self):
        center = self.state[1][1]
        if self.state[0][0] == self.state[2][2] == center or self.state[2][0] == self.state[0][2] == center :
            return center
        return 0

    def check_winner(self):
        if self.check_vertical():
            return self.check_vertical()
        elif self.check_horizontal():
            return self.check_horizontal()
        elif self.check_diagonal():
            return self.check_diagonal()
        
        return 0
    
    def display(self, screen):
        screen.blit(self.board, (0,0))
        self.update_board(screen)
        
        if self.turn == 1:
            screen.blit(self.ind_x, (0, 300))
        elif self.turn == 0:
            screen.blit(self.ind_o, (0, 300))

        winner = self.check_winner()
        if winner == 1:
            screen.blit(self.xwin, (0,0))
        elif winner == 2:
            screen.blit(self.owin, (0,0))
            
    def update_board(self, screen):
        for i, line in enumerate(self.state):
            for j, cell in enumerate(line):
                if cell == 1:
                    screen.blit(self.img_x, (j*100, i*100))
                elif cell == 2:
                    screen.blit(self.img_o, (j*100, i*100))
