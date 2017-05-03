#Задача 7. Вариант 15

#Создайте игру, в которой компьютер загадывает название одного из двенадцати
#городов, входящих в Золотое кольцо России, а игрок должен его угадать.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой
#игрок получал бы большее количество баллов за меньшее количество попыток.

#Черенкова Е.Ю.
#06.03.2017
import random
city=["Pereslavl","Rostov" ,"Yaroslavl" ,"Kostroma ",
      "Ivanovo" , "Suzdal" ,"Vladimir","Alexandrov ",
      "hierarchy" , "Gorokhovets", "Gus-Crystal", 
      "Dmitrov"]
print("Let's play a game. Guess the city, located in the golden ring")
score=0
j=0
while j<10000:
    city_selected=input("Select a city: ")
    i=random.randint(0,11)
    if city[i]==city_selected:
        prize=10000/(j+1)
        score=score+prize
        print("You win!!!You prize: ",prize,"You score=",score)
        j=0
    else:
        print("You lose.I put forth:",city[i],".Try again")
        j+=1
input("Press Enter")