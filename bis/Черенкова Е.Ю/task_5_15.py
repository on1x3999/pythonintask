# coding: utf-8
#Напишите программу, которая бы при запуске случайным образом 
#отображала название одного из двенадцати городов, входящих в Золотое кольцо России.

#Черенкова Е.Ю.
#03.03.2017

import random
city=["Pereslavl","Rostov" ,"Yaroslavl" ,"Kostroma ",
      "Ivanovo" , "Suzdal" ,"Vladimir,Alexandrov ",
      "hierarchy" , "Gorokhovets", "Gus-Crystal", 
      "Dmitrov", "Kalyazin", "Kideksha", "Moscow", 
      "Moore", "Myshkin", "Palekh" , "Ples", "Rybinsk",
      "Tutaev", "Uglich", "Yuriev-Polsky", "Shuya"]
i=random.randint(0,25)
print(city[i])
input("Press Enter")

