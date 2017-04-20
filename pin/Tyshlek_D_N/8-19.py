# Задача 8. Вариант 19.
# Доработайте игру "Анаграммы"(см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# TyshleK D.N
# 18.04.2017

import random

WORDS = ("нож", "топор", "катана", "тесак", "секира", "меч", "коса", "кинжал", "заточка", "арбалет", "лук", "пистолет", "пулемет", "петух", "таракан", "картон", "гнездо", "карта", "болт", "вулкан", "дракон", "лицо")

word = random.choice(WORDS)
correct = word
jumble =""
score = 1000000
attempt = 1
hint_num = 0



while word:
    position = random.randrange(len(word))
    jumble+=word[position]
    word = word[:position]+word[(position+1):]

print("Добро пожаловать в игру анаграммы!",
      "\nНадо переставить буквы так, чтобы получилось слово."
      )
print("Анаграмма - ", jumble)
guess=input("Попробуйте отгадать слово: ")

while guess != correct:
    print("Не правильно!")
    guess = input("Попробуйте еще раз: ")
    attempt += 1
    score -= attempt*5
    if score <= 0:
        print("GameOver! Кол-во попыток - ", attempt, ". Кол-во подсказок = ", hint_num, ". Кол-во очков - 0")
        break
    if guess == correct:
        break
    hint = input("Использвать подсказку? (y/n)")
    if hint == "y":
        score -= 50
        hint_num += 1
        n = random.randint(0, len(correct))
        print("Буква номер ", n+1, " - ", correct[n])
        guess = input("Попробуйте еще раз: ")
    else:
        guess = input("Попробуйте еще раз: ")



if guess == correct:
    print("Вы угадали! Кол-во попыток - ", attempt, ". Кол-во подсказок = ", hint_num, ". Кол-во очков - ", score)

input("\nНажмите Enter для выхода.")