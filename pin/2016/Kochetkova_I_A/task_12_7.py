#-*- coding: 1251-*-
# Задача 12 Вариант 7
# Разработайте	игру	"Крестики-нолики".	(см.	М.Доусон	Программируем	на	Python гл.	6).
# Kochetkova I.A
# 17.04.2017

X='X'
O='O'
EMPTY=' '
TIE='Ничья'
num_s=9
from os import system,name
def cls(): system('cls' if name=='nt' else 'clear')

def display_instruction():
    print('''Добро пожаловать в игру старую, как мир - крестики нолики! 
    Чтоб сделть ход введите соответсвующую цифру: 
            0 | 1 | 2 
            --------- 
		    3 | 4 | 5 
		    --------- 
		    6 | 7 | 8 
  Все предельно просто \n''')

def ask_yes_no(question):
    response=None
    while response not in ('да','нет'):
        response=input(question)        
    return response

def ask_number(question,low,high):
    response=None
    while response not in range(low,high):
        response=input(question)
        if response in ('0','1','2','3','4','5','6','7','8'):
            response=int(response)
    return response

def pieces():
    go_first=ask_yes_no('Хочешь ходить первым? (да/нет) ')
    if go_first=='да':
        print('Ты первый')
        human=X 
        comp=O  
    else:
        print('Первым хожу я ')
        human=O
        comp=X  
    return comp,human

def new_board():
    board=[]
    for square in range(num_s):
        board.append(EMPTY)
    return board

def display_board(board):
    print('\n\t',board[0],'|',board[1],'|',board[2],)
    print('\t','---------')
    print('\n\t',board[3],'|',board[4],'|',board[5],)
    print('\t','---------')
    print('\n\t',board[6],'|',board[7],'|',board[8],'\n')

def legal_moves(board):
    moves=[]
    for square in range(num_s):
        if board[square]==EMPTY:
            moves.append(square)
    return moves

def winner(board):
    ways_to_win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in ways_to_win:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board,human):
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number('Выбери 0-8 ',0,num_s)
        if move not in legal:
            print('Выбери другое, это поле зянято ')
    print('Твой ход учтен')
    return move

def comp_move(board,comp,human):
    board=board[:]
    best_moves=(4,0,2,6,8,1,3,5,7)
    print('Я выбираю поле под номером ',end=' ')
    for move in legal_moves(board):
        board[move]=comp
        if winner(board)==comp:
            print(move)
            return(move)
        board[move]=EMPTY
    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return(move)
        board[move]=EMPTY
    for move in best_moves:
        if move in best_moves:
            if move in legal_moves(board):
                print(move)
                return(move)

def next_turn(turn):
    if turn==X:
        return O    
    else:
        return X

def congrat_winner(the_winner,comp,human):
    if the_winner!=TIE:
        print('Три',the_winner,'в ряд!\n')
    else:
        print('Ничья')
    if the_winner==comp:
        print('Я выиграль')
    elif the_winner==human:
        print('Ты победил')
    elif the_winner==TIE:
        print('Ничья')

def main():
    display_instruction()
    comp,human=pieces()
    cls()
    turn=X
    board=new_board()
    display_board(board)
    while not winner(board):
        if turn==human:
            move=human_move(board,human)
            cls()
            board[move]=human
        else:
            move=comp_move(board,comp,human)
            board[move]=comp
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner,comp,human)

main()
input('нажмите ентер')
    