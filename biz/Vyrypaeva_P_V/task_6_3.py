#Задача6.Вариант3. 
#Создайте игру, в которой компьютер загадывает имя одной из семи птиц, доступных с первой версии игры Angry Birds, а игрок должен его угадать.

#Вырыпаева П. В.
#29.03.2017

import random
birds=['Рэд','Чак','Бомб', 'Матильда', 'Джей', 'Джейк', 'Джим'] 
variant=input('Назовите имя одной из птиц игры Angry Birds. Предложенные варианты: Рэд, Чак, Бомб, Матильда, Джей, Джейк, Джим') 
answer = random.choice(birds) 
if variant == answer: 
    print('Вы угадали!!\nПравильный ответ:', answer) 
else: 
    print('Вы не угадали!!\nПравильный ответ:', answer) 
input('Нажмите Enter для выхода')
