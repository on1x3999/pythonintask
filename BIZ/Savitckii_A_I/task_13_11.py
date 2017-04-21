#Задача 13
# Разработайте собственную стратегию ходов компьютера для игры "Крестики- нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой стратегией.
#Savitckii A I
#14.04.2017
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
 
def display_instruct():
    print(
    """
   Добро пожаловать на поле боя интеллектиуальных сражений.
   Твой мозг и моя игра сойдутся в схватке в игре "Крестики-нолики".
   Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
   доски - так, как показано ниже:
 
                       0 | 1 | 2
                       ---------
                       3 | 4 | 5
                       ---------
                       6 | 7 | 8
 
   Приготовься  к бою,смелый игрок. Схватка начинается прямо сейчас .\n
   """
    )
 
 
def ask_yes_no(question):
    #Задаёт вопрос с ответом 'Да' или 'Нет'.
    response = None
    while response not in ("д", "н"):
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
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (д, н): ")
    if go_first == "д":
        print("\nХорошо,ты играешь крестиками .")
        human = X
        computer = O
    else:
        print("\nНе я этого захтел. Вот и пришел твой конец. Мой ход будет первым.")
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
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])
 
 
def legal_moves(board):
    #Создаёт список доступных ходов
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
 
 
def winner(board):
    #Определяет победителя в игре
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
 
 
def human_move(board, human):
    #Получает ход человека
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nДа ты не смелый,а глупый! Это поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move
 
 
def computer_move(board, computer, human):
    #Ход компьютера
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
 
    print("Я выберу поле номер", end = " ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
 
    for moves in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
 
    for move in BEST_MOVES:
        if move in legal_moves(board):
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
        print("Кто бы сомневался? Победа в очередной раз досталась мне\n" \
              "В следдующий раз когда захочешь со мной сразиться,не забывай ,что я у тебя уже выигрывал!")
    elif the_winner == human:
        print("Как это получилось! Да ты явно жульничал \n" \
              "Я тебе обещаю,этого больше не повторится!")
    elif the_winner == TIE:
        print("Тебе н повезло, приятель: ты сумел сыграть вничью. \n" \
              "Может повторим? Потому что обычно я довольствуюсь победой!")
 
 
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
input("Нажмите Enter, чтобы выйти.")