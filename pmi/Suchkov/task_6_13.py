# Задача 6. Вариант 13. 
# Создайте игру, в которой компьютер загадывает название
#одного из двух спутников Марса, а игрок должен его угадать.


# Suchkov R.A. 
# 12.03.2017


import random
a = ('Фобос' , 'Деймос')
b = (random.choice(a))
ans = input ('Попробуйте угадать один из спутников Марса:')
if ans == b:
    print ("Поздравляю, это правильный ответ!!!")
else:
    print ("Ты не угадал((")
input ()
