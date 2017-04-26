#Задача 5. Вариант 12.
 #Напишите программу, которая бы при запуске случайным образом отображала
 #название одного из двенадцати подвигов Геракла.

 #Sedykh E. A.
 #23.04.2017
 
 import random
 print ('Программа случайным образом отображает название одного из двенадцати подвигов Геракла ')
 achievement = random.randint(1,12)
 if achievement == 1:
 	print('\n\\Немейский лев')
 elif achievement == 2:
 	print('\n\tЛернейская гидра')
 elif achievement == 3:
 	print('\n\tСтимфалийские птицы')
 elif achievement == 4:
 	print('\n\tКеринейская лань')
 elif achievement == 5:
 	print('\n\tЭриманфский кабан и битва с кентаврами')
 elif achievement == 6:
 	print('\n\tСкотный двор царя Авгия')
 elif achievement == 7:
 	print('\n\tКритский бык')
 elif achievement == 8:
 	print('\n\tКони Диомеда')
 elif achievement == 9:
 	print('\n\tПояс Ипполиты')
 elif achievement == 10:
 	print('\n\tКоровы Гериона')
 elif achievement == 11:
 	print('\n\t Похищение Цербера')
 else:
 	print('\n\tЗолотые яблоки гесперид')
 input('\nНажмите Enter для выхода')