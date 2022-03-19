from display import Display

# class for checking for a winner of draw


class Check(Display):

    def __init__(self):
        super().__init__()
        self.winner = False
        self.draw = False

    # function for checking for the winner

    def winner_checker(self):

        if (self.positions[1] == self.positions[2] and self.positions[1] == self.positions[3] and self.positions[1] != ' '):
            self.winner = True
        elif (self.positions[4] == self.positions[5] and self.positions[4] == self.positions[6] and self.positions[4] != ' '):
            self.winner = True
        elif (self.positions[7] == self.positions[8] and self.positions[7] == self.positions[9] and self.positions[7] != ' '):
            self.winner = True
        elif (self.positions[1] == self.positions[4] and self.positions[1] == self.positions[7] and self.positions[1] != ' '):
            self.winner = True
        elif (self.positions[2] == self.positions[5] and self.positions[2] == self.positions[8] and self.positions[2] != ' '):
            self.winner = True
        elif (self.positions[3] == self.positions[6] and self.positions[3] == self.positions[9] and self.positions[3] != ' '):
            self.winner = True
        elif (self.positions[1] == self.positions[5] and self.positions[1] == self.positions[9] and self.positions[1] != ' '):
            self.winner = True
        elif (self.positions[7] == self.positions[5] and self.positions[7] == self.positions[3] and self.positions[7] != ' '):
            self.winner = True
        else:
            self.winner = False
    

    def checkWhichMarkWon(self, mark):
        if self.positions[1] == self.positions[2] and self.positions[1] == self.positions[3] and self.positions[1] == mark:
            return True
        elif (self.positions[4] == self.positions[5] and self.positions[4] == self.positions[6] and self.positions[4] == mark):
            return True
        elif (self.positions[7] == self.positions[8] and self.positions[7] == self.positions[9] and self.positions[7] == mark):
            return True
        elif (self.positions[1] == self.positions[4] and self.positions[1] == self.positions[7] and self.positions[1] == mark):
            return True
        elif (self.positions[2] == self.positions[5] and self.positions[2] == self.positions[8] and self.positions[2] == mark):
            return True
        elif (self.positions[3] == self.positions[6] and self.positions[3] == self.positions[9] and self.positions[3] == mark):
            return True
        elif (self.positions[1] == self.positions[5] and self.positions[1] == self.positions[9] and self.positions[1] == mark):
            return True
        elif (self.positions[7] == self.positions[5] and self.positions[7] == self.positions[3] and self.positions[7] == mark):
            return True
        else:
            return False


    def draw_checker(self):
        for key in self.positions.keys():
            if (self.positions[key] == ' '):
                return False
        return True
        

    def minimax(self, board, depth, isMaximizing):
        if (self.checkWhichMarkWon(self.bot)):
            return 1
        elif (self.checkWhichMarkWon(self.player)):
            return -1
        elif (self.draw_checker()):
            return 0

        if (isMaximizing):
            bestScore = -100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.bot
                    score = self.minimax(board, depth + 1, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.player
                    score = self.minimax(board, depth + 1, True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore
