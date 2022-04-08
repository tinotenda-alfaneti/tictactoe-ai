from display import Display, art, welcome, end_message
from checker import Check
from players import Player

# instances of the class
display = Display()
brain = Check()
player = Player()

# Display on screen
print(art + "\n" + welcome)
print("You are playing first then computer follows")
print(display.positions_guide())

# Playing game
def play_game():
    game_mode = int(input("Two players or One player? (1/2): "))


    while not player.winner and not player.draw:
        
        player.human_player_one()
        if game_mode == 1:
            if not player.winner and not player.draw:
                player.computer_move()
        else:
            if not player.winner and not player.draw:
                player.human_player_two()


while True:
    play_game()
    choice = input("Do you want to play again (Yes/NO): ").lower()
    if choice == "yes":
        play_game()
    else:
        break
    
print(end_message)
