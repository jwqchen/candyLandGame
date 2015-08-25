import itertools
import random

random.seed(10)
class Dice:
	def __init__(self, num_dice, sides):
		self.num_dice = num_dice
		self.sides = sides
	def roll(self):
		'''roll dice'''
		rand_num = 0
		for i in range(self.num_dice):
			rand_num += random.randint(1, self.sides)
		return rand_num
		
		
class Player:
	id_iter = itertools.count(1)
	def __init__(self):
		self.id = next(self.id_iter)
		self.position = 0
		self.result = None
		# self.history = []

	def roll_dice(self, dice):
		return dice.roll()

	def move(self, rand_num, board):
		print("board.max_position", board.max_position)
		print(self.id, "wants to go to", rand_num + self.position)
		if board.max_position >= (rand_num + self.position):
			self.position += rand_num
			if self.position in board.layout:
				self.position = board.layout[self.position]
		else:
			print("oops, you rolled more than remaining steps")

	def is_finished(self, board):
		if self.position == board.max_position:
			return True
		else:
			return False

class Board:
	def __init__(self, max_position, layout = {1:10, 4:2}):
		self.max_position = max_position
		self.layout = layout

class Game:
	id_iter = itertools.count(1)
	def __init__(self, dice, board, player_num):
		self.id = next(self.id_iter)		
		self.dice = dice
		self.board = board
		self.player_num = player_num
		self.result = []


	#can I fold add-player into play?
	def add_player(self):
		player_list = [Player() for i in range (self.player_num)]
		self.player_list = player_list

	def play(self):
		self.add_player()
		finished_num = 0
		while finished_num < self.player_num:
			for player in self.player_list:
				if player.result == None:
					rand_num = player.roll_dice(self.dice)
					print(player.id, "you rolled", rand_num)
					player.move(rand_num, self.board)
					print(player.id, "you moved to", player.position)

					if player.is_finished(self.board):
						finished_num += 1
						print("player", player.id, "finished at position", finished_num)
						player.result = finished_num
						self.result.append([finished_num, player.id])
				else:
					pass
					#this implementation seems awkward
		print("game over!")
		self.result.sort()
		for i in range(len(self.result)):
			print("Place", i + 1, ": player", self.result[i][1])

class Simulation:
	def __init__(self, dice, board, player_num, round_num):
		self.round_num = round_num
		self.dice = dice
		self.board = board
		self.player_num = player_num
		self.round_num = round_num
		self.result = []

	def add_game(self):
		game_list = [Game(self.dice, self.board, self.player_num) for i in range(self.round_num)]
		self.game_list = game_list

	#every new game instantiates new players, ughhh
	def run(self):
		self.add_game()
		for i in range(self.round_num):
			self.game_list[i].play()
			self.result.append([self.game_list[i].id, self.game_list[i].result[0][1]])
		print(self.result)


def main():
	num_dice = 1
	sides = 6
	d = Dice(num_dice, sides)

	max_position = 50
	b = Board(max_position)

	dice = d
	board = b
	player_num = 2
	g = Game (dice, board, player_num)

	round_num = 5
	s = Simulation(d, b, player_num, round_num)
	s.run()

if __name__ == '__main__':
	main()



# def main():
# 	g = Game()
# 	g.add_board(Board(40, {3:6, 10:20, 38:39}))
# 	d = Dice(20)

# 	for i in range(0,20):
# 		g.add_player(Player(d))
# 	winner = g.run()
# 	print winner
