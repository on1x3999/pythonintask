#Задача 7. Вариант 3

#Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

#Zak L.S.
#9.04.2017

import random
print ('Отгадайте имя одной  из птиц игры Angry Birds ')
def get_random_bird():
   birds = ("Ред","Чак","Бомб","Матильда","Хэл","Теренс","Бабблз","Стелла")
   return random.choice(birds)
bird = get_random_bird()
user_bird = input('Введите ваш вариант: ')
ball = 5
while bird.lower() != user_bird.lower() and ball >1:
    ball -= 2
    print('У вас остлось', ball, 'баллов', 'Попробуйте ещё раз')
    user_bird = input('Введите ваш вариант: ')
if ball > 1:
   print("Да вы отгдали!"'У вас остлось', ball)
else:
    print('Баллы закончились, а вы не угадали имя ')
input ('Нажмите Enter для выхода')