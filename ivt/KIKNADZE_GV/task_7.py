# Задача 7. Вариант 22.
# Разработайте систему начисления очков для задачи 6,
# в соответствии с которой игрок получал бы большее
# количество баллов за меньшее количество попыток.
# Kiknadze G.V.
# 2017-02-28

import random, math

names=("Ромул, Рем")
print("Программа случайным образом загадывает имена двух братьев, легендарных основателей Рима. Попробуйте угадать это имя.")
print("Для выхода из игры нажмите Enter.")
score=0
attempts=0

while 1:
    computer=names[random.randint(0, 1)]
    print()
    print("Компьютер загадал новое слово.")
    print("Ваши баллы на счету: " + str(score))

    while 1:
        user=input("Попытайтесь угадать имя: ")
        if user == "":
            break

        if user == computer:
            print("Вы угадали! Это " + computer)
            break
        else:
            print("Вы не угадали.")
            attempts += 1;

    if user != "":
        print("Вы заработали баллов: " + str(max(3 - math.floor(attempts / 2), 1)))
        score += max(3 - math.floor(attempts / 2), 1)
        attempts = 0
    else:
        break