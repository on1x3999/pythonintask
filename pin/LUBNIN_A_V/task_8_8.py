# Задача 8. Вариант 8.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
#так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
#подсказку в том случае, если у него нет никаких предположений. Разработайте
#систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
#получали больше тех, кто запросил подсказку.


# Lubnin A.V.
# 17.04.2017

import random
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble =""

while word:  
	position = random.randrange(len(word))
	jumble += word[position] 
	word = word[:position] + word[(position + 1):]	
score = len(correct)
# начало игры
print ("""
	Добро пожаловать в игру 'Анаграммы'!
	Надо переставить буквы так. чтобы получилось осмысленное слово.
	""")
answer = "Zz"
print("Boт анаграмма:", jumble) 	
while answer != correct:
	answer = str(input("Ваш вариант или 'Y' для открытия позиции случайной буквы: "))
	if ((answer.lower == str("Y").lower) and (score > 0)):
		i = random.randint(1, len(correct))
		print("Вы использовали подсказку ", i, "буква: ", correct[i])
		score-=1
	elif (answer.upper == correct.upper):
		print("Верный ответ, вы получаете ", score, " очков")
print("Игра закончена, ваш итоговый счёт ", score, " очков. Нажмите Enter чтобы выйти.")	
input()
