class System:
    def __init__(self):
        self.o_win = False
        self.x_win = False

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

