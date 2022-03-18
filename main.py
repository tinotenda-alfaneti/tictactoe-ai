from display import Display, art, welcome, end_message
from checker import Check
from players import Player

# creating the class objects
display = Display()
brain = Check()
player = Player()

print(art + "\n" + welcome)
print(display.game_board())

# loop for playing game. The loop stops only when there is no more vacant positions or there is a winner
while not player.winner and not player.draw:

    if not player.winner and not player.draw:
        print("Player 1")
        player.player_1()
        print("\n")
    if not player.winner and not player.draw:
        print("Player 2")
        player.player_2()
        print("\n")


print(end_message)
