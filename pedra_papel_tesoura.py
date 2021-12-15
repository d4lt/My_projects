from math import perm
import random as rnd

computer = ['rock','paper','scissors']

you = input('rock,paper or scissors:')

while you not in computer:
    you = input('rock,paper or scissors:')

comp_choice = rnd.choice(computer)

def game(player, ia):

    if player == ia:
        print('draw!')

    if player == 'rock' and ia == 'scissors':
        print('you win!')

    if player == 'rock' and ia == 'paper':
        print('you lose!')

    if player == 'scissors' and ia == 'paper':
        print('you win!')

    if player == 'scissors' and ia == 'rock':
        print('you lose!')

    if player == 'paper' and ia == 'rock':
        print('you win!')

    if player == 'paper' and ia == 'scissors':
        print('you lose!')


print('your choice: {}'.format(you))
print('computers choice: {}'.format(comp_choice))

game(you, comp_choice)