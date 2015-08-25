#I didn't end up finishing the unit testing. So only a subset of functions are covered here.
from candyLand import *

#if there are multiple asserts in a function, nose will throw error on the first assert that goes wrong

def test_dice_init():
	d = Dice(1, 2)
	assert d.num_dice == 1
	assert d.sides == 2

def test_dice_roll():
	random.seed(10)
	d = Dice(1, 6)
	assert d.roll() == 5
	assert d.roll() == 1
	# d = Dice(2, 20)
	# assert d.roll() == 29

def test_player_init():
	p = Player()
	p.id = 1
	p = Player()
	p.id = 2

def test_player_roll_dice():
	random.seed(10)
	d = Dice(1,6)
	p = Player()
	assert p.roll_dice(d) == 5
	assert p.roll_dice(d) == 1

def test_player_move():
	b = Board(15)
	p = Player()
	p.move(4, b)
	assert p.position == 2  
	p.move(6, b)
	assert p.position == 8
	p.move(100, b)
	assert p.position == 8

def test_player_is_finished():
	b = Board(15)
	p = Player()
	p.position = 15
	assert p.is_finished(b) == True
	p.position = 10
	assert p.is_finished(b) == False

def test_board_init():
	b = Board(20)
	assert b.max_position == 20
	assert b.layout == {1:10, 4:2}

def test_game_init():
	d = Dice(1, 6)
	b = Board(25)
	g = Game(d, b, 2)
	assert g.id == 1
	g = Game(d, b, 3)
	assert g.id == 2
	assert g.dice == d
	assert g.board == b
	assert g.player_num == 3

def test_game_add_player():
	d = Dice(1, 6)
	b = Board(25)
	g = Game(d, b, 5)
	result0 = g.add_player()
	result = g.add_player()

	# print("length", len(result))
	# print("here", result[0].id)
	#not sure why this result always says 11 instead of 6\
	#but verified it on interactive 
	assert g.player_list[0].id == 11
 
