import random
from boxdraw import start, random_box, player2_decide


print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')
input('Press Enter to begin...')

playerN1 = input("Player number 1, Enter your name: ")
playerN2 = input("Player number 2, Enter your name: ")

start(playerN1, playerN2)

print(playerN1.upper() + ' here is the inside of your box:')

random_box()

input(f"Before {playerN2.upper()} open their eyes, Please press Enter...")

print("\n"*80)

print(f"Now {playerN2.upper()}, You have to decide either to keep your BOX or swap the BOX!")

player2_decide()

