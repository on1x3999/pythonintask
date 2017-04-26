# Задача 9 Вариант 5
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Дуненков Р.Е.
# 05.04.2017.
 
import random
 
WORDS = ('питон', 'анаграмма', 'простая', 'сложная', 'ответ', 'подстаканник')
word = random.choice(WORDS)
print('Компьютер загадал слово.'
      '\nУ вас есть 5 попыток узнать есть ли в нем какая-нибудь буква.'
      '\nЗагаданное слово состоит из ', len(word), 'букв\n')

result = ''
i = 0
while i < len(word):
    result += '*'
    i = i + 1

account = 5
while account > 0:
    char = input('Введите букву: ')
    resultD = result
    i = 0
    while i < len(word):
        if char == word[i]:
            result = result[:i] + word[i] + result[i + 1:]
        i = i + 1

    if resultD != result:
        print('Да, есть такая буква\n', result, '\n')
    else:
        print('Буквы ', char, ' нет\n', result, '\n')
    account = account - 1
 
usersWord = input('Количество подсказок исчерпано.'
                   '\nПопробуйте отгадать слово: ')
while usersWord != word:
    if usersWord == '':
        break
    else:
         usersWord = input('Неверно! попробуйте снова: ')

if usersWord == word:
    print('Верно!')

input('\n\nНажмите enter для выхода')
