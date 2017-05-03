# Задание 8. Вариант 10.
# Rechkalov A.S.

# 29.03.10
import random

WORDS = ("kek", "mek", "program", "python", "moveton", "RSSU")
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
            print("Ну это не серьезно, досвидос")
            break
        print (tip[0])
        tip = tip[1:]
        guess = input("\nВаше предположение: ")
        
    elif guess != pobeda:
        print("Неа")
        guess = input("Давай еще раз ")

    elif guess == pobeda:
        result = 1000-count*100
        print("Баааам, ты угадал! Твой результат: ", result)
        break
    

input("\n\nEnter, чтобы выйти. ")
