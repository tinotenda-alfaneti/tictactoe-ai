from display import Display, art, welcome, end_message
from checker import Check
from players import Player

# creating the class instances
display = Display()
brain = Check()
player = Player()

print(art + "\n" + welcome)
print("You are playing first then computer follows")
print(display.game_board())

while not player.winner and not player.draw:

    player.playerMove()
    player.compMove()

print(end_message)
