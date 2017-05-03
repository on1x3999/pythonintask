# Задание 10. Вариант 10.
# Rechkalov A.S.

# 29.03.17

point = "kek"
kek = None
count = 0
mount = 0
start = [point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point,point]
wisdom = []
agility = []
strength = []
health = []

while kek != "0":
    print("""

Здравствуй! Выбери пункт меню
0. Выход
1. Добавить очки из общего пула.
2. Вернуть очки в общий пул.
3. Где и сколько?
        """)


    kek = input("Выбери пункт меню: ")

    if kek == "1" :
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
    if kek == "2" :
        print("""
1. wisdom
2. agility
3. strength
4. health
""")
        mek = input("\n Откуда забираем? ")

        if mek == "1":
            print("Ну тут не густо, всего то", len(wisdom), "очков.")
            fek = int(input("Окей, сколько? "))
            while mount < fek:
                del wisdom[0]
                start.append(point)
                mount += 1
        if mek == "2":
            print("Ну тут не густо, всего то", len(agility), "очков.")
            fek = int(input("Окей, сколько? "))
            while mount < fek:
                del agility[0]
                start.append(point)
                mount += 1
        if mek == "3":
            print("Ну тут не густо, всего то", len(strength), "очков.")
            fek = int(input("Окей, сколько? "))
            while mount < fek:
                del strength[0]
                start.append(point)
                mount += 1
        if mek == "4":
            print("Ну тут не густо, всего то", len(health), "очков.")
            fek = int(input("Окей, сколько? "))
            while mount < fek:
                del heath[0]
                start.append(point)
                mount += 1
        mount = 0
    if kek == "3" :
        print("\nНераспределено:", len(start))
        print("wisdom:", len(wisdom))
        print("agility:", len(agility))
        print("strength:", len(strength))
        print("health:", len(health))
    

    input("\n\nГотово! Нажмите Enter, чтобы продолжить")
    
