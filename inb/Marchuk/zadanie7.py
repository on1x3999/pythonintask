#Задача 7. Вариант 12.
#

#Марчук А.Ю.
#09.04.2017


import random
tries = 1
score = 500
print('Программа загадывает название одного из восьми соборов Московского кремля')
churches = random.randint(1,8)
if churches == 1:
	name = 'Колокольня Ивана Великого'
elif churches == 2:
	name = 'Успенский собор'
elif churches == 3:
	name = 'Благовещенский собор'
elif churches == 4:
	name = 'Архангельский собор'
elif churches == 5:
	name = 'Храм Положения ризы божией Матери во Влахерне'
elif churches == 6:
	name = 'Патриарший дворец и собор Двенадцати апостолов'
elif churches == 7:
	name = 'Верхоспасский собор'
elif churches == 8:
	name = 'Церковь Рождества Богородицы на Сенях'
var = input('Угадай какая церковь?')
while var != name:
	tries += 1
	score -= 10
	var = input('Угадай какая церковь?')
print('Верно! Это ',name., 'Вам потребовалось', tries, ' попыток')
print ('Вам начислено', score , 'очков')
input (' Нажмите Enter для выхода')