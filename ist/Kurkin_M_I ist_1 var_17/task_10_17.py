#Задача 9. Вариант 17.
#Напишите	программу,	которая	будет	сообщать	род	деятельности	и	псевдоним	под которым	скрывается	Алексей	Максимович	Пешков.	
#После	вывода	информации программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для	выхода.

#Kurkin M. I.
#20.04.2017
Characteristics = [["Сила",0],["Здоровье",0],["Мудрость",0],["Ловкость",0]]

point_bank=30

a='0'

def parameter_changer(a,b):

	global point_bank

	global Characteristics

	if b<=point_bank:

		point_bank-=b

		Characteristics[a][1]+=b

	else:

		print("НЕВЕРОЯТНОЕ ЗНАЧЕНИЕ!!!11!11!11\nНичего не изменилось\n\n")

def info_hero():

	for i in range(4):

		print("Параметр",(i+1), Characteristics[i][0], "равен", Characteristics[i][1])

	print ("В запасе",point_bank,"очков\n")

print('\n\n\n\n|Вас приветствует программа "редактор персонажей для самой лучшей игры 2", вжух|\n\n')

info_hero()

print("Для выхода несколько раз нажмите ввод.")

input('Нажмите enter, чтобы начать редактирование')

stop='010101'

while stop!='':

	while a!="" or point_bank!=0:

		a=(int(input("Выберите параметр для изменения\t")))-1

		if a in range(1,5):

			print("На сколько изменяем",Characteristics[a][0],"?", end="\t")

			b=int(input())

			parameter_changer(a,b)

		else:

			print("\nХочешь вызвать ошибку? Попробуй что-нибудь ещё.\n")

		info_hero()

	stop=input("Для завершения нажмите enter, иначе ввидите текст")

if point_bank==0:

	print("Вы потратили все свои очки улучшения, но какой выдающийся у вас герой вышел")

	info_hero()

input("Конец работы. Нажмите ENTER")