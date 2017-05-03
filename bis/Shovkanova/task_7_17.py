#Задача 7. Вариант 17.

#Создайте игру, в которой компьютер загадывает название
#одного из пяти космических челноков проекта Спейс шаттл,
#а игрок должен его угадать.

#Шовканова Г.Д.
#19.03.2017

import random
print('Программа случайным образом загадывает название одного из пяти шаттлов проекта Spase Shuttle, а игрок должен его угадать.')
tries = 1
score = 1500
number = random.randint(1,5)
if number == 1:
	realname = 'Колумбия'
elif number == 2:
	realname = 'Челленджер'
elif number == 3:
	realname = 'Дискавери'
elif number == 4:
	realname = 'Атлантис'
elif number == 5:
	realname = 'Индевор'
name = input('\n\nНазовите один из шаттлов, входящих в проект Spase Shuttle: ')
while name != realname:
	tries += 1
	score -= 100
	name = input('\n\nПопробуйте снова:')
print('Верно! Это', realname, 'Вам потребовалось', tries, 'попыток')
print('Начислено' , score , 'очков')

input('\n\nPress Enter')