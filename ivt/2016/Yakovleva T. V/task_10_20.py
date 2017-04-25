#Задача 10. Вариант 20.

#10.Напишите программу "Генератор персонажей" для игры. Пользователю должно быть
#предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
#Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не 
#только брать эти пункты из общего "пула", но и возвращать их туда из характеристик,
#которым он решил присвоить другие значения.

#Yakovleva T. V.
#04.04.2017

print (
    """
\t\aДобро пожаловать в Генератор персонажей!\n
    """
    )
heroes = {'Анна': ['Анна', 5, 15, 5, 5]}
choice = None
while choice != 0:
    print(
        """
\tМеню:
0 - Выйти
1 - Просмотр персонажей
2 - Добавить персонажа
3 - Редактировать персонажа
4 - Удалить персонажа
        """
        )
    choice = int(input('Ваш выбор: '))

#Выход    
    if choice == 0:
        print ('\nДо свидания!')

#Просмотр        
    elif choice == 1:
        print ('\nВаши герои:')
        for key in heroes:
            print (key, ',', end = ' ')
        print ('\n')

#Добавление
    elif choice == 2:
        print ("")
        name= input ("Как зовут Вашго персонажа? ")
        a=name
        if name not in heroes:
            heroes[name] = [a, 'strength', 'health', 'wisdom', 'agility']
            total = 30
            heroes[name][0] = name
            
            s=int(input('Значение Силы: '))
            while s<0 or s>30:
                s=int(input('Введите корректное значение Силы:'))
            heroes[name][2] = s
            total -= s

            h=int(input('Значение Здоровья: '))
            while h<0 or h>30:
                h=int(input('Введите корректное значение Здоровья:'))
            heroes[name][2] = h
            total -= h

            w=int(input('Значение Мудрости: '))
            while w<0 or w>total:
                w=int(input('Введите корректное значение Мудрости:'))
            heroes[name][3] = w
            total -= w

            heroes[name][4] = total
            print ('Значение Ловкости:', total)

            print ('Персонаж добавлен.\n')

        else:
            print ("Такой персонаж уже есть. Для изменений характеристик отредактируйте его, выбрав 3 пункт меню. \n")

#Редактирование
    elif choice == 3:
        print ("")
        name = input ("Введите имя персонажа: ")
        if name in heroes:
            a=name
            heroes[name] = [a, 'strength', 'health', 'wisdom', 'agility']
            total = 30
            heroes[name][0] = name
            
            s=int(input('Значение Силы: '))
            while s<0 or s>30:
                s=int(input('Введите корректное значение Силы:'))
            heroes[name][2] = s
            total -= s

            h=int(input('Значение Здоровья: '))
            while h<0 or h>30:
                h=int(input('Введите корректное значение Здоровья:'))
            heroes[name][2] = h
            total -= h

            w=int(input('Значение Мудрости: '))
            while w<0 or w>total:
                w=int(input('Введите корректное значение Мудрости:'))
            heroes[name][3] = w
            total -= w

            heroes[name][4] = total
            print ('Значение Ловкости:', total)

            print ('Персонаж', a, 'изменен.\n')

        else:
            print ("Такого персонажа нет. Добавьте его, выбрав 2 рункт в меню. \n")

#Удаление
    elif choice == 4:
        name=input('Какого персонажа Вы хотите удалить? ')
        if name in heroes:
            del heroes[name]
            print ('Персонаж удален.')
        else:
            print ('Такого персонажа нет. Добавьте его, выбрав 2 пункт в меню. \n')

#Ошибочный ввод
    else:
        print ("Такого пункта в меню нет.")

input ("Нажмите Enter, чтобы выйти")
