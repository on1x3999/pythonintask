# Задача 6. Вариант 6.
# Создайте игру, в которой компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.

# Горлов Евгений Михайлович
# 07.03.2017

import random
RandomNumber = random.randint(1,7)
if RandomNumber == 1:
    City = 'Москва'
elif RandomNumber == 2 :
    City = 'Санкт-Петербург'
elif RandomNumber == 3 :
    City = 'Самара'
elif RandomNumber == 4 :
    City = 'Екатеринбург'
elif RandomNumber == 5 :
    City = 'Казань'
elif RandomNumber == 6 :
    City = 'Волгоград'
elif RandomNumber == 7 :
    City = 'Омск'
print ('Угадайте один из этих городов:Москва,Санкт-Петербург,Самара,Екатеринбург,Казань,Волгоград,Омск')
Choice = input ('Введите название города:')
if City == Choice :
    print ('Поздравляем вы угадали город:', City)
else:
    print ('К сожалению вы не угадали')
print ('Это:', City)	
input ('Нажмите Enter')
