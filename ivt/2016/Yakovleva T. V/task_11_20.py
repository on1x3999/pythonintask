#Задача 12. Вариант 16.

#12.Разработайте игру "Крестики-нолики".

#Yakovleva T. V.
#04.04.2017

X = "X"
O = "O"
EMPTY = " "
TIE = "НИЧЬЯ"
NUM_SQUARES = 9


def display_instruct():
    """Инструкция."""  
    print(
    """
   \n\t\t\tДобро пожаловать в игру крестики-нолики.
   Чтобы сделать ход, введите позицию от 0 до 8, которая соответствует данному полю:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Удачи и приятной игры. \n
    """
    )


def ask_yes_no(question):
    """Да\Нет."""
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ввод числа"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определение первого хода"""
    go_first = ask_yes_no("Вы хотите оставить за собой первый ход? (да/нет): ")
    if go_first == "да":
        print("\nХорошо. Вы ходите первыми.")
        human = X
        computer = O
    else:
        print("\nХорошо. Первым ходит компьютер.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Новая доска."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображение доски на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Доступные ходы."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определение победителя."""
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
    """Ход игрока."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Выберите поле (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nНедопустимый ход. Попробуйте снова.\n")
    print("Хорошо...")
    return move


def computer_move(board, computer, human):
    """Ход компьютера."""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Компьютер выбирает поле под номером", end=" ")
    
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    
    for move in legal_moves(board):
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
    """Смена хода."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Определение победителя."""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")

    if the_winner == computer:
        print("Компьютер одержал победу. \nПопытайтесь еще раз.")

    elif the_winner == human:
        print("Вы одержали победу! Наши поздравления!")

    elif the_winner == TIE:
        print("Потрясающе!")


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
