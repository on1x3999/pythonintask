import random
print('Добро пожаловать в игру "Анаграммы"!\nНадо переставить буквы так, чтобы получилось осмысленное слово.')
words=["елка","бутылка","потолок","солнце","курица"]
word=random.choice(words)
x=list(word)
random.shuffle(x)
print('Вот анаграмма: ',end='')
for i in x:
    print(i,end='')
print()
guess=input('Попробуйте отгадать исходное слово: ')
p=0
while guess not in words:
    guess=input('Неправильно! Попробуйте еще раз: ')
    p+=1
    if p<5:continue
    else: print('Подсказка: первая буква - ',word[0])
print('Правильно! Загаданное слово: ',guess)

