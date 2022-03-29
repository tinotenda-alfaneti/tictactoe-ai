from checker import Check

# class for choosing who is playing


class Player(Check):
    def __init__(self):
        super().__init__()
        self.player_symbol = "O"
        self.computer_symbol = "X"
        self.winner = False
        self.draw = False

    def is_space_free(self, position):
        if self.positions[position] == ' ':
            return True
        else:
            return False

    def insert_letter(self, letter, position):
        if self.is_space_free(position):
            self.positions[position] = letter
            print(self.game_board())

            if self.is_draw():
                print("Draw!")
                self.draw = True

            if self.is_winner(letter):
                self.winner = True
                if letter == 'X':
                    print("Computer won!")
                else:
                    print("You won!")
                    
            return


        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            self.insert_letter(letter, position)
            return

    def human_player_move(self):
        position = int(input("Enter the position for 'O':  "))
        self.insert_letter(self.player_symbol, position)
        return

    def computer_move(self):
        best_score = -100
        best_move = 0
        for key in self.positions.keys():
            if (self.positions[key] == ' '):
                self.positions[key] = self.computer_symbol
                score = self.check_best_move(self.positions, 0, False)
                self.positions[key] = ' '
                if (score > best_score):
                    best_score = score
                    best_move = key

        self.insert_letter(self.computer_symbol, best_move)
        return
