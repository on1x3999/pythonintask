# Задача 7. Вариант 22.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# Sapegin A.Y.
# 06.03.2017

import random

print('Программа случайна загадывает имена основателей рима.'
      +'\nУ вас есть 10 балла. Если угадаете +5 балл, если нет -5:'
      +'\nНаберите 20 баллов')
account = 10;

while(account !=0 and account <20):
    answer = input('\n1 - Рэм, 2 - Ромул'
                   +'\nВаш ответ: ')
    n = random.randint(1,2)
    if(int(answer) == n):
        account = account+5
        result = '\nВерно. Ваши баллы: ' + str(account)
    else:
        account = account-5
        result = '\nНеверно. Ваши баллы: ' + str(account)
    print(result)
if(account == 20):
    print('Вы победили')
else:
    print('Вы проиграли')
input('\n\nНажмите Enter для выхода.')