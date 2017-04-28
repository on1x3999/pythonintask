# Задача 12. Вариант 15
# Разработайте игру "Крестики-нолики"

# Чесноков Илья Сергеевич
# 18.03.2017

import random

# Data
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
authors = { "computer": 1, "human": 2 }

# Functions
def fieldSymbol(field):
    if board[field] == authors['human']:
        return "X"
    elif board[field] == authors['computer']:
        return "O"
    else:
        return field + 1

def showBoard(override = None):
    if override != None:
        array = override

        print(array[0], "|", array[1], "|", array[2])
        print(array[3], "|", array[4], "|", array[5])
        print(array[6], "|", array[7], "|", array[8])
    else:
        print(fieldSymbol(0), "|", fieldSymbol(1), "|", fieldSymbol(2))
        print(fieldSymbol(3), "|", fieldSymbol(4), "|", fieldSymbol(5))
        print(fieldSymbol(6), "|", fieldSymbol(7), "|", fieldSymbol(8))

def move(field, author):
    if field < 1 or field > 9:
        print("Неверный номер поля!")
        return None

    if board[field - 1] != 0:
        return None

    board[field - 1] = authors[author]
    return True

def checkWin(author):
    checkValue = authors[author]

    win_ways = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    for way in win_ways:
        if board[way[0] - 1] == board[way[1] - 1] == board[way[2] - 1] == checkValue:
            return True

    return False

def findWin():
    if checkWin("computer"):
        print("Компьютер победил!")
        
        return True
    elif checkWin("human"):
        print("Вы победили!")

        return True
    return False

def AI_move():
    moves = (5, 1, 3, 7, 9, 2, 4, 6, 8)
    
    for field in moves:
        if move(field, "computer") == True:
            print("Я выбираю поле номер", field)
            break

def main():
    print("Добро пожаловать в игру Крестики-нолики!\nТы должен вводить номер поля от 1 до 9, в соответствии с доской снизу!\nЯ играю за нолики, ты за крестики")
    showBoard(range(1, 10))

    print("\nХоди первым!")

    while True:
        # Проверка на победу
        if findWin():
            break
            
        # Ввод
        field = input("Введите поле для хода: ")
        
        # Осуществление хода
        if move(int(field), "human") == None:
            print("Неверное поле!")
            continue
        
        # Проверка на победу
        if findWin():
            showBoard()
            break
        
        # Ход AI
        print("Хорошо")
        AI_move()

        # Показ доски
        showBoard()

main()