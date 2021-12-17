import numpy as np
import random as rnd
import time

def length(array):

	return sum(len(i) for i in array)

class Game:


	def __init__(self):
		self.board = np.zeros((3,3))
		self.running = True
		self.turn = True

	def play(self):
		self.zeros = np.where(self.board == 0)
		zeros = self.zeros

		rol = list(zeros[0])
		col = list(zeros[1])

		rnd_r = rnd.choice(rol)
		rnd_c = col[rol.index(rnd_r)]

		if self.turn:
			self.board [rnd_r][rnd_c] = 1
		else:
			self.board [rnd_r][rnd_c] = 2

	def print_tab(self):
		for l in self.board:
			for c in l:
				print(int(c), end='    ')
			for i in range(2):
				print()
		print('-------------')

	def switch_turn(self):

		if self.turn:
			self.turn = False
		else:
			self.turn = True

	def	check_win(self):
		for row in range(3):
			if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
				self.running = False
		for col in range(3):
			if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0 :
				self.running = False


		if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
			self.running = False
		elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
			self.running = False
			

match = Game()

match.play()

while match.running:

	match.play()

	match.print_tab()
	time.sleep(2)
	match.switch_turn()

	match.check_win()
	if not match.running:
		print('we have a winner')
	if not 0 in match.board:
		print('\n tie')
		break