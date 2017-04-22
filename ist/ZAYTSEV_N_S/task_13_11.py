# Задача 13. Вариант 11.
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-
# нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой
# стратегией.

# Zaytsev N.S. 
# 22.04.2017

print (
"""
\t\tДобро пожаловать в игру "КРЕСТИКИ-НОЛИКИ"!
\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n
\tКто будет ходить первым - определится по жребию (рандомно).
\tЧтобы сделать ход, введи число от 1 до 9. Числа однозначно
\tсоответствуют полям доски - так, как показано ниже:\n
\t\t\t\t  7|8|9
\t\t\t\t---------
\t\t\t\t  4|5|6
\t\t\t\t---------
\t\t\t\t  1|2|3\n
\t\tПриготовься! Вот-вот начнется битва!
"""
)

import random

def drawBoard(board):
	print("\n\t", board[7], "|", board[8], "|", board[9])
	print("\n\t", "---------")
	print("\n\t", board[4], "|", board[5], "|", board[6])
	print("\n\t", "---------")
	print("\n\t", board[1], "|", board[2], "|", board[3], "\n") 

def inputPlayerLetter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Хочешь играть X или O?')
		letter = input().upper()
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	print('Хочешь попробовать снова? (yes или no)')
	return input().lower().startswith('y')
	
def makeMove(board, letter, move):
	board[move] = letter
	
def isWinner(bo, le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or
	(bo[4] == le and bo[5] == le and bo[6] == le) or
	(bo[1] == le and bo[2] == le and bo[3] == le) or
	(bo[7] == le and bo[4] == le and bo[1] == le) or
	(bo[8] == le and bo[5] == le and bo[2] == le) or
	(bo[9] == le and bo[6] == le and bo[3] == le) or
	(bo[7] == le and bo[5] == le and bo[3] == le) or
	(bo[9] == le and bo[5] == le and bo[1] == le))
	
def getBoardCopy(board):
	dupeBoard = []
	for i in board:
		dupeBoard.append(i)
	return dupeBoard
	
def isSpaceFree(board, move):
	return board[move] == ' '

def getPlayerMove(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('Какой твой следующий ход? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
		
def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move
	if isSpaceFree(board, 5):
		return 5
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])
	
def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True
	
while True:
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('Первым ходит: ' + turn)
	gameIsPlaying = True
	
	while gameIsPlaying:
		if turn == 'player':
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)
			
			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Ты выиграл!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Ничья!')
					break
				else:
					turn = 'computer'
		else:
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)
			
			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('Увы! Компьютер победил!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Ничья!')
					break
				else:
					turn = 'player'
	if not playAgain():
		break
input('\nPress enter to exit from this program...')