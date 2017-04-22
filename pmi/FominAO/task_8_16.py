# Задача 8. Вариант 16.
# Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Фомин Александр Олегович
# 08.04.2017
import random
words = [ 'игра', 'анаграмма', 'молоко' , 'новость', 'жар' , 'холодильник' ]
word = random.choice(words)
correct = word
def hint (i, dlin) :
    global correct
    if i < dlin:   
        podskazka = ''
        j = 0
        while j < i+1:
            podskazka = podskazka + correct[j]
            j+=1
        print("\nПодсказка! Первые буквы слова: ", podskazka)
    else:
         print("Подумайте хорошенько!")

anagramma = ''

while word:
    position=random.randrange(len(word))
    anagramma+=word[position]
    word=word[:position]+word[(position+1):]

scores = 100
j = 0;
k = 0;
print ("Добро пожаловать в игру 'Анаграммы!'\nНадо переставить буквы так, чтобы получилось слово.\nДля выхода нажмите Enter, не вводя своей версии.")
print("Aнаграмма: ", anagramma)
guess = input ("\nПопробуйте отгадать исходное слово: ")
while guess != "" and guess != correct:
    if guess != correct and not guess == "Не знаю":
        print("К сожалению, вы неправы.")
        j+=1
        guess = input ("\nПопробуйте отгадать исходное слово: ")
    if guess == "Не знаю":
        hint(k + 1, len(correct))
        j+=1
        k+=1
        guess = input("Попробуйте отгадать исходное слово: ")
    if guess == correct:
        print("Да, именно так! Вы отгадали!\n")
        j+=1

scores = 100 - 10*j - 10*k
if (scores < 0) or (guess == ""):
    scores = 0
print("Спасибо за игру! У вас", scores, "очков!")
input ('\n\nНажмите Enter, чтобы выйти.')