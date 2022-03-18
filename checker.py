from display import Display

# class for checking for a winner of draw


class Check(Display):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.winner = False
        self.draw = False

    # function for checking for the winner

    def winner_checker(self):

        # checking player 1 horizontal positions
        if "  ".join(self.positions[0]) == "X  X  X" or "  ".join(self.positions[1]) == "X  X  X" \
                or "  ".join(self.positions[2]) == "X  X  X":
            print("\nPlayer 1 won")
            self.winner = True

        # checking player 2 horizontal positions
        if "  ".join(self.positions[0]) == "O  O  O" or "  ".join(self.positions[1]) == "O  O  O" \
                or "  ".join(self.positions[2]) == "O  O  O":
            print("\nPlayer 2 won")
            self.winner = True

        # checking player 1 horizontal positions
        if (self.positions[0][0] == "X" and self.positions[1][0] == "X" and self.positions[2][0] == "X") \
                or (self.positions[0][1] == "X" and self.positions[1][1] == "X" and self.positions[2][1] == "X") \
                or (self.positions[0][2] == "X" and self.positions[1][2] == "X" and self.positions[2][2] == "X"):
            print("\nPlayer 1 won")
            self.winner = True

        # checking player 2 horizontal positions
        if (self.positions[0][0] == "O" and self.positions[1][0] == "O" and self.positions[2][0] == "O") \
                or (self.positions[0][1] == "O" and self.positions[1][1] == "O" and self.positions[2][1] == "O") \
                or (self.positions[0][2] == "O" and self.positions[1][2] == "O" and self.positions[2][2] == "O"):
            print("\nPlayer 2 won")
            self.winner = True

        # checking player 1 diagonal positions
        if (self.positions[0][0] == "X" and self.positions[1][1] == "X" and self.positions[2][2] == "X") \
                or (self.positions[0][2] == "X" and self.positions[1][1] == "X" and self.positions[2][0] == "X"):
            print("\nPlayer 1 won")
            self.winner = True

        # checking player 2 diagonal positions
        if (self.positions[0][0] == "O" and self.positions[1][1] == "O" and self.positions[2][2] == "O") \
                or (self.positions[0][2] == "O" and self.positions[1][1] == "O" and self.positions[2][0] == "O"):
            print("\nPlayer 2 won")
            self.winner = True

    # checking if all the positions are occupied

    def draw_checker(self):
        if self.count == 9 and not self.winner:
            print("This is a DRAW")
            self.draw = True
