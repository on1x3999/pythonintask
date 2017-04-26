#Задача 6. Вариант 12.
 #Создайте игру, в которой компьютер загадывает название одного из восьми
#соборов Московского кремля, а игрок должен его угадать.
 
 #Sedykh E. A.
 #23.04.2017
 
 import random
 tries = 1
 score = 1000
 print('Я загадала одно из названий соборов Московского кремля ')
 Cathedral = random.randint(1,3)
 if Cathedral == 1:
 	guessed = 'Колокольня Ивана Великого'
 elif Cathedral == 2:
 	guessed = 'Успенский собор'
 elif Cathedral == 3:
 	guessed = 'Верхоспасский собор'
 name = input('Угадай название!')
 while name != guessed:
 	tries += 1
 	score -= 300
 	name = input('\n\nПопробуйте снова:')
 print('\nВерно! Это', guessed, 'Вам потребовалось', tries, 'попыток')
 print('\nНачислено' , score , 'очков')
 input ('\nНажмите Enter для завершения.')