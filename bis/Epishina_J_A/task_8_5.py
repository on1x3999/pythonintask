# Задача 8
# Аннаграмма

# Епишина Ю.А.
# 29.03.17

import random
WORDS=("борщ","чебурек","пирог","пельмени","блины","салат","суп","суши","роллы","вареники")
word=random.choice(WORDS)
correct=word
jumble =""
finish=len(word)
while word:
	position=random.randrange(len(word))
	jumble+= word[position]
	word = word[:position] + word[(position +1):]
print(
"""
      Добро пожаловать в игру 'Анаграммы'!
	  Надо переставить буквы так, чтобы получилось осмысленное слово.
	 (Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print("Вот анаграмма:", jumble)
guess = input ("\nПопробуйте отгадать исходное слово: ")
y=100
x= ""

while y>0:
	if guess.lower() == correct:
		print("Вы отгадали!")
		break
	else:
		print("К сожалению вы ошиблись!")
		for letter in correct:
			x += letter
			if guess == correct:
				break
			print("Подсказка: ", x)
			y=y-1
			if y==0:
				break
			start = 0
			if x == correct[start:finish]:
				break
			guess = input("Попробуйте отгадать исходное слово: ")
		if guess != correct:
			y=0
		break

print("Количество очков: ", y)
print("Спасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")