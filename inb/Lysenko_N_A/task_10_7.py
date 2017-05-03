# Задача 10. Вариант 7.
# Напишите программу "Генератор персонажей" для игры. 
# Пользователю должно быть предоставлено 30 пунктов,
# которые можно распределить между четырьмя характеристиками: 
# Сила, Здоровье, Мудрость и Ловкость. 
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", 
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Lysenko N.A.
# 02.04.2017

print(
"""
			Добро пожаловать в 'Генератор персонажей'!
	Здесь Вы можете создать своих персонажей со своими характеристиками.
		Всего на каждого персонажа отводится 30 пунктов.
			Пункты могут быть распределены между: 
		   Силой, Здоровьем, Мудростью, Ловкостью.                         
"""
)
#Нулевой герой
characters = {'widetrace': ['widetrace', 0, 0, 0, 0]}
#Простое меню
choice = None
while choice != 0:
	print(
	"""
	Нажмите 0, чтобы выйти.
	Нажмите 1, чтобы добавить персонажа.
	Нажмите 2, чтобы редактировать персонажа.
	Нажмите 3, чтобы просмотреть имеющихся персонажей.
	Нажмите 4, чтобы удалить персонажа.
	"""
		)
	choice = int(input("Что вы хотите сделать: "))
	if choice == 0:
		print("До скорых встреч!")
#Нажали 1
	elif choice == 1:
		name = input("Как Вы назовете нового персонажа: ")
		n = name
		if name not in characters:
			characters[name] = [n, "strength", "health", "intellect", "agility"]
			points = 30
			characters[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > 30:
				s = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][1] = s
			points = points - s
			h = int(input("\nЗначение Здоровья: "))
			while h < 0 or h > points:
				h = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][2] = h
			points = points - h
			i = int(input("\nЗначение Мудрости: "))
			while i < 0 or i > points:
				i = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][3] = i
			points = points - i
			a = int(input("\nЗначение Ловкости: "))
			while a < 0 or a > points:
				a = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][4] = a
			points = points - a
			print("\nПерсонаж добавлен.")
		else:
			print("\nТакое имя уже существует.")
#Нажали 2
	elif choice == 2:
		name = input("Введите имя персонажа: ")
		n = name
		if name in characters:
			characters[name] = [n, "strength", "health", "intellect", "agility"]
			points = 30
			characters[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > 30:
				s = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][1] = s
			points = points - s
			h = int(input("\nЗначение Здоровья: "))
			while h < 0 or h > points:
				h = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][2] = h
			points = points - h
			i = int(input("\nЗначение Мудрости: "))
			while i < 0 or i > points:
				i = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][3] = i
			points = points - i
			a = int(input("\nЗначение Ловкости: "))
			while a < 0 or a > points:
				a = int(input("Такого значения не существует. Введите правильное значение:"))
			characters[name][4] = a
			points = points - a
			print("\nПерсонаж", name, "изменен.")
		else:
			print("\nТакого персонажа не существует.")
#Нажали 3
	elif choice == 3:
		print("Ваши персонажи:")
		for name in characters:
			specials = characters[name]
			print(specials)
#Нажали 4
	elif choice == 4:
		name = input("Какого персонажа Вы хотите удалить? ")
		if name in characters:
			del characters[name]
			print("\nПерсонаж удален.")
		else:
			print("\nТакого персонажа не существует.")
	else:
		print ("\nТакого пункта не существует.")
input("\n\nНажмите Enter, чтобы выйти.")