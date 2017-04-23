# Задача 8. Вариант 6.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Горлов Евгений Михайлович
# 08.04.2017


import random
Words = ('мяч','подсказка','вертолёт','анаграмма')
Word = random.choice (Words)
AdditionalWord = Word
Jumble = ''
Score = 100
for letter in Word :
    Position = random.randrange (0,len(Word))
    Jumble += Word[Position]
    Word = Word[:Position] + Word[(Position+1):]
print ('Попробуйте состоваить слово из этой анаграммы', Jumble)
Guess = input ('Введите слово: ')
while Guess != AdditionalWord:
    print ('\n\nДля подсказки введите: "помощь"')
    Guess = input ('Не верно, попробуйте еще раз: ')
    if Guess != AdditionalWord and Guess == 'помощь':
        Score = 1
        if AdditionalWord == 'мяч':
            print ('Подсказка: он круглый')
        elif AdditionalWord == 'подсказка':
            print ('Подсказка: то, без чего вы не можете решить анаграмму')
        elif AdditionalWord == 'вертолёт':
            print ('Подсказка: вертикальный взлет')
        elif AdditionalWord == 'анаграмма':
            print ('Подсказка: скорее всего, для вас это очень сложная игра')
print ('Поздравляем вы отгадали, ваш счет:', Score)
input ('Для выхода нажмите Enter')