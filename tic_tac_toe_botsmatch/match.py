from operator import is_not
import time
import random as rnd


def verify_win():

    for row in range(3):
        if hashtab[row][0] == hashtab[row][1] == hashtab[row][2] != '-':
            return True


    for col in range(3):
        if hashtab[0][col] == hashtab[1][col] == hashtab[2][col] != '-' :
            return True


    if hashtab[0][0] == hashtab[1][1] == hashtab[2][2] != '-':
        return True

    elif hashtab[0][2] == hashtab[1][1] == hashtab[2][0] != '-':
        return True



def bot_play(row, col):
    if hashtab[row][col] ==  '-':
        if bot_turn == 'bot1':
            hashtab[row][col] = 'O'
        elif bot_turn == 'bot2':
            hashtab[row][col] = 'X'
    else:
        return


def print_tab():
    for l in hashtab:
        for c in l:
            print(c, end='    ')
        for i in range(2):
            print()
    print('-------------')
# -------------------------------------#
hashtab = [['-','-','-'],
          ['-','-','-'],
          ['-','-','-']]
#------------------------------------------------------------#
bot_turn = 'bot1'

while True:

    if bot_turn == 'bot1':
        bot_turn = 'bot2'
    elif bot_turn == 'bot2':
        bot_turn = 'bot1'
    print(bot_turn)

    row = rnd.randint(0,2)
    column = rnd.randint(0,2)
    bot_play(row, column)

    time.sleep(2)

    print_tab()


    if verify_win() == True:
        print('we have a winner')
        break

    if not any('-' in  i for i in hashtab):
        print('tie')
        break


