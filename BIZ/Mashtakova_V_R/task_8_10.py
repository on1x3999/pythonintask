#	Задача 8. Вариант 10.
#       Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки,
#       отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#	Mashtakova V.R.
#	17.04.2017

import random

WORDS = ("life", "pdf", "lol", "python", "baber", "ritka")
word = random.choice(WORDS)
pobeda = word
tip = pobeda
annagrama = ""
count = 0;

while word:
    position = random.randrange(len(word))
    annagrama += word[position]
    word = word[:position] + word[(position+1):]

print ("Вот анаграмма:", annagrama)
print("Если не знаешь и хочешь подсказку - нажмите Enter")
guess = input("\nВаше предположение: ")

while 1>0:
    if guess == "":
        count += 1
        if len(pobeda) == 1:
            print("НЕТ")
            break
        print (tip[0])
        tip = tip[1:]
        guess = input("\nВаше предположение: ")
        
    elif guess != pobeda:
        print("Нет")
        guess = input("Еще попытка ")

    elif guess == pobeda:
        result = 1000-count*100
        print("Ураааа: ", result)
        break
    

input("\n\nEnter, чтобы выйти. ")
