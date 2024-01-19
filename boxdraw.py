
from random import randint

def start(player_1, player_2):

    players = f"{player_1}  {player_2}"
    print('''HERE ARE TWO BOXES:

          __________     __________
         /         /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   BLUE  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/'''
        f"\n {player_1}    {player_2}"
          )

    print(player_1 + ', you have a RED box in front of you.')
    print(player_2 + ', you have a BLUE box in front of you.')
    print("\n")
    print(player_1 + ', you will get to look into your box.')
    print(player_2 + ', close your eyes and don\'t look!!!')
    input('When ' + player_2 + ' has closed their eyes, press Enter...')
    print("\n")

value = 0

def random_box():
    global value
    value = randint(1, 2)

    if value == 1:
        print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|    __________
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   BLUE  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
   carrot! ''')

    elif value == 2:
        print('''
    _________
   |         |
   |         |
   |_________|    __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   BLUE  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  NO carrot! ''')


def player2_decide():

    if value == 1:
        player1_has_carrot = True
    elif value == 2:
        player1_has_carrot = False

    player2_choice = input("to keep press (K), to swap press (S)")

    if (player2_choice.upper() == 'K' and value == 2) or (player2_choice.upper() == 'S' and value == 1):
        print('YOU WON! You got the carrot.')
    elif (player2_choice.upper() == 'K' and value == 1) or (player2_choice.upper() == 'S' and value == 2):
        print('You Lost, Player 1 has the carrot!')
