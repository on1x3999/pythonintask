#Задача 9. Вариант 15

#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен
#его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток
#узнать, есть ли какая-либо буква в слове, причем программа может отвечать только
#"Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово

#Черенкова Е.Ю.
#07.03.2017

import random

while True:
    magic_word = random.choice(('silver', 'cloud','love','dog','cat','math'))
    print('Length = %i' % len(magic_word))
    for i in range(5):
        letter = input('Enter letter: ')
        if not letter:
            break
        print('YES' if letter[0] in magic_word else 'NO')
    my_word = input('Enter word: ')
    if my_word == 'exit':
        break
    print('You guessed word!!!' if my_word == magic_word else 'Nope...')
    input("Press Enter")