#Задача5.Вариант13.

#Напишите программу, которая бы при запуске случайным образом отображала
#имя одного из двенадцати апостолов.

#Попова Маргарита Александровна
#22.03.2016

import random
stuffing = random.randint(1,12)
if stuffing == 1:
  print('Андрей')
elif stuffing == 2:
  print('Петр')
elif stuffing == 3:
  print('Иоанн')
elif stuffing == 4:
  print('Иаков')
elif stuffing == 5:
  print('Филипп')
elif stuffing == 6:
  print('Варфоломей')
elif stuffing == 7:
  print('Матфей')
elif stuffing == 8:
  print('Фома')
elif stuffing == 9:
  print('Иаков')
elif stuffing == 10:
  print('Иуда Фаддей')
elif stuffing == 11:
  print('Симон')
elif stuffing == 12:
  print('Иуда Искариот')
input('Нажмите Enter для выхода')
