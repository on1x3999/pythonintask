# Задача 6. Вариант 17.

# Создайте игру, в которой компьютер загадывает название
# одного из пяти космических челноков проекта Spase Shuttle,
# а игрок должен его угадать.

#Шовканова Г.Д.
#18.03.2017

import random

print(
'Программа случайным образом загадывает название одного из пяти шаттлов проекта Spase Shuttle, а игрок должен его угадать.')
name = input('\n\nНазовите один из шаттлов, входящих в проект Spase Shuttle: ')
number = random.randint(1, 5)
if number == 1:
    realname = 'Колумбия'
elif number == 2:
    realname = 'Челленджер'
elif number == 3:
    realname = 'Дискавери'
elif number == 4:
    realname = 'Атлантис'
else:
    realname = 'Индевор'
if name == realname:
    print('Верно! Это', realname, '\nКак вам удалось угадать?')
else:
    print('Вы ошиблись.')

input('\n\nPress Enter')