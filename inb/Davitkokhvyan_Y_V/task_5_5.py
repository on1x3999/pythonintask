# Задача 5. Вариант 5.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из восьми соборов Московского кремля.

# Давиткохвян Юрий Васильевич
# 12.03.2017

print("Программа случайным образом отображает название одного из восьми соборов Московского кремля")

import random

builds = [
    "Успенский собор",
    "Благовещенский собор",
    "Архангельский собор",
    "Колокольня Ивана Великого",
    "Патриарший дворец и собор Двенадцати Апостолов",
    "Верхоспасский собор"
    ]
b = random.choice(builds)
print("Один из соборов Московского кремля, это:", b)
input("\n\nНажмите Enter для выхода.")
    
