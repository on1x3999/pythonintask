# Задача 10. Вариант 11.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно
# быть предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
# туда из характеристик, которым он решил присвоить другие значения.

# Zaytsev N.S. 
# 19.04.2017

print( 
"""
\tДобро пожаловать в игру "Генератор персонажей!"
				  
\t\t\tП Р А В И Л А
\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
\tТебе даётся 30 очков, которые нужно распределить
\tмежду параметрами: "здоровье", "сила", "мудрость", "ловкость". 
\tТы можешь изменять (добавлять\убавлять очки) параметры.
\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
\t\tДавай создадим супер-героя!
"""
)

name=input("Выбери имя своему герою: ")
attributes=("здоровье", "сила", "мудрость", "ловкость")
points=30
health=0
strength=0
wisdom=0
dexterity=0
while True:
    print ("Сейчас у тебя осталось", points, "очков.")
    print (
    """
    1-Добавить очки
    2-Убрать очки
    3-Просмотреть характеристики
    4-Выход
    """
	)
    choice=input("Выбери: ")
    if choice=="1":
        attribute=input("Какую характеристику изменить? Сила, здоровье, мудрость или ловкость? ")
        if attribute in attributes:
            add=int(input("Сколько очков добавить? "))
            if add<=points and add>0:
                if attribute=="сила":
                    strength+=add
                    print (name, "имеет сейчас", strength, "очков силы.")
                elif attribute=="здоровье":
                    health+=add
                    print (name, "имеет сейчас", health, "очков здоровья.")
                elif attribute=="мудрость":
                    wisdom+=add
                    print (name, "имеет сейчас", wisdom, "очков мудрости.")
                elif attribute=="ловкость":
                    dexterity+=add
                    print (name, "имеет сейчас", dexterity, "очков ловкости.")
                points-=add
            else:
                print ("Неверное значение!")
        else:
            print ("Неверное значение!")
    elif choice=="2":
        attribute=input("Какую характеристику изменить? Сила, здоровье, мудрость или ловкость? ")
        if attribute in attributes:
            take=int(input("Сколько очков убрать? "))
            if attribute=="сила" and take<=strength and take>0:
                strength-=take
                print (name, "имеет сейчас", strength, "очков силы.")
                points+=take
            elif attribute=="здоровье" and take<=health and take>0:
                health-=take
                print (name, "имеет сейчас", health, "очков здоровья.")
                points+=take
            elif attribute=="мудрость" and take<=wisdom and take>0:
                wisdom-=take
                print (name, "имеет сейчас", wisdom, "очков мудрости.")
                points+=take
            elif attribute=="ловкость" and take<=dexterity and take>0:
                dexterity-=take
                print (name, "имеет сейчас", dexterity, "очков ловкости.")
                points+=take
            else:
                print ("Неверное значение!")
        else:
            print ("Неверное значение!")
    elif choice=="3":
        print ("Сила -", strength)
        print ("Здоровье -", health)
        print ("Мудрость -", wisdom)
        print ("Ловкость -", dexterity)
    elif choice=="4":
        if points==0:
            break
        else:
            print ("Используй все очки!")
    else:
        print ("Неверное значение!")
print ("Поздравляю! Ты создал: "+name+'.')
print (name, "имеет", strength, "очков силы,", health, "очков здоровья,", wisdom, "очков мудрости и", dexterity, "очков ловкости.")
input ('\nPress enter to exit from program...')