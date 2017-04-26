#Задача 8. Вариант 14
#Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен получать прево на подсказку в том случае, если у него нет никаких предположений.
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

#Kartinceva A.U.
#20.04.17

import random

WORDS = ("рысь", "панда", "пиранья", "анастасия", "университет","сериал","фильм","торговый центр","анаконда","барс","леопард","кошка","словарь","автомат","кофе","зубочистка","неко")


def createJumbled(word):
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return jumble

print(
"""
\t\t\tПривет! Добро пожаловать в "Анаграммы"!
\n\t\tПравила просты! Чем меньше подсказок ты используешь, тем больше баллов получишь!
"""
)
score = 5000
helpcount = 0
totalGame = 0
playMore = "yes"

while playMore == "yes":
    word = random.choice(WORDS)
    index = WORDS.index(word)
    correct = word
    jumble = createJumbled(word)
    print("Анаграмма: ", jumble)
    print("\nЕсли нужна подсказка, введи 'yes'. Если нет - 'no'.")

    help = input("Будешь брать подсказку?: ")
    if help == "yes":
        hint = word[0] + word [1]
        print(hint)
        helpcount += 1
        guess = input("\nТвой ответ: ")

    elif help == "no":
        guess = input("\nТвой ответ: ")

    while guess != correct and guess != "":
        print("Увы! Это неправильный ответ!")
        print("\nЕсли нужна подсказка, введи 'yes'. Если нет - 'no'.")
        help = input("Будешь брать подсказку?: ")
        if help == "yes":
            hint2 = HINTS[index]
            print(hint2)
            helpcount += 2
        guess = input("Твой ответ: ")

    if guess == correct:
        print("Верно! Ты угадал!")

    if helpcount == 0:
        print("Ты даже не использовал не одной подсказки! Насколько же ты крутой!\n")
    totalGame += 1
    print("\nЧтобы продолжить играть, набери 'yes'.")
    playMore = input("Ты хочешь сыграть еще?: ")

print("\n")
print("Игр сыграно: ",totalGame)
print("Ты использовал подсказок: ",helpcount)
print("Твой счёт: ",(score-(totalGame*helpcount)))
 
input("\nНажми Enter, чтобы выйти! Удачи!")
