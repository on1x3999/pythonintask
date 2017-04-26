# Задача 5. Вариант 19.
# Напишите программу, которая бы при запуске случайным образом отображала название одной из восьми планет Солнечнойсистемы.

# Tyshlek D.N.
# 18.04.2017

import random


print("Программа случайным образом отображает название одной из восьми планет Солнечной системы.")

planeta = random.randint(1, 8)

print('\n Планеты Солнечной системы:', end=' ')

if planeta == 1:
    print('Земля')
elif planeta == 2:
    print('Марс')
elif planeta == 3:
    print('Нептун')
elif planeta == 4:
    print('Венера')
elif planeta == 5:
    print('Юпитер')
elif planeta == 6:
    print('Уран')
elif planeta == 7:
    print('Сатурн')
elif planeta == 8:
    print('Меркурий')
input("\n\nНажмите Enter для выхода.")