
from datetime import date

name = 'Лариса Петровна Косач-Квитка'
nickName = 'Леся Украинка'
dateBirth = date(1871,2,25)
dateDeath = date(1913,8,1)
age = int((dateDeath - dateBirth).days/365.25) #разность возвращает объект timedelta
data = 'Деятель украинской культуры, поэтесса, писательница, переводчик.'

msg = ('Имя: ' + name
      +'\nПсевдоним: ' + nickName
      +'\nДата рождения: ' + dateBirth.strftime('%d.%m.%Y')
      +'\nДата смерти: ' + dateDeath.strftime('%d.%m.%Y')
      +'\nВозраст: ' + str(age)
      +'\nФакты: ' + data)

print(msg)
input('\n\nНажмите Enter для выхода.')