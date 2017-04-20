#Задача 5 Вариант 3
#

#Галахова Елена Дмитриевна
#20.03.2017

import random 
print("Программа случайным образом отображает название одного из цветов радуги.") 
x = int (random.randint(1,7)) 
print("Цвет") 
if x == 1:
 print('Красный') 
elif x == 2: 
 print ('Оранжевый') 
elif x==3: 
 print('Жёлтый') 
elif x==4: 
 print('Зелёный') 
elif x==5: 
 print('Голубой') 
elif x==6: 
 print('Синий') 
else: 
 print ('Фиолетовый') 

input("Для выхода нажмите Enter.")
