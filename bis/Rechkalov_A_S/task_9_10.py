# Задание 9. Вариант 10.
# Rechkalov A.S.

# 29.03.17

import random
count = 0
WORDS = ("Контакт", "Пиво", "Одиночество", "Программист", "#ВсяСутьВОднойИгре")
pobeda = random.choice(WORDS)

print("Я выбрал, в слове", len(pobeda), "букв. У тебя 5 попыток.")

while count < 5:
    count += 1
    guessChar = input("Твой ход: ")
    if guessChar.lower() in pobeda.lower():
        print("Да")
    else:
        print("Нет")

guessWord = input("Время угадывать: ")
if guessWord == pobeda:
    print("Поздравления")
else:
    print("Не, покеда")

input("\n\nЖми Enter ")

