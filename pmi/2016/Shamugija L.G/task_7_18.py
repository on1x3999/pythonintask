#Задача 7. Вариант 18.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой 
#игрок получал бы большее количество баллов за меньшее количество попыток.

#Shamugija L.G.
#13.03.2017

import random
print("Программа загадывает имя одной из трех официальных жен Зевса, а игрок должен его угадать.")
number = random.randint(1, 3)
if number == 1 :
 realname = 'Метида'
elif number == 2 :
 realname = 'Фемида'
else :
 realname = 'Гера'
i = 1
point = 120
while i <= 3 :
 name = input("\n\nНазовите одно из имен оффицильных жен Зевса: ")
 if name == realname :
  print("Верно! Это", realname,"\nВы заработали:", point, "баллов.\nИ как тебе удалось угадать?")
  i = 4
 else :
  point = point - 40
  print("Ох, нет, ты ошибся.")
 if i != 3 :
  print("Попробуй еще раз.")
 else :
  print("\n\n\n\t\t\tYOU COULDN`T WIN!")
 i += 1
input("\n\nPress Enter")

