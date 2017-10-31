#Aayush Gupta 2017002
#Date :- 26/9/17
#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 0 to 8

"""
Tick-Tac-Toe game state is defined as follows: 

tile0 |  tile1  | tile2
______|_________|______
tile3 |  tile4  | tile5
______|_________|______
tile6 |  tile7  | tile8
______|_________|______

A playerer can belong to one of the following two categories:
1. Naive: Playerer checks a tile randomly.
2. Intelligent: Playerer follows some strategy to win a game. You shall define a strategy that an intelligent playerer can take.

We will estimate probability of winning for a playerer for different scenarios.
 
Game1: A number of games are playered between two naive playerers. Estimate probability of winning for playerer1. Assume playerer1 starts the game.

Game2: A number of games are playered between a naive and intelligent playerer. Estimate probability of winning for playerer1. Assume playerer1 is naive and starts the game.

Game3: A number of games are playered between two intelligent playerers. Estimate probability of winning for playerer1. Assume playerer1 starts the game.  
"""

import random 
# There are 2 playerers: playerer1 and playerer2
#playerer1=1
#playerer2=2


# There are 9 tiles numbered tile0 to tile8
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by playerer-1
# 2 value indicates that the tile is ticked by playerer-2
#tile=[0 for i in range(9)]
tile0= 0    
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0

# turn variable defines whose turn is now
#turn = Playerer1

def validmove(move):
	""" Checks whether a move playered by a playerer is valid or invalid.
		Return True if move is valid. 
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	x='tile'+str(move)
	if globals()[x]==0:
		return True
	else:
		return False

def win():
	""" Returns True if the board state specifies a winning state for some playerer.
		A playerer wins if ticks made by the playerer are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	if ((tile0 == 1 and tile1 == 1 and tile2 == 1) or # across the top
		(tile3 == 1 and tile4 == 1 and tile5 == 1) or # across the middle
		(tile6 == 1 and tile7 == 1 and tile8 == 1) or # across the bottom
		(tile0 == 1 and tile3 == 1 and tile6 == 1) or # down the left side
		(tile1 == 1 and tile4 == 1 and tile7 == 1) or # down the middle
		(tile2 == 1 and tile5 == 1 and tile8 == 1) or # down the right side
		(tile2 == 1 and tile4 == 1 and tile6 == 1) or # diagonal
		(tile0 == 1 and tile4 == 1 and tile8 == 1)):# diagonal
		return 1
	elif ((tile0 == 2 and tile1 == 2 and tile2 == 2) or # across the top
		(tile3 == 2 and tile4 == 2 and tile5 == 2) or # across the middle
		(tile6 == 2 and tile7 == 2 and tile8 == 2) or # across the bottom
		(tile0 == 2 and tile3 == 2 and tile6 == 2) or # down the left side
		(tile1 == 2 and tile4 == 2 and tile7 == 2) or # down the middle
		(tile2 == 2 and tile5 == 2 and tile8 == 2) or # down the right side
		(tile2 == 2 and tile4 == 2 and tile6 == 2) or # diagonal
		(tile0 == 2 and tile4 == 2 and tile8 == 2)):# diagonal
		return 2	
	else:
		return 0
	
def takeNaiveMove(player):
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.""" 
	for i in range(100000):
		num=random.randint(0,8)
		if validmove(num)==True:
			x='tile'+str(num)
			globals()[x]=int(player)
			break

def takeStrategicMove(player):
	""" Returns a tile number from the set of unchecked tiles using some rules."""
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile0
	if tile4==0:
		tile4=int(player)
	else:
		if tile8==0:
			tile8=int(player)
		elif tile6==0:
			tile6=int(player)
		elif tile2==0:
			tile2=(player)
		elif tile0==0:
			tile0=int(player)
		else:
			if tile7==0:
				tile7=(player)
			elif tile5==0:
				tile5=int(player)
			elif tile3==0:
				tile3=int(player)
			elif tile1==0:
				tile1=int(player)

	
def validBoard(x):
	""" Return True if board state is valid.
		A board state is valid if number of ticks by playerer1 is always either equal to or one more than the ticks by playerer2.
	"""
	if win()==0:
		if x==1:
			for i in range(9):
				j='tile'+str(i)
				if globals()[j]==0:
					return True
				else:
					return False
		if x==2:
			global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile0	
			if tile0==0:
				return True
			elif tile1==0:
				return True
			elif tile2==0:
				return True
			elif tile3==0:
				return True
			elif tile4==0:	
				return True
			elif tile5==0:
				return True
			elif tile6==0:	
				return True
			elif tile7==0:
				return True
			elif tile8==0:	
				return True
			else:
				return False
	else:
		return False

def game(gametype=1):
	""" Returns 1 if playerer1 wins and 2 if playerer2 wins
		and 0 if it is a draw.
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	if gametype==1:
		while validBoard(1)==True:
			takeNaiveMove(1)
			takeNaiveMove(2)
		return win()
	elif gametype==2:
		while validBoard(2)==True:
			takeNaiveMove(1)
			takeStrategicMove(2)
		return win()
	elif gametype==3:
		while validBoard(2)==True:
			takeStrategicMove(1)
			takeStrategicMove(2)
		return win()

def game1(n=1000):
	""" Returns the winning probability for playerer1. 
		n games are playered between two naive playerers. Estimate probability of winning for playerer1. Assume playerer1 starts the game.
	"""
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		if game(1)==1:
			count1+=1
		elif game(1)==2:
			count2+=1
		elif game(1)==0:
			count3+=1
	return (count1/n)#,(count2/n),(count3/n)

	

def game2(n=10000):
	"""Returns the winning probability for playerer1.
		n games are playered between a naive and intelligent playerer. Estimate probability of winning for playerer1. Assume playerer1 is naive and starts the game.
	"""
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		if game(2)==1:
			count1+=1
		elif game(2)==2:
			count2+=1
		elif game(2)==0:
			count3+=1
	return (count1/n)#,(count2/n),(count3/n)

def game3(n=10000):
	"""Returns the winning probability for playerer1. 
		n games are playered between two intelligent playerers. Estimate probability of winning for playerer1. Assume playerer1 starts the game.
	"""
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		if game(3)==1:
			count1+=1
		elif game(3)==2:
			count2+=1
		elif game(3)==0:
			count3+=1
	return (count1/n)#,(count2/n),(count3/n)
#print(game1())