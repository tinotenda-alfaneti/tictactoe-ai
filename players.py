from checker import Check

# class for choosing who is playing


class Player(Check):
    def __init__(self):
        super().__init__()
        self.player = ""

    # player 1

    def player_1(self):
        self.player = input("What is your position? (RowColumn): ")
        # try statement to catch the error of invalid position entered i.e word or numbers out of the list range
        try:
            # if statement for checking if the position is not taken and replacing the position when
            # it has not been played
            if self.positions[int(self.player[0])][int(self.player[1])] == "X" \
                    or self.positions[int(self.player[0])][int(self.player[1])] == "O":
                print("Position already chosen\nPlay again")
                self.player_1()
            else:
                self.positions[int(self.player[0])][int(self.player[1])] = "X"
                print(self.game_board())
                self.count += 1
            self.winner_checker()
            self.draw_checker()
        except:
            print("Position entered invalid.\nYou just lost your turn to play\n")

    # player 2

    def player_2(self):
        self.player = input("What is your position? (RowColumn): ")
        # try statement to catch the error of invalid position entered i.e word or numbers out of the list range
        try:
            # if statement for checking if the position is not taken and replacing the position when
            # it has not been played
            if self.positions[int(self.player[0])][int(self.player[1])] == "X" \
                    or self.positions[int(self.player[0])][int(self.player[1])] == "O":
                print("Position already chosen\nPlay again")
                self.player_2()
            else:
                self.positions[int(self.player[0])][int(self.player[1])] = "O"
                print(self.game_board())
                self.count += 1
            self.winner_checker()
            self.draw_checker()
        except:
            print("Position entered invalid.\nYou just lost your turn to play\n")
