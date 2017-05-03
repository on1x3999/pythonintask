# Задача 8.
# Анаграмма

# Lukyanov E.A.
# 04.04.2017

import random
WORDS=("Спартак","Бизнес-информатика","Лукьянов","Елизар","Барселона","молоко","кот", "квадрат", "гипертим", "колесо", "оборот" )
word=random.choice(WORDS)
correct=word
jumble=""
finish=len(word)
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("Добро пожаловать в игру 'Анаграммы'!",
      "\nПереставьте буквы так, чтобы получилось слово.")
print("Вот анаграмма: ", jumble)
guess = input("\nА ну-ка отгадайте исходное слово: ")
y=10
x= ""

while y>0:
	if guess.lower() == correct:
		print("Красава!")
		break
	else:
		print("Ошибочка вышла!")
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
			guess = input("А ну-ка отгадайте исходное слово: ")
		if guess != correct:
			y=0
		break

print("Количество очков: ", y)
print("Спасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")