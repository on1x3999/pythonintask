# Задание 6. Вариант 10.
# Rechkalov A.S.

# 29.03.17
import random

triforce = ("Германия", "Австро-венгрия", "Италия")
word = random.choice(triforce)

vvod = input("Ваше слово:")

while vvod != word:
    vvod = input("Ваше слово:")

print("Правильно!")
input("\n\nНажмите Enter, чтобы выйти.")


