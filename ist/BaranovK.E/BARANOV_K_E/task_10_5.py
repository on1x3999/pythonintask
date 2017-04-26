# Задача 10. Вариант 5.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Baranov K. E.
# 16.04.2017

import re

pool = 30
power = 0
health =0
wisdom = 0
skill = 0
name = input('\nВведите имя персонажа: ')
print('\nДля изменения параметров персонажа введите название свойста и количество пунктов с плюсом(чтобы увеличить) и с минусом(чтобы отнять)\n')


def printProperty():
    msg = ('\nИмя: ' + str(name)
          +'\nЛимит пунктов: ' + str(pool)
          +'\nСила: ' + str(power)
          +'\nЗдоровье: ' + str(health)
          +'\nМудрость: ' + str(wisdom)
          +'\nЛовкость: ' + str(skill) + '\n')
    print(msg)
    

def checkResponse(value, response):
    global pool
    n = re.findall('(\d+)', response)
    if len(n) > 0:
        n = int(n[0])
        if '+' in response:
            if (pool - n) >= 0:
                pool -= n
                value += n
                return value
            else:
                print('Лимит пунктов позволяет использовать значения до ', pool)
        elif '-' in response:
            if (value - n) >= 0:
                pool += n
                value -= n
                return value
            else:
                print('Невозможно убавить значение ', value, ' на ', n)
        else:
            print('Вы не указали знак +/-')
    else:
        print('Вы не ввели число')
    return value

        
printProperty()
response = input('>>').lower()
while response != '':
    if 'сила' in response:
        value = checkResponse(power, response)
        if power != value:
            power = value
            printProperty()
    elif 'здоровье' in response:
        value = checkResponse(health, response)
        if health != value:
            health = value
            printProperty()
    elif 'мудрость' in response:
        value = checkResponse(wisdom, response)
        if wisdom != value:
            wisdom = value
            printProperty()
    elif 'ловкость' in response:
        value = checkResponse(skill, response)
        if skill != value:
            skill = value
            printProperty()
    else:
        print('У персонажа нет такого свойства')
    response = input('>>').lower()
        
input('\n\nНажмите Enter для выхода')
