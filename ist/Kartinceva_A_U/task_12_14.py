#Задача 12. Вариант 14.
#Разработайте игру "Крестики-нолики"

#Kartinceva A.U.
#21.04.17

X = "X"
O = "O"
EMPTY = " "
TIE = "ничья"
NUM_SQUARES = 10
def main():
	return 0
def display_instruct():
	print (
	"""
	Добро пожаловать в игру "Крестики-нолики".
	Твой мозг и мой процессор сойдутся в схватке.
	Чтобый сделать ход, введи число(1-9). Числа соответсвую полям доски:
	
	   1 | 2 | 3
	   ---------
	   4 | 5 | 6
	   ---------
	   7 | 8 | 9
	   
	Приготовься к бою. Вот-вот начнется решающее сражение.\n
	"""
	)
	
def ask_yes_no (question):
	response = None
	while response not in ("да","нет"):
		response = input(question).lower()
	return response

	
	

def ask_number (question, low, high):
	response = None
	while response not in range (low, high):
		response = int (input (question))
	return response



	
def pieces():
	go_first = ask_yes_no("Хочешь ходить первым?(да/нет):\n ")
	if go_first == "да":
		print ("\nНу ладно, ходи первым! Ты играешь крестиками, а я ноликами.")
		human = X
		computer = O
	else:
		print ("\nТы уверен? Уже ничего не изменишь! Первым хожу я! Крестики мои.")
		computer = X
		human = O
	return computer, human



	
def new_board():
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board

	
	
	
def display_board(board):
	print ("\n\t" , board[1] , "|" , board[2] , "|", board[3])
	print ("\t" , "---------")
	print ("\t" , board[4] , "|" , board[5] , "|" , board[6])
	print ("\t" , "---------")
	print ("\t" , board[7] , "|" , board[8] , "|" , board[9])
	print ("\t" , "---------")

	

	
def legal_moves(board):
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves



	
def winner(board):
	WAYS_TO_WIN = (( 1 , 2 , 3),
				   ( 4 , 5 , 6),
				   ( 7 , 8 , 9),
				   ( 1 , 4 , 7),
				   ( 2 , 5 , 8),
				   ( 3 , 6 , 9),
				   ( 1 , 5 , 9),
				   ( 3 , 5 , 7))
	for row in WAYS_TO_WIN:
		if board[ row[0] ] == board[ row[1] ] == board[ row[2] ] != EMPTY:
			winner = board[ row[0] ]
			return winner
		if EMPTY not in board:
			return TIE
	return None




	
def human_move(board, human):
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Твой ход. Выбери одно из полей (1-9):", 0 , NUM_SQUARES)
		if move not in legal:
			print("\nЭто поле уже занято. Выбери другое.\n")
	print ("Ладно...")
	return move




	
def computer_move(board, computer, human):
	board = board[:]
	WAYS_TO_WIN = (( 1 , 2 , 3),
				   ( 4 , 5 , 6),
				   ( 7 , 8 , 9),
				   ( 1 , 4 , 7),
				   ( 2 , 5 , 8),
				   ( 3 , 6 , 9),
				   ( 1 , 5 , 9),
				   ( 3 , 5 , 7))
	for row in WAYS_TO_WIN:
		for cell in row:
			if board[cell] == EMPTY:
				board[cell] = computer
				return cell
		



		
def next_turn(turn):
	if turn == X:
		return O
	else:
		return X
	


	
def  congrat_winner(the_winner, computer, human):
	if the_winner != TIE:
		print ("\nКруто! Три ", the_winner, " в ряд!")
	else:
		print("\nНичья")
	if the_winner == computer:
		print ("Победа осталась за мной!")
		print ("Вот и довод в пользу того, что компьютеры превосходят людей во всем")
	elif the_winner == human:
		print ("Этого быть не может! Неужели ты смог переиграть меня, белковый?")
		print ("Клянусь: я, компьютер, не допущу этого еще раз!")
	elif the_winner == TIE:
		print ("Тебе повезло, что ты смог свести игру вничью.")
		print ("Радуйся пока можешь. Завтра ты уже не сможешь этого сделать!")



		
def game():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)
	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)
main()
game()
input("\nНажми Enter, чтобы выйти! Удачи!")