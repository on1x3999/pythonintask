#Задача 6. Вариант 17.
#Создайте игру, в которой компьютер загадывает название	одного из пяти космических челноков	проекта	Спейс шаттл,	
#а игрок должен его угадать. 

#Kurkin M. I.
#20.04.2017

import random

print("\aНачнём Игру.\n Я загадываю один из шатлов 'Спейс Шаттла', а ты его отгадываешь.")

print("Вот их список:")

k="Колумбия"

c="Челленджер"

d="Дискавери"

a="Атлантис"

ee="Индевор"

print("\n",k,'\n',c,'\n',d,'\n',a,'\n',ee)

rand=random.randint(0,5)

if rand==0:

	otvet=k

	podskazka="Он мёртв"

elif rand==1:

	otvet=c

	podskazka="Одноимённый корабль исследовал океан в XIX веке"

elif rand==2:

	otvet=d

	podskazka="Он прослужил столько же лет, сколько нужно укланяться от армии"

elif rand==3:

	otvet=a

	podskazka="Брат промитея"

elif rand==4:

	otvet=ee

	podskazka="Эдвин Хаббл благодарин этой штуке"

print("Кажется я загадал")

reshenie=1

while reshenie!=otvet:

	reshenie=input("Отвечай\n")

	if reshenie!=otvet:

                print(podskazka)

input("\n\nТы смог, но это было легко.\nНажмите	Enter	для	выхода.")