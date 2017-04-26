# Задача 5. Вариант 14.
# Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати башен Московского кремля.

# Русаков В.А.
# 14.04.2017

import random

print("Программа случайным образом отображает название одной из двадцати башен Московского кремля.")

bashnya = random.randint(1, 20)

print('\nЭто башня:', end=' ')

if bashnya == 1:
    print('Беклемишевская')
elif bashnya == 2:
    print('Константино-Еленинская')
elif bashnya == 3:
    print('Набатная башня')
elif bashnya == 4:
    print('Царская башня')
elif bashnya == 5:
    print('Спасская ')
elif bashnya == 6:
    print('Сенатская башня')
elif bashnya == 7:
    print('Никольская башня')
elif bashnya == 8:
    print('Угловая Арсенальная')
elif bashnya == 9:
    print('Средняя Арсенальная')
elif bashnya == 10:
    print('Троицкая башня')
elif bashnya == 11:
    print('Кутафья башня')
elif bashnya == 12:
    print('Комендантская')
elif bashnya == 13:
    print('Оружейная')
elif bashnya == 14:
    print('Боровицкая')
elif bashnya == 15:
    print('Водовзводная')
elif bashnya == 16:
    print('Благовещенская башня')
elif bashnya == 17:
    print('Тайницкая башня')
elif bashnya == 18:
    print('Первая Безымянная башня')
elif bashnya == 19:
    print('Вторая Безымянная башня')
elif bashnya == 20:
    print('Петровская')

input("\n\nНажмите Enter для выхода.")
