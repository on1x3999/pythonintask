# Задача 6, Вариант 5 
# Создайте игру, в которой компьютер загадывает один из трех цветов светофора, а игрок должен его угадать.

# Исламов Р.Р.
# 18.03.2017

import random
print("Отгадайте один из трех цветов светофора")
print("У вас две попытки")
color = int(input("Введите число: "))
x = random.randint(1, 3)
time = 1
while color != x:
    if color < x:
        print("Не верно")
    elif color > x:
        print("Не верно")
    if time == 2:
        print("Это была последняя попытка")
        break
    color = int(input("Введите число: "))
    time += 1
if color == x:
    print("Да вы отгдали!!!Это было число", x)
else:
    print("Вы не угадали!!!Это было число",x)
print('Программа выбрала', end=" ")
if color == 1 :
    print("Красный")
elif color == 2 :
    print("Желтый")
elif color == 3 :
    print("Зеленый")
		
input ('Нажмите Enter для выхода')
