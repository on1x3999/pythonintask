#Задача 7. Вариант 17.
#Напишите	программу,	которая	будет	сообщать	род	деятельности	и	псевдоним	под которым	скрывается	Алексей	Максимович	Пешков.	
#После	вывода	информации программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для	выхода.

#Kurkin M. I.
#19.04.2017
import random

loop="1"

point=0

while loop:

        wordslist = ("лоно", "прогресс", "разряд", "эпопея", "корпорация", "рефлексия", "протест", "узурпация","диэтиламид",)

        wordslist += ("проекция", "конструктор" , "метрика" , "ортогональность",)

        word = random.choice(wordslist)

        correct = word

        jumble=""

        while word:

        	position=random.randrange(len(word))

        	jumble= jumble + " " + word[position]

        	word=word[:position]+word[(position+1):]

#start

        print('''

	Добро пожаловать в Игру "Анаграммы 1.2"

		Вам нужно составить из букв слово и записать его.

		Вот эти буквы(лишних букв нет и их достаточно):''')

        print(jumble)

        i=0.5

        guess = input("\nПопробуй отгадать слово: ")

        while guess!= correct and guess!="":

        	print("Увы.... нет:'(")

        	

        	if guess != correct:

        		helper = random.randrange((len(correct)-1))

        		print("ПОДСКАЗАКА: буквы номер", helper, '"', correct[(helper-1)], '"' )

        		i+=0.5

        	guess=input("Попробуй снова\n")

        if guess==correct:

                print("Отлично. Вы правы\n")

                print("Вы набрали очки:")

                point=point+1000/i

                print(point)

        print("Спасибо за игру")

        loop = input("Введите любой текст для повтора /n")