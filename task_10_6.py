Characteristics = {'Strength':5,
				   'Agility':5,
				   'Health':5,
				   'Intelligent':5}
Сhoice = None
Points = 30

print ('У вас есть 30 очков характеристик для распределения, \n значения характеристик не могут опускаться ниже 5 !!! \n')

while Сhoice != 0:
    A = True
    Refresh = Points
    
    if Points == 0 :
        print ('У вас закончились очки характеристик, если вы уверены в своем выборе, введите 0 для выхода')
        
    print(
    """
    0 - Выход
    1 - Прибавить очки характеристик
    2 - Убавить очки характеристик
    
	На данный момент ваши характеристики""",Characteristics,"""
    """
    )
	
    Choice = input('Выбор: ')
    
    if Choice == '0':
        print ('До свидания')
	
    elif Choice == '1':
        print (
		'''
		Введите на английском характеристику, которую хотите повысить
		Strength - Сила
		Agility - Ловкость
		Health - Жизни
		Intelligent - Интеллект
		На данный момент ваши характеристики ''',Characteristics,'''
		'''
		)
        
        CharName = input ()
        while CharName not in Characteristics :
            CharName = input ('Введите точное название характеристики')
		
        while Points < 0 or A == True or Characteristics[CharName] <= 5 :
		
            if Points < 0 :
                print ('\n\t\033[96m Недопустимое изменение характеристик, попробуйте еще раз! \033[0m\n')
                Points = Refresh
                
            A = False
            print ('Вам доступно',Points, 'очков')
            Value = int(input ('Введите на сколько пунктов вы хотите повысить характеристику: '))
            Characteristics[CharName] += Value
            Points -= Value
	    
    elif Choice == '2':
        print (
		'''
		Введите на английском характеристику, которую хотите понизить
		Strength - Сила
		Agility - Ловкость
		Health - Жизни
		Intelligent - Интеллект
		На данный момент ваши характеристики """,Characteristics,"""
		'''
		)
        CharName = input ()
        
        while CharName not in Characteristics :
            CharName = input ('Введите точное название характеристики')
            
        while Points > 30 or A==True and  Characteristics[CharName] <=5 :
		
            if Points > 30:
                
                print ('\n\t\033[96m Недопустимое изменение характеристик, попробуйте еще раз! \033[0m\n')
                Points = Refresh
                
            A=False
            print ('Вам доступно',Points, 'очков')
            Value = int(input ('Введите на сколько пунктов вы хотите убавить характеристику: '))
            Characteristics[CharName] -= Value
            Points += Value
			
input ()
