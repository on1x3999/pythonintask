# Задание 10. Вариант 10.
# Mongush D.S.

# 05.04.17

point = ""
vvod = None
count = 0
mount = 0
start = [point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point]
wisdom = []
agility = []
strength = []
health = []

while vvod != "0":
    print("""
Здравствуй! Выбери пункт меню
0. Выход
1. Добавить очки из общего пула.
2. Вернуть очки в общий пул.
        """)


    vvod = input("Выберите пункт меню: ")

    if vvod == "1" :
        print("\nВам доступно", len(start), "очков")
        print("""
1. wisdom
2. agility
3. strength
4. health
""")
        quest = input("Какую характеристику вы хотите повысить? ")
        diff = int(input("На какое количество очков? "))

        if quest == "1":
            while count < diff:
                del start[0]
                wisdom.append(point)
                count += 1
        if quest == "2":
            while count < diff:
                del start[0]
                agility.append(point)
                count += 1
        if quest == "3":
            while count < diff:
                del start[0]
                strength.append(point)
                count += 1
        if quest == "4":
            while count < diff:
                del start[0]
                health.append(point)
                count += 1
        count = 0
    if vvod == "2" :
        print("""
1. wisdom
2. agility
3. strength
4. health
""")
        quest = input("\nОткуда вы желаете убрать очки? ")

        if quest == "1":
            diff = int(input("Имеется", len(wisdom), "очков. Введите количество очков: "))
            while mount < diff:
                del wisdom[0]
                start.append(point)
                mount += 1
        if quest == "2":
            diff = int(input("Имеется", len(wisdom), "очков. Введите количество очков: "))
            while mount < diff:
                del agility[0]
                start.append(point)
                mount += 1
        if quest == "3":
            diff = int(input("Имеется", len(wisdom), "очков. Введите количество очков: "))
            while mount < diff:
                del strength[0]
                start.append(point)
                mount += 1
        if quest == "4":
            diff = int(input("Имеется", len(wisdom), "очков. Введите количество очков: "))
            while mount < diff:
                del heath[0]
                start.append(point)
                mount += 1
        mount = 0
    

    input("\n\nГотово! Нажмите Enter, чтобы продолжить")
    
