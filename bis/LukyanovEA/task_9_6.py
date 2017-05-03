# Задача 9.

# Lukyanov E.A.
# 18.04.2017

import random
WORDS=("Спартак","Бизнес-информатика","Лукьянов","Елизар","Барселона","молоко","кот", "квадрат", "гипертим", "колесо", "оборот" )

HANGMAN =("Отлично", "Хорошо", "Плохо", "Очень плохо", "Позор")
МAX_WRONG =len(HANGMAN)-1 
word = random.choice(WORDS) 
so_far = "-" * len(word)
wrong = 0
used = [] 
userword = ''
guess = ''

mode = input('Подсказки нужны? (да/нет): ')
if (mode.lower() == 'да') :
	print(WORDS, word, wrong, МAX_WRONG, used, guess)


print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")
while wrong < МAX_WRONG and so_far != word and userword != word:
	
	guess = input("\n\nВведите букву: ")
	guess = guess.lower()
	while guess in used: 
		print("Bы уже предлагали эту букву", guess)
		guess = input("\n\nBвeдитe букву: ")
		guess = guess.lower()
	used.append(guess) 

	if guess in word: 
		print("\nДa! Буква", guess, "есть в слове!")
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += so_far[i]
		so_far = new 
	else:
		print("\nK сожалению, буквы", guess, "нет в слове.")

	print("\nBы уже предлагали следующие буквы:\n", used) 
	print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far) 

	ans = 'нет'
	if wrong < МAX_WRONG :
		ans = input('\n\nГотовы назвать все слово целиком? (да/нет): ')
	else :
		userword = input('\n\nВведите свой вариант слова: ')
	
	if (ans.lower() == 'да' ) :
		userword = input('\n\nВведите свой вариант слова: ')
	
	if (userword == word) :
		break
	wrong += 1 
if wrong == МAX_WRONG:
	print(HANGMAN[wrong])
	print("\nBac повесили!")
else: 
	print("\nBы отгадали!")

print('\n\n\n',HANGMAN[wrong]) 

print("\nБылo загадано слово", word) 
input("\n\nHaжмитe Enter. чтобы выйти.") 