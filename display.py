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

end_message = "Thank you for playing My TicTacToe\n"


class Display:
    def __init__(self):
        self.positions = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "} 
        self.board = ""

    def game_board(self):
        self.board = f"{self.positions[1]}|{self.positions[2]}|{self.positions[3]}\n-+-+-\n{self.positions[4]}|{self.positions[5]}|{self.positions[6]}\n-+-+-\n{self.positions[7]}|{self.positions[8]}|{self.positions[9]}\n"

        return self.board

    def positions_guide(self):
        return f"1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n"
         