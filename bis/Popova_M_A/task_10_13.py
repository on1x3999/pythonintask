# Задача 10. Вариант 13.
# Напишите программу "Генератор персонажей" для игры. 
# Пользователю должно быть предоставлено 30 пунктов,
# которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,
# чтобы пользователь мог не только брать эти пункты из общего "пула",
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
# Попова М. А.
# 16.04.2017

print(
"""
Распредели данные тебе очки характеристик как ты пожелаешь.
Всего будет доступно 30 очков характеристик (далее ОХ), которые тебе предстоит распределить.
"""
)
oh=30
os=0
oz=0
om=0
ol=0
s='';z='';m='';l=''
st='\n\t\t\t\t\t\t\t\t\t\t\t'
flag=True
otv='да'
def stat_func():
	print (st,'Сила:    ',os,st,'Здоровье:',oz,st,'Мудрость:',om,st,'Ловкость:',ol,'\n',st,'Свободно:',oh)
def sila_func(s):
	global os,oh,flags
	if s>oh:
		print('У вас недостаточно ОХ')
	elif os+s<0:
		print('У вас недостаточно силы')
	else:
		flags=False
		oh-=s
		os+=s
	stat_func()
def zdor_func(z):
	global oz,oh,flagz
	if z>oh:
		print('У вас недостаточно ОХ')
	elif oz+z<0:
		print('У вас недостаточно здоровья')
		
	else:
		flagz=False
		oh-=z
		oz+=z	
	stat_func()
def mudr_func(m):
	global om,oh,flagm
	if m>oh:
		print('У вас недостаточно ОХ')
	elif om+m<0:
		print('У вас недостаточно мудрости')
	else:
		flagm=False
		oh-=m
		om+=m	
	stat_func()
def lovk_func(l):
	global ol,oh,flagl
	if l>oh:
		print('У вас недостаточно ОХ')
	elif ol+l<0:
		print('У вас недостаточно ловкости')
	else:
		flagl=False
		oh-=l
		ol+=l
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
					print('Введите число')
			sila_func(s)
		if oh==0 and flagotv!=True:
			break
		while flagz:
			while True:
				z=input('Здоровье:  ')
				try:
					z=int(z)
					break
				except ValueError:
					print('Введите число')
			zdor_func(z)
		if oh==0 and flagotv!=True:
			break
		while flagm:
			while True:
				m=input('Мудрость:  ')
				try:
					m=int(m)
					break
				except ValueError:
					print('Введите число')
			mudr_func(m)
		if oh==0 and flagotv!=True:
			break
		while flagl:
			while True:
				l=input('Ловкость:  ')
				try:
					l=int(l)
					break
				except ValueError:
					print('Введите число')
			lovk_func(l)
		if oh==0:
			break
		if oh!=0:
			while True:
				otv=input('У вас остались нераспределенные ОХ. Хотите их дораспределить? да/нет\n')
				if otv=='нет':
					break
				elif otv=='да':
					flagotv=True
					stat_func()
					break
				else:
					continue
	if oh==0:
		while True:
			otv=input('Вы распределили все ОХ. Хотите их перераспределить? да/нет\n')
			if otv=='нет':
				break
			elif otv=='да':
				flagotv=True
				while True:
					otv2=input('Сбросить все значения? да/нет\n')
					if otv2=='нет':
						print('Из вложенных характеристик можно вычитать нужные значения путем приставки "-"')
						stat_func()	
						break	
					elif otv2=='да':
						oh=30
						os=0
						oz=0
						om=0
						ol=0
						stat_func()	
						break
					else:
						continue	
				break
			else:
				continue
print('И так...\n')
input('Вы закончили распределение ОХ.')
