# Задача 8, Вариант 1-50
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Григорьева
# 19.04.2017

#Анаграммы
#Программа выбирает какое-либо слово и переставляет его буквы
#Задача игрока-восстановить исходное слово.

import random
 
WORDS = ("анаграмма","компьютер","пешеход","товарищ","вселенная","молчание" )
 
word = random.choice(WORDS)
 
correct = word
 
i_dont_know = "Я не знаю"
hint = word[0] + word[1] 
 
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
 
points = 25
 
print(
    """
                               
     Добро пожаловать в игру «Анаграммы»!
Надо переставить буквы так,чтобы получилось осмысленное слово.
    Если вы не знаете ответ , введите: «Я не знаю».
(Для выхода нажмите Enter, не вводя его версию.)
    """
)
print("Это анаграма: ", jumble)
guess = input("\nПопробуйте угадать исходное слово: ")
while guess != "" and guess != correct:
    if guess != correct and not guess == i_dont_know:
        print("К сожалению, вы не правы.")
    if guess == i_dont_know:
        scores -= 5
        print("\nПодсказка! Первые три буквы этого слова", hint)
    guess = input("Попробуйте угадать исходное слово: ")
    if guess == correct:
        print("Да,именно так! Вы отгадали!\n")
 
if points < 0:
    points = 0
print("Спасибо за игру! Ваш счет: ", points)
input("\n\nНажмите Enter, чтобы выйти.")
