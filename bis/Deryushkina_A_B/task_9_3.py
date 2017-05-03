#Задача 9. Вариант 3.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.
#Deryushkina A.B.
#29.03.2017

import random
WORDS=("университет", "студент", "учебник", "программирование", "буфет", "весна", "компьютер", "любовь", "проектор")

totals=("Молодец!", "Хорошая работа", "Ну, пойдёт", "Не очень то и быстро", "Хуже некуда")
max_wrong =len(totals)-1 
word = random.choice(WORDS) 
so_far = "-" * len(word)
wrong = 0
used = [] 
userword = ''
guess = ''

mode = input('Выводить подсказки? (да/нет): ')
if (mode.lower() == 'да') :
	print(WORDS, word, wrong, max_wrong, used, guess)


print("Дoбpo пожаловать в игру 'Виселица'. Удачи!")
while wrong < max_wrong and so_far != word and userword != word:
	
	guess = input("\n\nВведите букву: ")
	guess = guess.lower()
	while guess in used: 
		print("Bы уже предлагали букву", guess)
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
		print("\nK сожалению. буквы", guess, "нет в слове.")

	print("\nBы уже предлагали следующие буквы:\n", used) 
	print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far) 

	answer = 'нет'
	if wrong < max_wrong :
		answer = input('\n\nГотов назвать слово? (да/нет): ')
	else :
		userword = input('\n\nВведите свой вариант слова: ')
	
	if (answer.lower() == 'да' ) :
		userword = input('\n\nВведите свой вариант слова: ')
	
	if (userword == word) :
		break
	wrong += 1 
if wrong == max_wrong:
	print(totals[wrong])
	print("\nBac повесили!")
else: 
	print("\nBы отгадали!")

print('\n\n\n',totals[wrong]) 

print("\nБылo загадано слово", word) 
input("\n\nHaжмитe Enter. чтобы выйти.") 