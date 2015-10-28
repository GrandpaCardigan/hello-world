#reversi

import random 
import sys

def drawBoard(board):

	HLINE = '  +---+---+---+---+---+---+---+---+'
	VLINE = '  |   |   |   |   |   |   |   |   |'

	print('    1   2   3   4   5   6   7   8')
	print(HLINE)
	for y in range(8):
		print(VLINE)
		print(y+1, end=' ')
		for x in range(8):
			print('| %s' % (board[x][y]), end=' ')
		print('|')
		print(VLINE)
		print(HLINE)

def resetBoard(board):

	for x in range(8):
		for y in range(8):
			board[x][y] = ' '


	#Starting Pieces:
	board[3][3] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'
	board[4][4] = 'X'

def getNewBoard():

	board = []
	for i in range(8):
		board.append([' '] * 8)

	return board

def isValidMode(board, tile, xstart, ystart):

	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False

	board[xstart][ystart] = tile 

	if tile == 'X': 
		otherTile = 'O'
	else: 
		otherTile = 'X'

	tilesToFlip = []
	for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x, y = xstart, ystart
		x += xdirection 
		y += ydirection
		if isOnBoard(x, y) and board[x][y] == otherTile:

			x += xdirection
			y += ydirection
			if not isOnBoard(x, y):
				continue
			while board[x][y] == otherTile:
				x += xdirection
				y += ydirection
			if not isOnBoard(x, y): 
				break
			if not isOnBoard(x, y):
				continue
			if board[x][y] == tile:
				# There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
				while True: 
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x, y])

	board[xstart][ystart] = ' '
	if len(tilesToFlip) == 0:
		return False
	return tilesToFlip

def isOnBoard(x, y):

	return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
	# Returns a new board with . marking the valid moves the given player can make.
	dupeBoard = getBoardCopy(board)

	for x, y in getValidMoves(dupeBoard, tile):
		dupeBoard[x][y] = '.'
	return dupeBoard

def getValidMoves(board, tile):

	validMoves = []

	for x in range(8):
		for y in range(8):
			if isValidMode(board, tile, x, y) != False:
				validMoves.append([x, y])
	return validMoves

def GetScoreOfBoard(board):

	xscore = 0
	oscore = 0
	for x in range(8):
		for y in range(8):
			if board[x][y] == 'X':
				xscore += 1 
			if board[x][y] == 'O':
				oscore += 1
	return {'X':xscore, 'O':oscore}

def enterPlayerTile():


	tile = ''
	while not (tile == 'X' or tile == 'O'):
		print('Do you want to be X or O?')
		tile = input().upper()



	if tile == 'X':
		return ['X', 'O']
	else: 
		return ['O', 'X']


def whoGoesFirst():
	if random.randint(0, 1) == 0
		return 'Computer'
	else: 
		return 'Player'


def playAgain():
	print('Do you want to play again? (yes) or (no)')
	return input().lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
	tilesToFlip = isValidMode(board, tile, xstart, ystart)

	if tilesToFlip == False:
		return False 

	board[xstart][ystart] = tile
	for x, y in tilesToFlip: 
		board[x][y] = tile
	return True

def getBoardCopy(board):
	dupeBoard = getNewBoard()

	for x in range(8):
		for y in range(8):
			dupeBoard[x][y] = board[x][y]

	return dupeBoard

def isOnCorner(x, y):
	
	return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):

	DIGITS1TO8 = '1, 2, 3, 4, 5, 6, 7, 8'.split()
	while True:
		print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
		move = input().lower()
		if move == 'quit':
			return 'quit'
		if move == 'hints':
			return 'hints'

		if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
			x = int(move[0]) - 1
			y = int(move[1]) - 1
			if isValidMode(board, playerTile, x, y) == False:
				continue
			else:
				break
			else:
				print('That is not a valid move. Type the x digit (1-8), and then the y digit (1-8)')
				print('For example, 81 will be the top right corner.')

	return [x, y]

def getComputerMove(board, ComputerTile):
	possibleMoves = getValidMoves(board, computerTile)
	random.shuffle(possibleMoves)
	for x in y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]
	bestscore = -1 
	for x in y in possibleMoves:
		dupeBoard = getBoardCopy(board)
		makeMove(dupeBoard, computerTile, x, y)
		score = GetScoreOfBoard(dupeBoard)[ComputerTile]
		if score > bestscore:
			bestMove = [x, y]
			bestScore = score
	return bestMove

def showPoints(playerTile,ComputerTile):
	scores = GetScoreOfBoard(mainBoard)
	print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))

print('Welcome to Reversi!')

while True: 
	mainboard = getNewBoard()
	resetBoard(mainboard)
	playerTile, ComputerTile = enterPlayerTile()
	showHints = False
	turn = whoGoesFirst()
	print ('The ' + turn + ' Will go first.')

	while True: 
		if turn == 'Player'
			if showHints:
				validMovesBoard = getBoardWithValidMoves(mainboard, playerTile)
				drawBoard(validMovesBoard)
			else: 
				drawBoard(mainBoard)
			showPoints(playerTile, ComputerTile)
			move = getPlayerMove(mainBoard, playerTile)
			if move == 'quit':
				print('Thanks for playing!')
				sys.exit()
			elif move == 'hints':
				showHints = not showHints
				continue
			else:
				makeMove(mainBoard, playerTile, move[0], move[1])

			if getValidMoves(mainBoard, ComputerTile) == []:
				break
			else: 
				turn = 'computer'
		else:
			drawBoard(mainBoard)
			showPoints(playerTile, ComputerTile)
			input('Press enter to see the comptuer\'s move.')
			x, y = getComputerMove(mainBoard, ComputerTile)
			makeMove(mainBoard, ComputerTile, x, y)

			if getValidMoves(mainBoard, playerTile) == []:
				break
			else: 
				turn == 'player'

	drawBoard(mainBoard)
	scores = GetScoreOfBoard(mainBoard)
	print('X scored %s points. O scored %s points' % (scores['X'], scores['O']))
	if scores[playerTile] > scores[ComputerTile]:
		print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
	elif scores[playerTile] < scores[ComputerTile]: 
		print('You lost. The Computer beat you by %s points.' % (scores[ComputerTile] - scores[playerTile]))
	else: 
		print('The game was a tie!')

	if not playAgain():
		break



