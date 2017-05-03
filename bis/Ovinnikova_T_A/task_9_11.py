# Задача 9. Вариант 11.
# 1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
# Вслед за тем игрок должен попробовать отгадать слово.

# Ovinnikova T.A.
# 18.04.2017

import random

name=input("Как тебя зовут?")
print("Добро пожаловать в игру, ", name, "!")
print("Составляй из букв слова и попробуй победить!")
allpoint=0;point=0;k=0;n=0;flag=True;pos=0
def och_func(b):
	global k
	global point
	global allpoint
	global n
	if b==1:
		k=50
	if b==0:
		n+=1
		point=100-k
		allpoint+=point
		k=0
		print('У вас ',point,'очков')
		print('Всего ',allpoint, 'очков')		
		
while flag:
	WORDS = ["борода", "рама", "собака", "рождение", "молитва", "говор", "браконьерство"]
	word = random.choice(WORDS)
	correct=word
	print('В слове ',len(word),'букв')
	print('Сможешь за 5 попыток отгадать все буквы в этом слове?\n')
	while pos!=5:
		i=input()
		if i in list(word):
			print('Молодец ',i,':)\nОсталось',4-pos,'попыток')
		else:
			print('Такой буквы нет :( У тебя ещё',4-pos,'попыток')
		pos+=1
	pos=0
	if correct==input('Попробуй назвать всё слово!\n'):
		g=input('Ура!\n\n Попробовать ещё? да/нет\n')
	else:
		g=input('Увы, но неверно.\n\n Загадать ещё слово? да/нет\n')
	while flag:
                if g=='да':
			break
		elif g=='нет':
			print('Спасибо за игру, ', name, '!')
			flag=False
			input()
		else:
			g=input('Сыграть ещё? да/нет\n')
			continue

input("\n\nНажмите Enter для выхода.")
