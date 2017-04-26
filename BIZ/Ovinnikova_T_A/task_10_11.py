# Задача 10. Вариант 11.
# Напишите программу "Генератор персонажей" для игры. 
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость.
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Ovinnikova T.A.
# 18.04.2017


print("Добро пожаловать в игру!")
print("Вам необходимо распределить 30 очков на четыре различные характеристики. Вперёд!")
point=30; sila=0; zdor=0; mudr=0; lovk=0; s='';z='';m='';l=''
st='\n\t\t\t\t\t\t\t\t\t\t\t'
flag=True;
otv='да'
def stat_func():
        print (st,'Сила:    ',sila,st,'Здоровье:',zdor,st,'Мудрость:',mudr,st,'Ловкость:',lovk,'\n',st,'Осталось:',point)
def sila_func(s):
	global sila,point,flags
	if s>point:
		print('Не хватает очков')
	elif sila+s<0:
		print('Не хватает силы')
	else:
		flags=False
		point-=s
		sila+=s
	stat_func()
def zdor_func(z):
	global zdor,point,flagz
	if z>point:
		print('Не хватает очков')
	elif zdor+z<0:
		print('Не хватает здоровья')
		
	else:
		flagz=False
		point-=z
		zdor+=z	
	stat_func()
def mudr_func(m):
	global mudr,point,flagm
	if m>point:
		print('Не хватает очков')
	elif mudr+m<0:
		print('Не хватает мудрости')
	else:
		flagm=False
		point-=m
		mudr+=m	
	stat_func()
def lovk_func(l):
	global lovk,point,flagl
	if l>point:
		print('Не хватает очков')
	elif lovk+l<0:
		print('Не хватает ловкости')
	else:
		flagl=False
		point-=l
		lovk+=l
	stat_func()
flagotv=False
stat_func()	
while otv=='да':
	while otv=='да':
		flags=flagz=flagm=flagl=True
		while flags:
			while True:
				s=input('Сила:  ')
				try:
					s=int(s)
					break
				except ValueError:
					print('Введите ваше число')
			sila_func(s)
		if point==0 and flagotv!=True:
			break
		while flagz:
			while True:
				z=input('Здоровье:  ')
				try:
					z=int(z)
					break
				except ValueError:
					print('Введите ваше число')
			zdor_func(z)
		if point==0 and flagotv!=True:
			break
		while flagm:
			while True:
				m=input('Мудрость:  ')
				try:
					m=int(m)
					break
				except ValueError:
					print('Введите ваше число')
			mudr_func(m)
		if point==0 and flagotv!=True:
			break
		while flagl:
			while True:
				l=input('Ловкость:  ')
				try:
					l=int(l)
					break
				except ValueError:
					print('Введите ваше число')
			lovk_func(l)
		if point==0:
			break
		if point!=0:
			while True:
				otv=input('У вас ещё остались очки. Распределите? да/нет\n')
				if otv=='нет':
					break
				elif otv=='да':
					flagotv=True
					stat_func()
					break
				else:
					continue
	if point==0:
		while True:
			otv=input('Все очки распределены. Хотите перераспределить? да/нет\n')
			if otv=='нет':
				break
			elif otv=='да':
				flagotv=True
				while True:
					otv2=input('Сбросить распределение очков? да/нет\n')
					if otv2=='нет':
						print('Значения можно вычитать с помощью знака "-" перед вводимым числом')
						stat_func()	
						break	
					elif otv2=='да':
						point=30
						sila=0
						zdor=0
						mudr=0
						lovk=0
						stat_func()	
						break
					else:
						continue	
				break
			else:
				continue
print('Распределение очков по характеристикам завершено.\n')
input("\n\nНажмите Enter для выхода.")
