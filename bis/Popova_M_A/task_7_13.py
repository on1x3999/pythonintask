# Задача 7. Вариант 13.
# Создайте игру, в которой компьютер загадывает название одного из двух спутников Марса, а игрок должен его угадать.

# Попова М. А.
# 16.04.2017


print('Ответ чувствителен к регистру!')
import random
x=0;och=0;koef=0
def positive_func(a):
	global koef
	global x
	global och
	if a==1:
		ochp=1000-100*koef
		koef=0
		x+=1
		och=och+ochp
		print('В точку!')
		print('Вам начислено', ochp, 'очков')
		print('Всего у вас', och, 'очков')
	if a==0:
		print('Не верно!')
		ochp=(1000-100*koef)
		if ochp>100:
			koef+=1
		else:
			koef+=0
while x>-1:
	if x==0:
		print('Какое название носит крупнейший спутник Марса?')
		y=input('Введите ответ: ')
		if y==('Фобос'):
			positive_func(1)
		else:
			positive_func(0)
	if x==1:
		print('Орбита какого спутника находится ближе всего к Марсу?')
		y=input('Введите ответ: ')
		if y==('Фобос'):
			positive_func(1)
		else:
			positive_func(0)
	if x==2:
		print('Какой спутник Марса был открыт раньше?')
		y=input('Введите ответ: ')
		if y==('Деймос'):
			positive_func(1)
		else:
			positive_func(0)
	if x==3:
		print('Название какого спутника Марса в переводе с греческого означает "паника"?')
		y=input('Введите ответ: ')
		if y==('Деймос'):
			positive_func(1)
		else:
			positive_func(0)
	if x==4:
		print('Вы ответили на ',x,'вопросов и получили',och,'очков. Из-за неверных ответов у вас в сумме было списано ',(x)*1000-och,'очков. Хотите поробовать ещё? Y/N')
		y=input()
	if y==('N'):
		break
	if y==('Y'):
		x=0
		och=0
