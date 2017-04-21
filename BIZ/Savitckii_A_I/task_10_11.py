# Задача 10.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения

#Savitckii A I
#14.04.2017
y=5;
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
			strength=strength+1
			print ("Ваша сила равна", strength)
			y=y-1
		else: 
			strength=strength-1
			print ("Ваша сила равна", strength)
			y=y+1
	if guess == "здоровье":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			health=health+1
			print ("Ваше здоровье равно:", health)
			y=y-1
		else: 
			health=health-1
			print ("Ваше здоровье равно:", health)
			y=y+1
	if guess == "мудрость":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			wisdom=wisdom+1
			print ("Ваша мудрость равна:", wisdom)
			y=y-1
		else: 
			wisdom=wisdom-1
			print ("Ваша мудрость равна:", wisdom)
			y=y+1
	if guess == "ловкость":
		sravn = input ("Отнимите или прибавьте очки (+/-)")
		if sravn == "+":
			agility=agility+1
			print ("Ваша ловкость равна:", agility)
			y=y-1
		else: 
			agility=agility-1
			print ("Ваше ловкость равна:", agility)
			y=y+1
	print("У вас осталось очков: ", y)
	print ("\n\nВаши навыки: здоровье - ", health, "сила - ", strength, "мудрость - ", wisdom, "ловкость - ", agility)
print ("Навыки успешно распределены.")
input("\n\nHaжмитe Enter. чтобы выйти.") 