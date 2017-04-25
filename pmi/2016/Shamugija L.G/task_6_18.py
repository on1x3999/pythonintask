#Задача 6. Вариант 18.
#Создайте игру, в которой компьютер загадывает имя одной из трех 
#официальных жен Зевса, а игрок должен его угадать.

#Shamugija L.G.
#13.03.2017

import random
print("Программа загадывает имя одной из трех официальных жен Зевса, а игрок должен его угадать.")
name = input("\n\nНазовите одно из имен оффицильных жен Зевса: ")
number = random.randint(1, 3)
if number == 1 :
 realname = 'Метида'
elif number == 2 :
 realname = 'Фемида'
else :
 realname = 'Гера'
if name == realname :
 print("Верно! Это", realname,"\nКак вам удалось угадать?")
else :
 print("Ох, нет, ты ошибся.")

input("\n\nPress Enter")
