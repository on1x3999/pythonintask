#Задача 7. Вариант 17.
#Создайте игру, в которой компьютер загадывает название одного из пяти
#космических челноков проекта Спейс шаттл, а игрок должен его угадать.

#Федоров Г.Ю.
#28.02.2017


import random

print("какой из 5 челноков проекта спейс шаттл загадала программа ?")
 
the_number = random.randint(1, 5)

guess = int(input("Take a guess: "))
 
ballov = 100
   
while guess != the_number :
    print("вы не угадали!")
    if guess > the_number :
        ballov = ballov-2
        print("меньше")
    else :
        ballov= ballov-2
        print("больше")
    guess = int(input("догадка: "))
    if guess == the_number :
        print("вы угадали")

        print("загаданное число было", the_number)
        print("вы получили столько баллов", ballov)
    
            
 
     
     
input("\n\nPress the enter key to exit.")


