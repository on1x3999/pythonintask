name = 'тициано вечеллио'
nickname = 'тициан'
question = ('Герой нашей сегодняшней программы ' + name
            + '\nПод каким же именем мы знаем этого человека? Ваш ответ:')
			
result = input(question)

if result.lower() == nickname:
    print('\nВерно, ' + name + ' - ' + result)
else:
    print('\nНе верно')	
	
input('\n\nНажмите Enter для выхода.')	