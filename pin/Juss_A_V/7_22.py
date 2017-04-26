#Задача 7. Вариант 22
#	Разработайте	систему	начисления	очков	для	задачи	6,	в	соответствии	с	которой игрок	получал	бы	большее	количество	баллов	за	меньшее	количество	попыток.
#Juss A.V.
#18.04.2017
import random

print("Программа случайным образом загадывает имя одного из двух братьев, легендарных основателей Рима")

number = random.randint(1,2)

if number == 1:
    name = "Ромул"
elif number == 2:
    name = "Рем"

points = 100
attempt = 1
answer = input('назови имя одного из основателей')

while answer != name:
    attempt += 1
    answer = input("Не правильно! Попробуйте еще раз: ")
    if (points - attempt * 10) <= 0:
        print("Конец игры! Кол-во очков: ", points - attempt*10)
        break


if answer == name:
    points -= attempt * 10
    print("Вы угадали! Кол-во очков: ", points, ". Кол-во попыток: ", attempt)
    print("Правильный ответ: ", name)

    input("\nНажмите Enter для выхода.")