#Задача 10. Вариант 4

#1-50. Напишите программу "Генератор персонажей" для игры.
#Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость.
#Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

#Григорьева Яна.В.
#19.04.17
y=25;
health=0
strength=0
wisdom=0
agility=0
sravn=""


print("\nПривет! Вам доступно очков: ", y, "\nРаспределите их по своим умениям.")
print ("\n\nВаши умения: здоровье - ", health, "сила - ", strength, "мудрость - ", wisdom, "ловкость - ", agility)






while y>0:
	guess = input("Выберите навык: ")
	if guess == "сила":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			strength=strength+10
			print ("Ваша сила равна", strength)
			y=y-1
		else: 
			strength=strength-10
			print ("Ваша сила равна", strength)
			y=y+1
	if guess == "здоровье":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			health=health+10
			print ("Ваше здоровье равно:", health)
			y=y-1
		else: 
			health=health-10
			print ("Ваше здоровье равно:", health)
			y=y+1
	if guess == "мудрость":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			wisdom=wisdom+10
			print ("Ваша мудрость равна:", wisdom)
			y=y-1
		else: 
			wisdom=wisdom-10
			print ("Ваша мудрость равна:", wisdom)
			y=y+1
	if guess == "ловкость":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			agility=agility+1
			print ("Ваша ловкость равна:", agility)
			y=y-10
		else: 
			agility=agility-1
			print ("Ваше ловкость равна:", agility)
			y=y+10
	print("У вас осталось очков: ", y)
	print ("\n\nВаши навыки: здоровье - ", health, "сила - ", strength, "мудрость - ", wisdom, "ловкость - ", agility)
print ("Навыки успешно распределены.")
input("\n\nHaжмитe Enter. чтобы выйти.") 
