#Задание 12.Вариант 14.
#1-50.	Разработайте	собственную	стратегию	ходов	компьютера	для	игры	"Крестики
#нолики"	(Задача	12).	Перепишите	функцию	computer_move()	в	соответствии	с	этой стратегией.


#Tsukanov K.M.
#13.04.2017
X = "Х"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    print("""
Добро пожаловать игру "Крестики-нолики". Я, компьютер, буду сражаться с тобой!
Чтобы сделать ход, введи число от О до 8. Числа однозначно соответствуют полям доски - так, как показано ниже:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Приготовься!""")

def ask_yes_no(question):
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("Хочешь оставить за собой первый ход?(y/n) ")
    if go_first == "y":
        print("Ладно, ходи первый.")
        human = X
        computer = O
    else: 
        print("Ладно, я буду ходить первым.")
        computer = X
        human = O
    return computer, human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def full(board):
	for i in range(0, 8):
		if board[i] == EMPTY:
			return False
	return True

def winner(board):
	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]]==board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
	if full(board):
		return TIE


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8).", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято!\n")
    print("Хорошо...")
    return move

def computer_move(board, computer, human):
	board = board[:]
	print("Я выберу поле номер", end = " ")
	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
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

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Я победил!")
    elif the_winner == human:
        print("Ты победил!")
    elif the_winner == TIE:
        print("Тебе повезло, но в следующий раз я одержу победу!")

def main():
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
input("\n\nНажмите Enter, чтобы выйти.")