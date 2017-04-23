# Задача 7. Вариант 14.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Rozum R.S.
# 16.04.2017

import random

print("Программа случайным образом загадывает имя одного из трех официальных талисманов зимних Олимпийских игр, а игрок должен угадать его. Чем меньше попыток использует игрок, тем больше очков получит.")

number = random.randint(1,3)

if number == 1:
    mascot = "Леопард"
elif number == 2:
    mascot = "Белый Мишка"
elif number == 3:
    mascot = "Зайка"

points = 100
attempt = 1

answer = input("Назовите имя одного из талисманов: ")

while answer != mascot:
    attempt += 1
    answer = input("Не правильно! Попробуйте еще раз: ")
    if (points - attempt * 10)  <= 0:
        print("Конец игры! Кол-во очков: ", points - attempt*10)
        break


if answer == mascot:
    points -= attempt * 10
    print("Вы угадали! Кол-во очков: ", points, ". Кол-во попыток: ", attempt)
    print("Правильный ответ: ", mascot)

#while answer != mascot:
#   points -= 1
#   answer = input("Не правильно! Попробуйте еще раз: ")
#   if points == 0:
#      print("Конец игры! Кол-во очков: ", points)
#       break

#if answer == mascot:
#    print("Вы угадали! Кол-во очков: ", points)


input("\nНажмите Enter для выхода.")