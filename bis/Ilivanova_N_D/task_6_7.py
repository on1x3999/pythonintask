# Задача 6, Вариант 7
# Создайте игру, в которой компьютер загадывает имя одного из двух сооснователей компании Google, а игрок должен его угадать.

# Иливанова Н.Д.
# 20.04.2017

import random
founders = random.randrange(2)
founder = ("Сергей Брин","Ларри Пейдж")
print ('Отгадайте название одного из двух сооснователей компании Google ')
user_founder = input ('Введите Ваш вариант: ')
while user_founder.lower() != founder[founders].lower():
    user_chudo = input ('Вы не угадали,попробуйте ещё раз: ')
print ('Вы угадали!')
input ('Нажмите Enter для выхода')
