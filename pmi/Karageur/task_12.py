#Задача №13..

#1-50.	Разработайте	собственную	стратегию	ходов	компьютера	для	игры	"Крестики
#нолики"	(Задача	12).	Перепишите	функцию	computer_move()	в	соответствии	с	этой стратегией.

#Довбыш Д.В.

X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instr():
	print("Инструкция")

def ask_yes_no(question):
	respone = None
	while respone not in ("y","n"):
		respone = input(question).lower()
	return respone

def ask_number(question, low, high):
	respone = None
	while respone not in range(low, high):
		respone = int(input(question))
	return respone

def pieces():
	go_first = ask_yes_no("Ты хочешь, чтобы я дал тебе фору? (y/n): ")
	if go_first == "y":
		print("Любишь хитрить? Хорошо, первый ход за тобой, но я все равно одержу победу. Играй крестиками.")
		human = X
		computer = O
	else:
		print("А ты смелый... Я начну, и победа останется за мной.")
		human = O
		computer = X
	return computer,human

def new_board():
	board=[]
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

def display_board(board):
	print("\n\t",board[0],"|",board[1],"|", board[2])
	print("\t","----------")
	print("\n\t",board[3],"|",board[4],"|", board[5])
	print("\t","----------")
	print("\n\t",board[6],"|",board[7],"|", board[8], "\n")

def legal_moves(board):
	moves=[]
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves

def winner(board):
	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]]==board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
	if board_full(board):
		return TIE

def board_full(board):
	for i in range(0, 8):
		if board[i] == EMPTY:
			return False
	return True


def human_move(board,human):
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Твой ход. Выбери поля (1-9): ", 1, NUM_SQUARES + 1)
		move -= 1
		if move not in legal:
			print("Ха-ха! Я умнее, чем ты думаешь! Это поле уже занято!")
		return move

def computer_move(board, computer, human):
	board = board[:]
	print("Хмм, я выберу поле под номером", end = " ")
	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for row in WAYS_TO_WIN:
		for cell in row:
			if board[cell] == EMPTY:
				board[cell] = computer
				return cell


def next_turn(turn):
	if turn==X:
		return O
	else:
		return X

def congrat_winner(the_winner, computer, human):
	if the_winner != TIE:
		print("Три", the_winner, "в ряд")

	if the_winner == computer:
		print("Я же говорил, что победа останется за мной!")
	elif the_winner == human:
		print("КАК?! Неужели ты перехитрил меня?!")
	elif the_winner == TIE:
		print("Ох, на этот раз, что-то пошло не по плану... Ничья")

def main():
	display_instr()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	while not winner(board):
		if turn == human:
			move = human_move(board,human)
			board[move]=human
		else:
			move = computer_move(board,computer,human)
			board[move] = computer
		display_board(board)
		turn=next_turn(turn)
	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)

main()
input("Нажмите Enter, чтобы выйти.")