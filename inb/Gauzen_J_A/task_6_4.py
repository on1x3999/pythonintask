# Задача 6. №Вариант 4.
#Создайте игру, в которой компьютер загадывает название одного из двенадцати подвигов Геракла, а игрок должен его угадать.

#16.04.2017
# Гаузен Юлия Александровна

print("Я загадаю один из 12 подвигов Геракла,а ты попробуй угадать.")
podv=["Немейский лев","Лернейская гидра","Стимфалийские птицы","Керинейская лань","Эриманфский кабан и битва с кентаврами","Скотный двор царя Авгия","Критский бык","Кони Диомеда","Пояс Ипполиты","Коровы Гериона","Похищение Цербера","Золотые яблоки гесперид"]
import random
a=random.choice(podv)
b=input("Твой ответ:")
if a==b:
    print("Все верно!")
else:
    print("Не верно! Верный ответ:",a)

input("Нажмите Enter, чтобы выйти.")

