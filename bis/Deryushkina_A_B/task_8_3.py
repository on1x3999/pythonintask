#Задача 8. Вариант 3.
#Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#Deryushkina A.B.
#29.03.2017

import random
слова=("привет", "студент", "учебник", "программирование", "буфет", "весна", "компьютер", "любовь", "проектор")
word=random.choice(слова)
correct=word
jumble=""
finish=len(word)
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("Добро пожаловать в игру - Анаграммы!",
      "\nНадо пререставить буквы так, чтобы получилось слово.")
print("Вот анаграмма: ", jumble)
guess = input("\nПопробуйте отгадать загаданное слово: ")
y=100
x= ""

while y>0:
	if guess.lower() == correct:
		print("Вы угадали!")
		break
	else:
		print("Увы, вы ошиблись!")
		for letter in correct:
			x += letter
			if guess == correct:
				break
			print("Подсказка: ", x)
			y=y-10
			if y==0:
				break
			start = 0
			if x == correct[start:finish]:
				break
			guess = input("Попробуйте отгадать загаданное слово: ")
		if guess != correct:
			y=0
		break

print("Количество очков: ", y)
print("Спасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")