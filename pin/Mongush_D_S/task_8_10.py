# Задание 8. Вариант 10.
# Mongush D.S.

# 05.04.10
import random

#От типовой задачи в учебнике эта отличается двумя вещами
WORDS = ("peripheral", "flatbed", "python", "anarchy")
word = random.choice(WORDS)
win = word
tip = win
annagrama = ""
count = 0;


while word:
    #Формируем анаграмму при помощи срезов
    position = random.randrange(len(word))
    annagrama += word[position]
    word = word[:position] + word[(position+1):]

print ("Вот анаграмма:", annagrama)
print("Если нет догадок и хочешь подсказку - нажми Enter")
guess = input("\nВаше предположение: ")

while 0<1:
    # Тут человек, просто нажимая Enter, получает подсказку
    if guess == "":
        #Считаем количество подсказок, для того, чтобы уменьшить результат тех, кто использовал подсказки, в зависимости от их количества
        count += 1
        if len(win) == 1:
            print("Осталась одна буква! Так не честно!")
            break
        #Здесь так же используем срезы, чтобы давать подсказки правильно
        print (tip[0])
        tip = tip[1:]
        guess = input("\nВаше предположение: ")
        
    elif guess != win:
        print("Вы не угадали!")
        guess = input("Попробуйте еще раз ")

    elif guess == win:
        #Уменьшаем результат
        result = 1000-count*100
        print("Вы угадали! Ваш результат: ", result)
        break
    

input("\n\nEnter, чтобы выйти. ")
