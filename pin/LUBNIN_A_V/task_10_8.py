# Задача 10. Вариант 8.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.

# Lubnin A.V.
# 18.04.2017

print (
'''
		Добро пожаловать в программу "Генератор персонажей"!
	Существует 4 характиристики: Сила, Здоровье, Мудрость и Ловкость.
	Вам предоставлено 30 пунктов, которые можете распределить между ними, также Вы можете возвращать их обратно 
	и присвоить их другой характеристике.
		Приятной игры! 
		
			
''')

print("Как зовут вашего героя, попавшего в жестокий мир Врайден?")
player = input("Имя: ")
print("\nИ так, ", player, " после кораблекрушения совсем забыл какие у него были характеристики...")
print(player, ", распредели 30 очков между силой, здоровьем, ловкостью и мудростью.")

Power = 0
Health = 0
Mana = 0
Stamina = 0
choice = None
while choice != "0":
    freePoints = (30 - Power - Health - Mana - Stamina)
    print(
    """
	-----------------------------------
    Меню:
    0 - Завершить распределение (в т.ч. если остались свободные очки)
    1 - Добавить очки
    2 - Посмотреть уже присвоенные очки
    3 - удалить очки
	-----------------------------------
    """
    )
    choice = input("Ваш выбор: ")

# Блок выхода
    if choice == "0":
        print("Прощай ",player)


# Блок распределения
    elif choice == "1":
        print("Вам доступно ", freePoints, " свободных очков для распределения")
        print("1 - Сила")
        print("2 - Здоровье")
        print("3 - Мудрость")
        print("4 - Ловкость")
        tempInput  = (input("Введите номер характеристики в которую хотите добавить очки - "))
        if  tempInput  == "1":
            tempInput  = int(input("Сколько очков вы хотите добавить в Силу?"))
            if tempInput  >= 0 and tempInput  <= freePoints:
                Power += tempInput 
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif  tempInput  == "2":
            tempInput  = int(input("Сколько очков вы хотите добавить в Здоровье?"))
            if tempInput  >= 0 and tempInput  <= freePoints:
                Health += tempInput 
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif  tempInput  == "3":
            tempInput  = int(input("Сколько очков вы хотите добавить в Мудрость?"))
            if tempInput  >= 0 and tempInput  <= freePoints:
                Mana += tempInput 
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif  tempInput  == "4":
            tempInput  = int(input("Сколько очков вы хотите добавить в Ловкость?"))
            if tempInput  >= 0 and tempInput  <= freePoints:
                Stamina += tempInput 
            else:
                print("Вы ввели недопустимое кол-во очков")


# Блок предпросмотра
    elif choice == "2":
        print("Ваши характеристики:")
        print("Сила - ", Power)
        print("Здоровье - ", Health)
        print("Мудрость - ", Mana)
        print("Ловкость - ", Stamina)
        print("\nУ вас еще есть - ", freePoints, "очков")

# Блок отката очков
    elif choice == "3":
        print("Удаление результатов")
        print("1 - Сила")
        print("2 - Здоровье")
        print("3 - Мудрость")
        print("4 - Ловкость")
        tempInput = (input("Введите номер характеристики которую в которой хотите удалить очки - "))
        if tempInput == "1":
            tempInput = int(input("Сколько очков вы хотите удалить в Силе - "))
            if tempInput <= Power and tempInput > 0:
                Power -= tempInput
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif tempInput == "2":
            tempInput = int(input("Сколько очков вы хотите удвлить в Здоровье - "))
            if tempInput <= Health and tempInput > 0:
                Health -= tempInput
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif tempInput == "3":
            tempInput = int(input("Сколько очков вы хотите удалить в Мудрости - "))
            if tempInput <= Stamina and tempInput > 0:
                Mana -= tempInput
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif tempInput == "4":
            tempInput = int(input("Сколько очков вы хотите удалить в Ловкости - "))
            if tempInput <= Stamina and tempInput > 0:
                Stamina -= tempInput
            else:
                print("Вы ввели недопустимое кол-во очков")
        else:
            print("В меню нет пункта", tempInput)
    else:
        print("Извините, в меню нет пункта", choice)
		
# Блок завершения.
print(player, " наделен следующими атрибутами:")
print("Сила - ", Power)
print("Здоровье - ", Health)
print("Мудрость - ", Mana)
print("Ловкость - ", Stamina)
print("Выходя из пещеры вы заметели медведя. Неловкое движение и вас заметили. Пару мгновений и медведь убивает", player)
input("Нажмите Enter для выхода")