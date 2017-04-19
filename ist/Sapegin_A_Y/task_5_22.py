# Задача 5. Вариант 22.
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух сооснователей компании Google.
# Sapegin A.Y.
# 06.03.2017

import random

creators = ['Сергей Брин', 'Лари Пэйдж']
n = random.randint(0, len(creators)-1)
print(creators[n])

input('\n\nНажмите Enter для выхода.')