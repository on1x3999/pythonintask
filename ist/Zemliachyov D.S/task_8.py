
import random

WORDS = ('хлеб', 'зарядка', 'карты', 'цирк', 'ужин', 'апельсин', 'бинокль')
word = random.choice(WORDS)
correct = word
jumble = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]


print('Добро пожаловать в игру "Анаграммы"!'
       +'\nнужно поставить буквы так. чтобы получилось осмысленное слово.'
       +'\n(Для выхода нажмите Enter. не вводя своей версии).'
       +'\n(Чтобы получить подсказку в ведите help)'
      )
print('\n\nМаксимальное количество баллов:', len(jumble))
print('Вот анаграмма: ', jumble)


account = len(jumble)
nHelp = 0 
guess = input('\n\nПопробуйте отгадать исходное слово: ')

while(guess != correct and guess != ''):
    if(guess == 'help'):
        if account > 0: 
            account = account -1
            print(nHelp + 1, '-ая буква ', correct[nHelp]
                  +'\nКоличесто оставшихся баллов: ', account)
            nHelp = nHelp + 1
        else:
            print('Подсказки закончились')
            
    else:
        print('Вы не правы.\nКоличесто оставшихся баллов: ', account)
        
    guess = input('\nПопробуйте отгадать исходное слово: ')
    
if guess == correct: 
      print('Вы отгадали. Колличество ваших баллов ', account, ' из ', len(jumble))
        
print('Спасибо за игру!')
input('Нажмите enter для выхода')
      

      
    