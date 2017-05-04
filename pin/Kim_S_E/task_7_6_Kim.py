#Задача 7. Вариант 6.

#1-50.	Разработайте	систему	начисления	очков	для	задачи	6,	в	соответствии	с	которой

#игрок	получал	бы	большее	количество	баллов	за	меньшее	количество	попыток.

#Kim Sergey Evgen'evi4



import random



city_numbers = random.randint(1,7)



if city_numbers == 1 :

    city = "Москва"

elif city_numbers == 2 :

    city = "Петербург"

elif city_numbers == 3 :

     city = "Нижний Новгород"

elif city_numbers == 4 :

    city = "Новосибирск"

elif city_numbers == 5 :

    city = "Самара"

elif city_numbers == 6 :

    city = "Екатеринбург"

elif city_numbers == 7 :

    city = "Казань"



trial = 6

bonus = 35000



while trial > 0 :

    answer = input("Назовите один из городов, где присутствует работающий метрополитен: ")

    if answer ==  city:

        print("\nВы угадали!")

        print("Вам начислено", bonus, "баллов.")

        break

    else :

        print("\nВы не угадали!")

        if trial > 1 :

            print("Попробуйте еще раз.")

        else :

            print("Правильный ответ: ", city)

        

    trial -= 1

    bonus -= 1000	

input("\nНажмите Enter для выхода")