art = """
888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888 
"""
welcome = "\nWelcome to my TicTacToe Game\n"

end_message = "Thank you for playing My TicTacToe"


class Display:
    def __init__(self):
        self.positions = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]  # Nested list for positions
        self.board = ""

    # function for displaying the positions as a box to mimic the tic tac toe game
    def game_board(self):
        self.board = ("  0  1  2" + "\n" + "0 " + "  ".join(self.positions[0]) + "\n" + "1 " +
                      "  ".join(self.positions[1]) + "\n" + "2 " + "  ".join(self.positions[2]))
        return self.board
