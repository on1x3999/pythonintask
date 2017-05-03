
#Задача 10. Вариант 15.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,
#чтобы пользователь мог не только брать эти пункты из общего "пула", но и
#возвращать их туда из характеристик, которым он решил присвоить другие
#значения.

#Shiyanova A.V.
#22.03.2017

scores = 30
hp = 0
strenght = 0
wisdom = 0
agility = 0
heroes =[]
choice =None
print (
    """
       Добро пожаловать в "Генератор персонажей"
       Вам предоставлено 30 очков, которые Вам нужно распределить 
	   между четырьмя характристиками. 
	   Полученных персонажей можно сохранить.
    """
    )
while choice != '0':
    print(
        """
Создание персонажа:
0 - Выйти
1 - Здоровье""",hp,"""
2 - Сила""",strenght,"""
3 - Мудрость""",wisdom,"""
4 - Ловкость""",agility,"""
__________________________________
5 - Сгенерировать персонажа
6 - Список созданных персонажей
7 - Обнулить характеристики
"""
    )
    choice= input ('Выберите пункт:')
    if choice == '0':
        print ('До свидания!')
    elif choice == '1':
        print (
        """
1 - Добавить очки
2 - Отнять очки
    """
        )
        choice_2= input('Ваш выбор:')
        if choice_2 == '1':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',hp,'очков')
            hp_c = int(input('Сколько очков вы хотите прибавить?'))
            if hp_c>scores:
                print ('\nК сожалению у Вас нет столько очков.')
            else:
                hp = hp + hp_c
                scores = scores - hp_c
        elif choice_2 == '2':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',hp,'очков')
            hp_c = int(input('Сколько очков вы хотите отнять?'))
            if scores == 30 or hp_c>hp:
                print ('\nВы не можете отправить персонажа в минус.')
            else:
                hp = hp - hp_c
                scores = scores + hp_c
        else:
            print ('\nНе удалось определить команду.')
    elif choice == '2':
        print (
        """
1 - Добавить очки
2 - Отнять очки
    """
        )
        choice_2= input('Ваш выбор:')
        if choice_2 == '1':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',strenght,'очков')
            strenght_c = int(input('Сколько очков вы хотите прибавить?'))
            if strenght_c>scores:
                print ('\К сожалению у Вас нет столько очков.')
            else: 
                strenght = strenght + strenght_c
                scores = scores - strenght_c
        elif choice_2 == '2':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',strenght,'очков')
            strenght_c = int(input('Сколько очков вы хотите отнять?'))
            if scores == 30 or strenght_c>strenght:
                print ('\nВы не можете отправить персонажа в минус.')
            else:
                strenght = strenght - strenght_c
                scores = scores + strenght_c
        else:
            print ('\nНе удалось определить команду.')
    elif choice == '3':
        print (
        """
1 - Добавить очки
2 - Отнять очки
    """
        )
        choice_2= input('Ваш выбор:')
        if choice_2 == '1':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',wisdom,'очков')
            wisdom_c = int(input('Сколько очков вы хотите прибавить?'))
            if wisdom_c>scores:
                print ('\nК сожалению у Вас нет столько очков.')
            else:
                wisdom = wisdom + wisdom_c
                scores = scores - wisdom_c
        elif choice_2 == '2':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',wisdom,'очков')
            wisdom_c = int(input('Сколько очков вы хотите отнять?'))
            if scores == 30 or wisdom_c>wisdom:
                print ('\nВы не можете отправить персонажа в минус.')
            else:
                wisdom = wisdom - wisdom_c
                scores = scores + wisdom_c
        else:
            print ('\nНе удалось определить команду.')
    elif choice == '4':
        print (
        """
1 - Добавить очки
2 - Отнять очки
    """
        )
        choice_2= input('Ваш выбор:')
        if choice_2 == '1':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',agility,'очков')
            agility_c = int(input('Сколько очков вы хотите прибавить?'))
            if agility_c>scores:
                print ('\nК сожалению у Вас нет столько очков.')
            else:
                agility = agility + agility_c
                scores = scores - agility_c
        elif choice_2 == '2':
            print ('У Вас имеется',scores,'свободных очков.')
            print ('Эта характеристика содержит',agility,'очков')
            agility_c = int(input('Сколько очков вы хотите отнять?'))
            if scores == 30 or agility_c>agility:
                print ('\nВы не можете отправить персонажа в минус.')
            else:
                agility = agility - agility_c
                scores = scores + agility_c
        else:
            print ('\nНе удалось определить команду.')
    elif choice == '5':
        print ('Ваши характеристики равны:')
        stats= print("""
Здоровье""",hp,"""
Сила""",strenght,"""
Мудрость""",wisdom,"""
Ловкость""",agility
        )
        stats=('Здоровье',hp,'Сила',strenght,'Мудрость',wisdom,'Ловкость',agility)
        hero= input ('Введите название созданного персонажа: ')
        entry= (stats,hero)
        heroes.append(entry)
    elif choice == '6':
        print ('Список созданных персонажей\n')
        print ('НАЗВАНИЕ\tСТАТЫ')
        for entry in heroes:
            stats,hero= entry
            print (hero,'\t',stats)
    elif choice == '7':
        scores = 30
        hp = 0
        strenght = 0
        wisdom = 0
        agility = 0
    else:
        print ('\nНе удалось определить команду.')
