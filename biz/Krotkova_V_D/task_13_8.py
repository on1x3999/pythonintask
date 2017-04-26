#Задача 12. Вариант 8.
#Разработайте игру "Крестики-нолики". 
#(см. М.Доусон Программируем на Python гл. 6).  

#Krotkova V.D
#23.04.2017

#глобальные константы
X="X"
O="O"
Empty=" "
draw="Ничья"
Square_number=9

def instructions():   
    print("""
    Добро подаловать на ринг грандиознейших интеллектуральных сосотязаний всех времен.  
    Твой мозг и компьютер сойдуться в схватке за доской игры "Крестики-нолики".  
    Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям доски - 
    так как показано ниже:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
    Приготовься к бою, жалкий человечишка. Вот вот начнется решающее сражение. \n
    """)
    
def ask_yes_no(question):
    response = None
    while response not in ("Да", "Нет"):
        response = input(question)
    return response
 
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response 
 
def pieces():
    go_first = ask_yes_no("Ты будешь ходить первым? (Да/Нет): ")
    if go_first == "Да":
        print("\nХорошо, тогда ходи крестиками.")
        human = X
        computer = O
    else:
        print("\nТак, я хожу! Ты играешь ноликами.")
        computer = X
        human = O
    return computer, human
     
def new_board():
    board = []
    for square in range(Square_number):
        board.append(Empty)
    return board
     
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])
     
def legal_moves(board):
    moves = []
    for square in range(Square_number):
        if board[square] == Empty:
            moves.append(square)
    return moves
     
def winner(board):
    ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in ways:
        if board[row[0]] == board[row[1]] == board[row[2]] != Empty:
            winner = board[row[0]]
            return winner
        if Empty not in board:
            return draw
    return None
     
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери поле (0-8):", 0, Square_number)
        if move not in legal:
            print("\n-.- Серьезно? Ты не видишь, что поле занято? Выбери другое поле\n")
    return move
     
def computer_move(board, computer, human):
    board = board[:]
    print("Я выберу поле № ")
    ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in ways:
        for cell in row:
            if board[cell] == Empty:
                board[cell] = computer
                return cell
             
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
         
def congrat_winner(the_winner, computer, human):
    if the_winner != draw:
        print("Три", the_winner, "!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Я победил! И как ты только мог надеяться одержать надо мной победу? Глупец!")
    elif the_winner == human:
        print("Ты выиграл! Но даже не расчитывай, что это повториться вновь! Дуракам везет..")
    elif the_winner == draw:
        print("Неожиданный поворот!")
         
def main():
    print("\t\tЭто инструкция для игры в 'Крестики-нолики':")
    instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while  not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner, computer, human)
     
main()
input("Press Enter for Exit")
