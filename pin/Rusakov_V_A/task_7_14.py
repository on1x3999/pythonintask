# Задача 7. Вариант 9.

# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Русаков В.А.
# 15.04.2017

import random

print("Программа случайным образом загадывает название одного из 3-х талисманов, а игрок должен его угадать.")

talisman_numbers = random.randint(1, 3)

if talisman_numbers == 1:
    talisman = 'Леопард'
elif talisman_numbers == 2:
    talisman = 'Мишка'
elif talisman_numbers == 3:
    talisman = 'Зайка'

trial = 3
bonus = 3000

while trial > 0:
    answer = input('\nНазовите одного из талисманов: ')
    if answer == talisman:
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else:
        print('\nВы не угадали!!!')
        if trial > 1:
            print('Попробуйте еще раз.')
        else:
            print('Правильный ответ: ', talisman)

    trial -= 1
    bonus -= 1000

input("\n\nНажмите Enter для выхода.")
