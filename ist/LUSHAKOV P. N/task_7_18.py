# Задача 7. Вариант 18.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Lushakov P. N.
# 01.03.2017

import random

print('Каждый раз программа загадывает одну из трёх жён зевса.'
      +'\nУ вас есть з балла. Если угадаете +1 балл, если нет -1:'
      +'\nНаберите 6 баллов')
account = 3;

while(account !=0 and account <6):
    answer = input('\n1 - Метида, 2 - Фемида, 3 - Гера'
                   +'\nВаш ответ: ')
    n = random.randint(1, 3)
    if(int(answer) == n):
        account = account+1
        result = '\nВерно. Ваши баллы: ' + str(account)
    else:
        account = account-1
        result = '\nНеверно. Ваши баллы: ' + str(account)
    print(result)
if(account == 6):
    print('Вы победили')
else:
    print('Вы проиграли')
input('\n\nНажмите Enter для выхода.')