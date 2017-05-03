# Задание 7. Вариант 10.
# Rechkalov A.S.

# 29.03.17
import random

triforce = ("Германия", "Австро-венгрия", "Италия")
word = random.choice(triforce)

vvod = input("Ваше слово:")
count = 1

while vvod != word:
    vvod = input("Ваше слово:")
    count += 1

result = 1000 // count
print("Правильно! Ваш результат:", result)
input("\n\nНажмите Enter, чтобы выйти.")

