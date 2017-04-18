# Задача 13(12). Вариант 16.
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-нолики" (Задача 12).
# Перепишите функцию computer_move() в соответствии с этой стратегией.

# Смирнов Н.Н.
# 20.03.2017


X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instr():
    print("""
    Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён.
    Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
    Чтобы сделать ход. введи число от 1 до 9. 
    Числа однозначно соответствуют полям доски - так, как показано ниже:
     0 | 1 | 2
     ---------
     3 | 4 | 5
     ---------
     6 | 7 | 8
    Приготовься к бою, жалкий белковый человечишка. 
    Вот-вот начнется решающее сражение. \n
    """)


def ask_yes_no(question):
    respone = None
    while respone not in ("y", "n"):
        respone = input(question).lower()
    return respone


def ask_number(question, low, high):
    respone = None
    while respone not in range(low, high):
        respone = int(input(question))
    return respone


def pieces():
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y/n): \n")
    if go_first == "y":
        print("Ну что ж, даю тебе фору, играй крестиками.")
        human = X
        computer = O
    else:
        print("Твоя удаль тебя погубит... Буду начинать я.")
        human = O
        computer = X
    return computer, human


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if board_full(board):
        return TIE


def board_full(board):
    for i in range(0, 8):
        if board[i] == EMPTY:
            return False
    return True


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери поле (0-8): \n", 0, NUM_SQUARES)
        if move not in legal:
            print("Смешной человек! Это поле уже занято. ")
    print("Ок.")
    return move


# перепишем функцию computer_move.
# реализованная стратегия - алгоритм дерева-выбора:
# занять угол, затем противоположный(если свободен) или любой ближайший
#   если противоположный - занять центр(если свободен) или любой угол;
#   если ближайший - если свободно между углами - занять, либо любой угол
#           если противоположный - занять между углами
#           если ближайший - занять между углами
import random
CORNERS = (0, 8, 2, 6)
BETWIXT = (1, 3, 5, 7)
ALL = (0, 1, 2, 3, 4, 5, 6, 7, 8)
step = 0
def computer_move(board, computer, human):
    board = board[:]
    global step
    print("Я выберу поле номер", end=" ")


# если честно - эти блоки можно убрать, всё писалось без него, но тогда ходы быстро становятся предсказуемы
    # особено этот
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:  # занять позицию, если есть победный вариант
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:  # начать защищаться, если следующим ходом игрок выиграет
            print(move)
            return move
        board[move] = EMPTY


# а ещё тут присутствует элемент случайности, что делает игру интереснее
# да, я знаю, что многие строки можно убрать в функции, но это я понял только потом и решил не переписывать
    for move in legal_moves(board):  # стратегия объяснена в начале
        if move in legal_moves(board):
            if step == 0:
                while step == 0:  # первый шаг
                    move = random.choice(CORNERS)
                    if move in legal_moves(board):
                        print(move)
                        step += 1
                        global c_s_n
                        c_s_n = move  # запоминаем полученную позицию на первом шаге
                        return move
            board[move] = EMPTY
            if step == 1:
                while step == 1:  # второй шаг
                    if c_s_n == 0:
                        move = 8
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            global c_s_tw
                            c_s_tw = move  # запоминаем полученную позицию на втором шаге
                            return move
                        else:
                            step_random_in_two_a = 0
                            while step_random_in_two_a == 0:
                                move = random.choice(CORNERS)
                                if move in legal_moves(board):
                                    print(move)
                                    step_random_in_two_a += 1
                                    step += 1
                                    c_s_tw = move  # запоминаем полученную позицию на втором шаге
                                    return move
                    elif c_s_n == 8:
                        move = 0
                        if move in legal_moves(board):
                                print(move)
                                step += 1
                                c_s_tw = move  # запоминаем полученную позицию на втором шаге
                                return move
                        else:
                                step_random_in_two_a = 0
                                while step_random_in_two_a == 0:
                                    move = random.choice(CORNERS)
                                    if move in legal_moves(board):
                                        print(move)
                                        step_random_in_two_a += 1
                                        step += 1
                                        c_s_tw = move  # запоминаем полученную позицию на втором шаге
                                        return move
                    elif c_s_n == 2:
                        move = 6
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            c_s_tw = move  # запоминаем полученную позицию на втором шаге
                            return move
                        else:
                            step_random_in_two_a = 0
                            while step_random_in_two_a == 0:
                                move = random.choice(CORNERS)
                                if move in legal_moves(board):
                                    print(move)
                                    step_random_in_two_a += 1
                                    step += 1
                                    c_s_tw = move  # запоминаем полученную позицию на втором шаге
                                    return move
                    elif c_s_n == 6:
                        move = 2
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            c_s_tw = move  # запоминаем полученную позицию на втором шаге
                            return move
                        else:
                            step_random_in_two_a = 0
                            while step_random_in_two_a == 0:
                                move = random.choice(CORNERS)
                                if move in legal_moves(board):
                                    print(move)
                                    step_random_in_two_a += 1
                                    step += 1
                                    c_s_tw = move  # запоминаем полученную позицию на втором шаге
                                    return move
            board[move] = EMPTY
#  вот тут до меня дошло, что я неадекватно называю переменные...
            if step == 2:
                while step == 2:  # третий шаг
                    if (c_s_n == 0 and c_s_tw == 8) or (c_s_n == 8 and c_s_tw == 0) or (c_s_n == 2 and c_s_tw == 6) or (c_s_n == 6 and c_s_tw == 2):
                        move = 4
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            global c_s_th
                            c_s_th = move  # запоминаем полученную позицию на третьем шаге
                            return move
                        else:
                            random_in_three = 0
                            while random_in_three == 0:
                                move = random.choice(CORNERS)
                                if move in legal_moves(board):
                                    print(move)
                                    random_in_three += 1
                                    step += 1
                                    c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                    return move
                    else:
                        if (c_s_n == 2 or 0) and (c_s_tw == 0 or 2):
                            move = 1
                            if move in legal_moves(board):
                                print(move)
                                step += 1
                                c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                return move
                            else:
                                random_in_three = 0
                                while random_in_three == 0:
                                    move = random.choice(CORNERS)
                                    if move in legal_moves(board):
                                        print(move)
                                        random_in_three += 1
                                        step += 1
                                        c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                        return move
                        if (c_s_n == 6 or 0) and (c_s_tw == 0 or 6):
                            move = 3
                            if move in legal_moves(board):
                                print(move)
                                step += 1
                                c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                return move
                            else:
                                random_in_three = 0
                                while random_in_three == 0:
                                    move = random.choice(CORNERS)
                                    if move in legal_moves(board):
                                        print(move)
                                        random_in_three += 1
                                        step += 1
                                        c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                        return
                        if (c_s_n == 8 or 2) and (c_s_tw == 2 or 8):
                            move = 5
                            if move in legal_moves(board):
                                print(move)
                                step += 1
                                c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                return move
                            else:
                                random_in_three = 0
                                while random_in_three == 0:
                                    move = random.choice(CORNERS)
                                    if move in legal_moves(board):
                                        print(move)
                                        random_in_three += 1
                                        step += 1
                                        c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                        return move
                        if (c_s_n == 8 or 6) and (c_s_tw == 6 or 8):
                            move = 7
                            if move in legal_moves(board):
                                print(move)
                                step += 1
                                c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                return move
                            else:
                                random_in_three = 0
                                while random_in_three == 0:
                                    move = random.choice(CORNERS)
                                    if move in legal_moves(board):
                                        print(move)
                                        random_in_three += 1
                                        step += 1
                                        c_s_th = move  # запоминаем полученную позицию на третьем шаге
                                        return move
            board[move] = EMPTY
            if step == 3:
                while step == 3:  # четвёртый шаг
                    if ((c_s_n and c_s_tw) or (c_s_tw and c_s_th) or (c_s_n and c_s_th)) == ((0 and 2) or (2 and 0)):
                        move = 1
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            global c_s_fo
                            c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                            return move
                        else:
                            random_in_four = 0
                            while random_in_four == 0:
                                move = random.choice(ALL)
                                if move in legal_moves(board):
                                    print(move)
                                    random_in_four += 1
                                    step += 1
                                    c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                                    return move
                    if ((c_s_n and c_s_tw) or (c_s_tw and c_s_th) or (c_s_n and c_s_th)) == ((0 and 6) or (6 and 0)):
                        move = 3
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                            return move
                        else:
                            random_in_four = 0
                            while random_in_four == 0:
                                move = random.choice(ALL)
                                if move in legal_moves(board):
                                    print(move)
                                    random_in_four += 1
                                    step += 1
                                    c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                                    return move
                    if ((c_s_n and c_s_tw) or (c_s_tw and c_s_th) or (c_s_n and c_s_th)) == ((2 and 8) or (8 and 2)):
                        move = 5
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                            return move
                        else:
                            random_in_four = 0
                            while random_in_four == 0:
                                move = random.choice(ALL)
                                if move in legal_moves(board):
                                    print(move)
                                    random_in_four += 1
                                    step += 1
                                    c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                                    return move
                    if ((c_s_n and c_s_tw) or (c_s_tw and c_s_th) or (c_s_n and c_s_th)) == ((6 and 8) or (8 and 6)):
                        move = 7
                        if move in legal_moves(board):
                            print(move)
                            step += 1
                            c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                            return move
                        else:
                            random_in_four = 0
                            while random_in_four == 0:
                                move = random.choice(ALL)
                                if move in legal_moves(board):
                                    print(move)
                                    random_in_four += 1
                                    step += 1
                                    c_s_fo = move  # запоминаем полученную позицию на четвёртом шаге
                                    return move
            board[move] = EMPTY
            if step == 4:  # пятый шаг, это условие не будет выполнено никогда, но пусть будет..
                rif = 0
                while rif == 0:
                    move = random.choice(ALL)
                    if move in legal_moves(board):
                        print(move)
                        rif += 1
                        return move
            board[move] = EMPTY

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд")

    if the_winner == computer:
        print("Как я и предсказывал, победа в очередной раз осталась за мной.")
    elif the_winner == human:
        print("Увы, но ты победил меня..")
    elif the_winner == TIE:
        print("Ничья.")


def main():
    display_instr()
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

input("\n\nНажмите Enter, чтобы выйти")