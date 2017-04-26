# Задача 8. Вариант 11.
# 1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Ovinnikova T.A.
# 18.04.2017

import random

print ("Добро пожаловать в игру 'Анаграммы'!")
print ("Составьте слово из предложенных букв и попробуйте победить!")

def help_func(a):
	if a=='борода':
		print('Поросль на лице')
	if a=='рама':
		print('Она украшает картину')
	if a=='собака':
		print('Домашнее животное')
	if a=='рождение':
		print('Появление на свет')
	if a=='молитва':
		print('Обращение к Богу')
	if a=='говор':
		print('Особенность речи в провинции')
	if a=='браконьерство':
		print('Охота в заповеднике')
		
point=0;
allpoint=0;
k=0;
n=0;
flag1=True;
flag2=False
def point_func(b):
	global k
	global allpoint
	global point
	global n
	if b==1:
		k=50
	if b==0:
		n+=1
		allpoint=100-k
		point+=allpoint
		k=0
		print('У вас ',allpoint,'очков')
		print('Всего ',point, 'очков')
		
while 0!=1:
	WORDS = ("борода", "рама", "собака", "рождение", "молитва", "говор", "браконьерство")
	word = random.choice(WORDS)
	correct = word
	jumble =""
	while word:
		position = random.randrange(len(word))
		jumble += word[position]
		word = word[:position] + word[(position + 1):]
	print("Загаданное слово:", jumble,'.\nЕсли не получается, введите "help"')
	guess = input("\nВаш ответ: ")
	while 0!=1:	
		while guess == "help":
			help_func(correct)
			point_func(1)
			guess = input("\nВаш вариант: ")
		while guess != correct and guess != "help":
			print("Ответ \"", guess, "\" не верен")
			print("\nЗагаданное слово:", jumble,'.\nВведите "help" для получения подсказки')
			guess = input("\nВаш вариант: ")
		if guess == correct:
			point_func(0)
			print("Правильно!!!!!")
			print("Так держать!;)")
			g=input('Сыграть ещё? да / нет\n')
			while 1!=0:
				if g=='да':
					break
				elif g=='нет':
					flag2=True
					print('Возвращайся позже, сыграем ещё!;)')
					if (5<=n<=20 or 5<=n%10<=10):
						otv='ответов'
					elif 2<=n%10<=4:
						otv='ответа'
					elif n%10==1:
						otv='ответ'
					print('За',n,'правильных',otv,'вы набрали',point,'очков')
					input()
					break
				else:
					g=input('Сыграть ещё? да/нет\n')
					continue
		if flag1:
			break
	if flag2:
		break



input("\n\nНажмите Enter для выхода.")
