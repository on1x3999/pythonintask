#ГолубеваЕ.А.
#1Вариант 5задание
#18.04.17
#Напишите программу, которая бы при запуске случайным образом отображала
#название одного из семи чудес света.
import random
stuffing = random.randint(1, 7)

if stuffing == 1:
   print("Пирамида Хеопса")

elif stuffing == 2:
 
   print("Висячие сады Семирамиды")
 
elif stuffing == 3:
   print("Статуя Зевса в Олимпии")
 
elif stuffing == 4:
   print("Храм Артемиды в Эфесе")
 
elif stuffing == 5:
   print("Мавзолей в Галикарнасе")

elif stuffing == 6:
   print("Колосс Родосский")

else:
   print("Александрийский маяк")

 
 
input("\n\nНажмите Enter, чтобы выйти.")
 
