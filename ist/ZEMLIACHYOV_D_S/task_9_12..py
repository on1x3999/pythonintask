import random
 

WORDS = ("апельсин","малина","телефон","компьтер","превращения","человек")
word = random.choice(WORDS)
correct = word
 
print("""Угалайте загаданное слово. У Вас есть 5 попыток узнать, есть ли какая-то буква в нём,после чего нужно попытаться угадать слово. """)
 
print("Загаданное слово содержит {} букв.".format(len(correct)))
 

counter = 1
 
while True:
    if counter <= 5:
        letter = input("\nВведите букву: ")
        if letter.isalpha() and len(letter) == 1:
            if letter in correct:
                print("Да, такая буква есть в слове.")
                counter += 1
            else:
                print("Нет, такой буквы нет в слове.")
                counter += 1
        else:
            print("Возможно, Вы ввели не букву.")
          
    else:
        counter = 1
        break
 
while True:
    if counter <= 5:
        guess = input("\nТеперь попробуйте угадать слово: ")
        if not guess.isalpha():
            print("Неверно.")
        elif guess != correct:
            print("Попробуйте еще раз. У вас осталось попыток: {}".format(5 - counter))
            counter += 1
        elif guess == correct:
            print("Вы угадали слово!")
            break
    else:
        print("Вы проиграли.")
        break
 
input("\n\nНажмите Enter для выхода.")