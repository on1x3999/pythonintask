# Задача 8, вариант 7

# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на языке Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Иливанова Н.Д.
# 20.04.2017

import random
WORDS=("понедельник","вторник","среда","четверг","пятница","суббота","воскресенье")
word=random.choice(WORDS)
correct=word
days=""
finish=len(word)
while word:
    position=random.randrange(len(word))
    days+=word[position]
    word=word[:position]+word[(position+1):]
print("Добро пожаловать в игру 'Анаграммы'!",
      "\nНадо пререставить буквы так, чтобы получилось слово.")
print("Вот анаграмма: ", days)
guess = input("\nПопробуйте отгадать исходное слово: ")
y=10
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
