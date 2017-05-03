#Задача5.Вариант3. 

#Напишите программу, которая бы при запуске случайным образом отображала название одного из цветов радуги.

#Вырыпаева П. В.
#21.03.2017

import random
stuffing = random.randint(1, 7)
if stuffing == 1:
    print('красный')
elif stuffing == 2:
    print('оранжевый')
elif stuffing == 3:
    print('желтый')
elif stuffing == 4:
    print('зеленый')
elif stuffing == 5:
    print('голубой')
elif stuffing == 6:
    print('синий')
elif stuffing == 7:
    print('фиолетовый') 
input('Нажмите Enter, чтобы покинуть игру')
