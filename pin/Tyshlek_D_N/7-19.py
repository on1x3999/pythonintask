# Задача 7. Вариант 19.
# Создайте игру, в которой компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.
# Tyshlek D.N.
# 18.04.2017

import random

print("Программа случайным образом загадывает имя одного из семи городов, а игрок должен угадать его.")

number = random.randint(1,7)

if number == 1:
    city = "Москва"
elif number == 2:
    city = "Санкт-Питербург"
elif number == 3:
    city = "Сочи"
elif number == 4:
    city = "Раменское"
elif number == 5:
    city = "Домодедово"
elif number == 6:
    city = "Волгоград"
elif number == 7:
    city = "Краснодар"

    points = 100
    attempt = 1

answer = input("Назовите город из России: ")

    while answer != city:
        attempt += 1
        answer = input("Не правильно! Попробуйте еще раз: ")
        if (points - attempt * 10) <= 0:
            print("Конец игры! Кол-во очков: ", points - attempt * 10)
            break

    if answer == city:
        points -= attempt * 10
        print("Вы угадали! Кол-во очков: ", points, ". Кол-во попыток: ", attempt)
        print("Правильный ответ: ", city)

    # while answer != city:
    #   points -= 1
    #   answer = input("Не правильно! Попробуйте еще раз: ")
    #   if points == 0:
    #      print("Конец игры! Кол-во очков: ", points)
    #       break

    # if answer == city:
    #    print("Вы угадали! Кол-во очков: ", points)


    input("\nНажмите Enter для выхода.")
