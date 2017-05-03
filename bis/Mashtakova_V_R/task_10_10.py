#	Задача 10. Вариант 10.
#       Напишите программу "Генератор персонажей" для игры.
#       Пользователю должно быть предоставлено 30 пунктов, которые можно распределить
#       между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
#	Mashtakova V.R.
#	17.04.2017

point = "sun"
sun = None
count = 0
mount = 0
start = [point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point]
wisdom = []
agility = []
strength = []
health = []

while sun != "0":
    print("""
Здравствуй! Выбери пункт меню
0. Выход
1. Добавить очки из общего пула.
2. Вернуть очки в общий пул.
3. Где и сколько?
        """)


    sun = input("Выбери пункт меню: ")

    if sun == "1" :
        print("\nВам доступно", len(start), "очков")
        print("""
1. wisdom
2. agility
3. strength
4. health
""")
        mek = input("Какую характеристику вы хотите повысить? ")
        fek = int(input("На сколько очков? "))

        if mek == "1":
            while count < fek:
                del start[0]
                wisdom.append(point)
                count += 1
        if mek == "2":
            while count < fek:
                del start[0]
                agility.append(point)
                count += 1
        if mek == "3":
            while count < fek:
                del start[0]
                strength.append(point)
                count += 1
        if mek == "4":
            while count < fek:
                del start[0]
                health.append(point)
                count += 1
        count = 0
    if sun == "2" :
        print("""
1. wisdom
2. agility
3. strength
4. health
""")
        mel = input("\n Откуда? ")

        if mel == "1":
            print("Нет", len(wisdom), "очков.")
            fek = int(input("Сколько? "))
            while mount < fek:
                del wisdom[0]
                start.append(point)
                mount += 1
        if mel == "2":
            print("Нет", len(agility), "очков.")
            fek = int(input("Сколько? "))
            while mount < fek:
                del agility[0]
                start.append(point)
                mount += 1

        if mel == "3":
            print("нет", len(strength), "очков.")
            fek = int(input("Сколько? "))
            while mount < fek:
                del strength[0]
                start.append(point)
                mount += 1
        if mel == "4":
            print("Нет", len(health), "очков.")
            fek = int(input("Сколько? "))
            while mount < fek:
                del heath[0]
                start.append(point)
                mount += 1
        mount = 0
    if sun == "3" :
        print("\nНераспределено:", len(start))
        print("wisdom:", len(wisdom))
        print("agility:", len(agility))
        print("strength:", len(strength))
        print("health:", len(health))
    

    input("\n\nГотово! Нажмите Enter, чтобы продолжить")



