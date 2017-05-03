# Задача 9.

# Епишина Ю.А.
# 11.04.2017

import random
WORDS=("борщ","чебурек","пирог","пельмени","блины","салат","суп","суши","роллы","вареники")

HANGMAN =("Умничка", "Не очень умничка", "Дурачок", "Вообще плохо", "хуже некуда")
МAX_WRONG =len(HANGMAN)-1 
word = random.choice(WORDS) 
so_far = "-" * len(word)
wrong = 0
used = [] 
userword = ''
guess = ''

mode = input('Выводить подсказки? (д/н): ')
if (mode.lower() == 'д') :
	print(WORDS, word, wrong, МAX_WRONG, used, guess)


print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")
while wrong < МAX_WRONG and so_far != word and userword != word:
	
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

	ans = 'н'
	if wrong < МAX_WRONG :
		ans = input('\n\nГотов назвать слово? (д/н): ')
	else :
		userword = input('\n\nВведите свой вариант слова: ')
	
	if (ans.lower() == 'д' ) :
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