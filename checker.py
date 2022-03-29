from display import Display

# class for checking for a winner of draw


class Check(Display):

    def __init__(self):
        super().__init__()

    # function for checking for the winner

    def is_winner(self, mark):
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


    def is_draw(self):
        for key in self.positions.keys():
            if (self.positions[key] == ' '):
                return False
        return True
        

    # computer move
    def check_best_move(self, board, depth, is_maximizing):
        if (self.is_winner(self.computer_symbol)):
            return 1
        elif (self.is_winner(self.player_symbol)):
            return -1
        elif (self.is_draw()):
            return 0

        if (is_maximizing):
            best_score = -100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.computer_symbol
                    score = self.check_best_move(board, depth + 1, False)
                    board[key] = ' '
                    if (score > best_score):
                        best_score = score
            return best_score

        else:
            best_score = 100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.player_symbol
                    score = self.check_best_move(board, depth + 1, True)
                    board[key] = ' '
                    if (score < best_score):
                        best_score = score
            return best_score
