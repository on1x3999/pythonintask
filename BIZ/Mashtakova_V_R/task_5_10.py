#	Задача 5. Вариант 10.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из шести континентов Земли.
#	Mashtakova V.R.
#	17.04.2017

print("один из 6ти континентов") 
import random 
continent=random.randit(1,6) 
if continent == 1: 
print("африка") 
if continent == 2: 
print("евразия") 
if continent == 3: 
print("австралия") 
if continent == 4: 
print("северная америка") 
if continent == 5: 
print("южная америка") 
if continent == 6: 
print("антарктида") 
input("нажми Enter для выхода")
