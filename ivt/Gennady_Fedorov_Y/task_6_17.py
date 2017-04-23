#Задача 6. Вариант 17.
#Создайте игру, в которой компьютер загадывает название одного из пяти
#космических челноков проекта Спейс шаттл, а игрок должен его угадать.

#Федоров Г.Ю.
#28.02.2017

import random

print("какой из 5 челноков проекта спейс шаттл загадала программа ?")
 
the_number = random.randint(1, 5)

guess = int(input("Take a guess: "))
    
while guess != the_number :
    print("вы не угадали!")
    if guess > the_number :
        print("меньше")
    else :
        print("больше")
    guess = int(input("догадка: "))
    if guess == the_number :
        print("вы угадали")

        print("загаданное число было", the_number)
        
    
            
 
     
     
input("\n\nPress the enter key to exit.")

