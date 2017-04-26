# Задание 9. Вариант 14.
# Tsukanov K.M.

# 06.04.17

import random
count = 0
WORDS = ("дом", "книга", "окно", "питон")
win = random.choice(WORDS)

print("Слово выбрано, в нем", len(win), "букв. У тебя 5 попыток, чтобы угадать его буквы.")

while count < 5:
    count += 1
    guessChar = input("Твой ход: ")
    if guessChar.lower() in win.lower() and guessChar != "":
        print("Да")
    else:
        print("Нет")

guessWord = input("Пора угадывать: ")
if guessWord == win:
    print("Поздравляем! Вы победили!")
else:
    print("Вы не угадали!")

input("\n\nЖми Enter ")

