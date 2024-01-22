from random import randint


def start(player_1, player_2):

    print('''HERE ARE TWO BOXES:

          __________     __________
         /         /|   /         /|
        +---------+ |  +---------+ |
        |   RED   | |  |   BLUE  | |
        |   BOX   | /  |   BOX   | /
        +---------+/   +---------+/'''

          f"\n            {player_1.upper()}           {player_2.upper()}"
          )
    print()
    print(player_1.upper() + ', you have a RED box in front of you.')
    print(player_2.upper() + ', you have a BLUE box in front of you.\n')
    print(player_1.upper() + ', you will get to look into your box.')
    print(player_2.upper() + ', close your eyes and don\'t look!!!\n')
    input('When ' + player_2.upper() + ' has closed their eyes, press Enter...')
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
  NO carrot! \n''')


def player2_decide():
    if value == 1:
        player1_has_carrot = True
    elif value == 2:
        player1_has_carrot = False

    player2_choice = input("to keep press (K), to swap press (S)! \n > ")
    print()

    try:
        if (player2_choice.upper() == 'K' and value == 2) or (player2_choice.upper() == 'S' and value == 1):
            print('YOU WON! You got the carrot.')
        elif (player2_choice.upper() == 'K' and value == 1) or (player2_choice.upper() == 'S' and value == 2):
            print('You Lost, Player 1 has the carrot!')
        else:
            print("please enter valid input!")
            player2_decide()
    except:
        print("please enter valid input!")
        player2_decide()
