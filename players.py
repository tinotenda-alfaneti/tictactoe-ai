from checker import Check

# class for choosing who is playing


class Player(Check):
    def __init__(self):
        super().__init__()
        self.player = "O"
        self.bot = "X"

    def spaceIsFree(self, position):
        if self.positions[position] == ' ':
            return True
        else:
            return False

    def insertLetter(self, letter, position):
        if self.spaceIsFree(position):
            self.positions[position] = letter
            print(self.game_board())

            if (self.draw_checker()):
                print("Draw!")

            self.winner_checker()
            if self.winner:
                if letter == 'X':
                    print("Bot wins!")
                else:
                    print("Player wins!")
                    
            return


        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            self.insertLetter(letter, position)
            return

    # player 1

    def playerMove(self):
        position = int(input("Enter the position for 'O':  "))
        self.insertLetter(self.player, position)
        return
    
    # computer play

    def compMove(self):
        bestScore = -100
        bestMove = 0
        for key in self.positions.keys():
            if (self.positions[key] == ' '):
                self.positions[key] = self.bot
                score = self.minimax(self.positions, 0, False)
                self.positions[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        self.insertLetter(self.bot, bestMove)
        return
