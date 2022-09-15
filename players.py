from checker import Check

# class for choosing who is playing


class Player(Check):
    def __init__(self):
        super().__init__()
        self.player1_symbol = "O"
        self.player2_symbol = "X"
        self.winner = False
        self.draw = False
        self.computer = False

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
                if self.computer:
                    if letter == 'X':
                        print("Computer won!")
                    else:
                        print("You won!")
                else:
                    if letter == "X":
                        print("Player 2 won")
                    else:
                        print("Player 1 won")
                    
            return


        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            self.insert_letter(letter, position)
            return

    def human_player_one(self):
        position = int(input("Enter the position for 'O':  "))
        self.insert_letter(self.player1_symbol, position)
        return

    def human_player_two(self):
        position = int(input("Enter the position for 'X':  "))
        self.insert_letter(self.player2_symbol, position)
        return

    # computer move
    def computer_move(self):
        self.computer = True
        best_score = -100
        best_move = 0
        for key in self.positions.keys():
            if (self.positions[key] == ' '):
                self.positions[key] = self.player2_symbol
                score = self.check_best_move(self.positions, 0, -100, 100, False)
                self.positions[key] = ' '
                if (score > best_score):
                    best_score = score
                    best_move = key

        self.insert_letter(self.player2_symbol, best_move)
        return
