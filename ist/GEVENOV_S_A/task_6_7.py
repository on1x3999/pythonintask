# Задача 6. Вариант 7.
# Создайте	игру,	в	которой	компьютер	загадывает	имя	одного	из	двух	сооснователей компании	Google,	а	игрок	должен	его	угадать.

# Gevenov S. A.
# 16.04.2017

import random 

Googlefounders=['Ларри Пейдж', 'Сергей Брин'] 
VvodGooglefounders=input('Назовите имя одного из двух сооснователей компании Google:') 
a=random.choice(Googlefounders) 

if a==VvodGooglefounders: 
    print('Вы угадали! \n Правильный ответ', a) 
else: 
    print('Вы не угадали ! \n Правильный ответ', a) 
input("\n\nНажмите Enter для выхода.")