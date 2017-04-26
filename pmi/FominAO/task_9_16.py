# Задача 10. Вариант 16.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
# Фомин Александр Олегович
# 04.04.2017
print('\nTry to guess the word.\n')
word = 'impossible'
print('There are %s latters in this word.\n' % len(word))
print('You have only 5 attempts to do it!\n')
lat = input('Your latter: ')
countl = 0
n = 0
def catcher ():
    flag = False
    for i in word:
        if i == lat:
	        flag = True
    return(flag)
while n<3: 
    n = n + 1
    flag = catcher();
    if flag==True:
	    lat = input('You got this one!\nLets continue: ')
    else:
        lat = input('No, its not.\nLets try again: ')
if flag==True:
    lat = input('You got this one!\nAnd your last one: ')
else:
    lat = input('No, its not.\nLets try last time: ')
flag = catcher();
if flag==True:
    wordatt = input('You got this one!\nNow try to write whole ward: ')
else:
    wordatt = input('No, its not.\nYou can write whole word, if you got it:  ')	
if word == wordatt:
    print('You right!\n Thanks for playing!')
else:
    print('Unfortunately you are not right.\nThanks for playing, good luck next time.\n')
input('\n\nPress Enter to close...')