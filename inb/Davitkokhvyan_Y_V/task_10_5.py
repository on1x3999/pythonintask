# Задача 10. Вариант 5
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Давиткохвян Юрий Васильевич
# 20.04.2017

import random

# Func
def FindKey(key, hash):
    try:
        return hash[key]
    except KeyError:
        return None

# Текст
print("У вас есть 30 очков для распределения между характеристиками (Сила, Здоровье, Мудрость, Ловкость)")
print("Введите через пробел название характеристики и очки, которые вы хотите ему присвоить (либо - очки для вычитания)")

# Данные
pointspool = 30

# Характеристики
characteristics = { "Сила": 0, "Здоровье": 0, "Мудрость": 0, "Ловкость": 0 }

while True:
    data = input("Введите данные: ")

    if data == 'конец':
        print("\n\nХарактеристики Вашего персонажа:\n")
        print("Сила:", characteristics['Сила'], "Здоровье:", characteristics['Здоровье'], "Мудрость", characteristics['Мудрость'], "Ловкость", characteristics['Ловкость'], "\n")
        
        print("Оставшиеся очки:", pointspool)
        break
    
    splitted = data.split(" ")

    if len(splitted) != 2:
        print("Вы ввели неправильные данные")
        continue
    
    if FindKey(splitted[0], characteristics) == None:
        print("Вы ввели неправильную характеристику")
        continue
    
    if pointspool < int(splitted[1]):
        print("У Вас не хватает очков в пуле!")
        continue

    characteristics[splitted[0]] += int(splitted[1])
    pointspool -= int(splitted[1])

    print("Ваш пул:", pointspool, "очков\n")
    print("Текущие характеристики:\n")
    print("Сила:", characteristics['Сила'], "Здоровье:", characteristics['Здоровье'], "Мудрость", characteristics['Мудрость'], "Ловкость", characteristics['Ловкость'], "\n")
    print("Введите 'конец' для выхода")