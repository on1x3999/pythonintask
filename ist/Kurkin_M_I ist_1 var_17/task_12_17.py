#Задача 12. Вариант 17.
#Напишите	программу,	которая	будет	сообщать	род	деятельности	и	псевдоним	под которым	скрывается	Алексей	Максимович	Пешков.	
#После	вывода	информации программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для	выхода.

#Kurkin M. I.
#20.04.2017
X='X'

O='O'

EMPTY=" "

TIE="Ничья"

NUM_SQUARES = 9

from os import system,name

def cls(): system('cls' if name == 'nt' else 'clear')

def display_instruction():

	print(

		"""

		Добро пожаловать. ИИvs.Человек

		Чтоб сделть ход введите соответсвующую цифру:

		0 | 1 | 2

		---------

		3 | 4 | 5

		---------

		6 | 7 | 8

		Начнём \n""")

def ask_yes_no(question):

	response = None

	while response not in ("y", "n"):

		response=input(question).lower()

	return response

def ask_number(question, low, high):

	response = None

	while  response not in range(low, high):

		response=(input(question))

		if response in ("0", "1", "2", "3", "4", '5','6','7','8'):

			response=int(response)

	return response

def pieces():

	go_first = ask_yes_no("Хочешь оставить за собой первый ход(y/n): ")

	if go_first == "y":

		print("Вы первый")

		human = X

		computer = O

	else:

		print("Ок, я первый")

		computer = X

		human = O

	return computer, human

def new_board():

	board = []

	for square in range(NUM_SQUARES):

		board.append(EMPTY)

	return board

def display_board(board):

	print("\n\t",board[0],"|",board[1],"|",board[2],)

	print("\t","---------")

	print("\n\t",board[3],"|",board[4],"|",board[5],)

	print("\t","---------")

	print("\n\t",board[6],"|",board[7],"|",board[8],'\n')

def legal_moves(board):

	moves=[]

	for square in range(NUM_SQUARES):

		if board[square] == EMPTY:

			moves.append(square)

	return moves

def winner(board):

	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

	for row in WAYS_TO_WIN:

		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:

			winner= board[row[0]]

			return winner

		if EMPTY not in board:

			return TIE

	return None

def human_move(board,human):

	legal = legal_moves(board)

	move = None

	while move not in legal:

		move = ask_number("Твой Выбор. Выбери 0-8: ", 0, NUM_SQUARES)

		if move not in legal:

			print("Ошибка: поле занято")

	print("Принято")

	return move

def compuer_move(board,computer,human):

	board = board[:]

	BEST_MOVES = (4,0,2,6,8,1,3,5,7)

	print("Я выберу поле номер",end=" ")

	for move in legal_moves(board):

		board[move] = computer

		if winner(board) == computer:

			print(move)

			return(move)

		board[move]=EMPTY

	for move in legal_moves(board):

		board[move]=human

		if winner(board)==human:

			print(move)

			return move

		board[move]=EMPTY

	for move in BEST_MOVES:

		if move in BEST_MOVES:

			if move in legal_moves(board):

				print(move)

				return move

def next_turn(turn):

	if turn == X:

		return O

	else:

		return X

def congrat_winner(the_winner,computer, human):

	if the_winner != TIE:

		print("ТРИ",the_winner,"в ряд!\n")

	else:

		print ("Ничья")

	if the_winner == computer:

		print("Я win")

	elif the_winner == human:

		print("Твоя взяла")

	elif the_winner==TIE:

		print("Ничья")

def main():

	display_instruction()

	computer,human = pieces()

	cls()

	turn =X

	board = new_board()

	display_board(board)

	while not winner(board):

		if turn == human:

			move =human_move(board,human)

			cls()

			board[move]=human

		else:

			move =  compuer_move(board, computer, human)

			board[move]=computer





		display_board(board)

		turn = next_turn(turn)

	the_winner=winner(board)

	congrat_winner(the_winner,computer,human)







main()

input("Нажмите ввод")