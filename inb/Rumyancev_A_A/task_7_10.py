# Задача 7. Вариант 10.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.




# Румянцев А.А.
# 16.03.2017

import random

listing = ['Германия', 'Австро-Венгрия', 'Италия', ]
game = random.choice(listing)
count = 0
points = 0
pointso = 0
while True:
    player = input('\nВведите название страны, входившей в Тройственный Союз: ')
    if (player == game):
        print ('Верно угадано!')
        points = 2000-(count*1000)
        pointso = pointso + points
        print('Заработано очков: ', points)
        conf = input('\nПопробовать ещё раз? ')
        if conf == 'N':
            break
        else: 
            count = 0
    else:
        print('Попробуйте ещё!')
        count = count + 1

print('\nЗаработано всего очков: ', pointso)

input('\nНажмите Enter')