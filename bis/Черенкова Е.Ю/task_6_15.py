#Задача 6. Вариант 15

#Создайте игру, в которой компьютер загадывает название одного из двенадцати
#городов, входящих в Золотое кольцо России, а игрок должен его угадать.

#Черенкова Е.Ю.
#06.03.2017
import random
city=["Pereslavl","Rostov" ,"Yaroslavl" ,"Kostroma ",
      "Ivanovo" , "Suzdal" ,"Vladimir","Alexandrov ",
      "hierarchy" , "Gorokhovets", "Gus-Crystal", 
      "Dmitrov"]
i=random.randint(0,11)
print("Let's play a game. Guess the city, located in the golden ring")
city_selected=input("Select a city: ")
if city[i]==city_selected:
    print("You win!!!")
else:
    print("You lose.I put forth:",city[i],".Try again")
input("Press Enter")