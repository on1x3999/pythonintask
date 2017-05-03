# Задача 12. Вариант 3.
# Разработайте игру "Крестики-нолики".
# Deryushkina A.B.
# 16.04.2017

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 10
 
def table():
    print(
    """
	Приветствую тебя, мой друг. Сегодня ты поймешь, кто же умнее... человек или компьютер (конечно-же я)!
	Приглашаю тебя поиграть со мной в игру "Крестики-нолики".
	Чтобы сделать ход, введи число от 1 до 9. Числа соотвествуют полям доски - так, как показано ниже:
 
                       1 | 2 | 3
                       ---------
                       4 | 5 | 6
                       ---------
                       7 | 8 | 9
 
   """
    )
 
 
def yes_or_no(question):
    #Задаёт вопрос с ответом 'Да' или 'Нет'.
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
    return response
 
 
def ask_number(question, low, high):
    #Просит ввести число из диапазона
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
 
 
def pieces():
    #Определяет принадлежность перового хода.
    go_first = yes_or_no("Хочешь оставить за собой первый ход? (да, нет): ")
    if go_first == "да":
        print("\nПоехали, ты играешь крестиками.")
        human = X
        computer = O
    else:
        print("\nНачну-ка я, пожалуй, схожу крестиком")
        computer = X
        human = O
    return computer, human
 
 
def new_board():
    #Создаёт новую игровую доску
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
 
 
def display_board(board):
   #Отображает игровую доску на экране
    print("\n\t", board[1], "|", board[2], "|", board[3])
    print("\t", "----------")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t", "----------")
    print("\t", board[7], "|", board[8], "|", board[9])
 
 
def step(board):
    #Создаёт список доступных ходов
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
 
 
def winner(board):
    #Определяет победителя в игре
    WAYS_TO_WIN = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (3, 6, 9),
                   (1, 5, 9),
                   (3, 5, 7))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
 
 
def human_move(board, human):
    #Получает ход человека
    legal = step(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (1 - 9):", 1, NUM_SQUARES)
        if move not in legal:
            print("\nАу! Это поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move
 
 
def computer_move(board, computer, human):
    #Ход компьютера
    board = board[:]
    BEST_MOVES = (5, 1, 3, 7, 9, 2, 4, 6, 8)
 
    print("Я выберу поле номер", end = " ")
    for move in step(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
 
    for moves in step(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
 
    for move in BEST_MOVES:
        if move in step(board):
            print(move)
            return move
 
 
def next_turn(turn):
    #Переход кода
    if turn == X:
        return O
    else:
        return X
 
 
def congrat_winner(the_winner, computer, human):
    #Поздравляет победителя игры
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Я так и знал, что у тебя ничего не получится\n" \
              "Компьютеры круче людей!")
    elif the_winner == human:
        print("О нет, я не мог этого допустить, наверное это случайность..\n")
    elif the_winner == TIE:
        print("Тебе несказанно повезло: ты сумел игру вничью. \n" \
              "Это редкость, думаю, в следующий раз тебе уже не выиграть")
 
 
def main():
    table()
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
input("Нажмите Enter, чтобы выйти.")