# Задача 13. Вариант 15
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой стратегией.

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
    strategies = ((1, 5, 7, (4, 3, 9)), # Угловые стратегии с большим треугольником
                  (1, 3, 5, (2, 7, 9)),
                  (3, 5, 9, (1, 6, 7)),
                  (5, 7, 9, (1, 3, 8)),
                  
                  (1, 2, 4, (3, 7)), # Угловые стратегии с маленьким треугольником
                  (2, 3, 6, (1, 9)),
                  (6, 8, 9, (3, 7)),
                  (4, 7, 8, (1, 9)))
    
    picked = False
    for strategy in strategies:
        print("Проверка стратегий")
        if (board[strategy[0] - 1] == 1 or board[strategy[0] - 1] == 0 and
            board[strategy[1] - 1] == 1 or board[strategy[1] - 1] == 0 and
            board[strategy[2] - 1] == 1 or board[strategy[2] - 1] == 0):

            if board[strategy[0] - 1] == 1 and board[strategy[1] - 1] == 1 and board[strategy[2] - 1] == 1:
                for field in strategy[3]:
                    if move(field, "computer") == True:
                        print("Я выбираю поле номер", field)

                        picked = True
                        break

            if picked == True: break

            for element in strategy:
                if element == strategy[3]:
                    break
                
                if move(element, "computer") == True:
                    print("Я выбираю поле номер", element)

                    picked = True
                    break

    
    if picked == False:
        array = range(1, 10)
        
        while True:
            pick = random.choice(array)

            if move(pick, "computer") == True:
                print("Я случайно выбираю поле номер", pick)
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