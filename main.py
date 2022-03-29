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
    

while not player.winner and not player.draw:
    
    player.human_player_move()

    if not player.winner and not player.draw:
        player.computer_move()

print(end_message)
