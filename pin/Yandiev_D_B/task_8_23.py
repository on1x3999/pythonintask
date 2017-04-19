# Задание 8. Вариант 23.
# Яндиев Д. Б.

# 1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# 15.04.17

import random

WORDS = ("python", "programm", "computer", "github")
word = random.choice(WORDS)
win = word
tip = win
annagrama = ""
count = 0


while word:
    position = random.randrange(len(word))
    annagrama += word[position]
    word = word[:position] + word[(position+1):]

print ("Анаграмма:", annagrama)
print("Не знаешь и хочешь подсказку? Нажми Enter")
guess = input("\nВаше предположение: ")

while 0<1:
    if guess == "":
        count += 1
        if len(win) == 1:
            print("Осталась одна буква! Так не честно!")
            break
                print (tip[0])
        tip = tip[1:]
        guess = input("\nВаше предположение: ")
        
    elif guess != win:
        print("Вы не угадали!")
        guess = input("Попробуйте еще раз ")

    elif guess == win:
                result = 1000-count*100
        print("Вы угадали! Ваш результат: ", result)
        break
    

input("\n\nEnter, чтобы выйти. ")
