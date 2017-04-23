# Задача 10. Вариант 14.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возращать их туда из характеристик, которым он решил присвоить другие значения.

# Rozum R.S.
# 19.04.2017

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.point = 30
        self.force = 0
        self.health = 0
        self.wisdom = 0
        self.agility = 0
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        #Метка: остаток очков
        self.l_point_num = Label(self, text = "Осталось очков: " + str(self.point))
        self.l_point_num.grid(row = 0, column = 0, rowspan = 2, columnspan = 3, padx = 10,  pady = 5)
        #Метка: параметр силы
        self.l_force = Label(self, text = "Сила - " + str(self.force))
        self.l_force.grid(row = 2, column = 1, columnspan = 2, sticky = 'w')

        #Метка: Параметр здоровья
        self.l_health = Label(self, text = "Здоровье - " + str(self.health))
        self.l_health.grid(row = 3, column = 1, columnspan = 2, sticky='w')

        #Метка: параметр мудрости
        self.l_wisdom = Label(self, text = "Мудрость - " + str(self.wisdom))
        self.l_wisdom.grid(row=4, column=1, columnspan=2, sticky='w')

        #Метка: параметр ловкости
        self.l_agility = Label(self, text = "Ловкость - " + str(self.agility))
        self.l_agility.grid(row=5, column=1, columnspan=2, sticky='w')

        #Кнопка: плюс к параметру силы
        self.plus_force = Button(self, text = "+", command = self.plus_force_but)
        self.plus_force.grid( row = 2, column = 3, ipadx = 3, ipady = 2, padx = 10)
        #Кнопка: минус к паметру силы
        self.minus_force = Button(self, text = "-", command = self.minus_force_but)
        self.minus_force.grid( row = 2, column = 4, ipadx = 3, ipady =2, padx=10)

        #Кнопка: плюс к параметру здровья
        self.plus_health = Button(self, text = "+", command = self.plus_health_but)
        self.plus_health.grid(row= 3, column=3, ipadx=3, ipady=2, padx=10)
        #Кнопка: минус к паметру здоровья
        self.minus_health = Button(self, text="-", command=self.minus_health_but)
        self.minus_health.grid(row= 3, column=4, ipadx=3, ipady=2, padx=10,pady =10)

        #Кнопка: плюс к параметру мудрости
        self.plus_wisdom = Button(self, text="+", command= self.plus_wisdom_but)
        self.plus_wisdom.grid(row= 4, column=3, ipadx=3, ipady=2, padx=10)
        #Кнопка: минус к параметру мудрости
        self.minus_wisdom = Button(self, text="-", command= self.minus_wisdom_but)
        self.minus_wisdom.grid(row= 4, column=4, ipadx=3, ipady=2, padx=10)

        #Кнопка: плюс к параметру ловоксти
        self.plus_agility = Button(self, text="+", command= self.plus_agility_but)
        self.plus_agility.grid(row=5, column=3, ipadx=3, ipady=2, padx=10)
        #Кнопка: минус к параметру ловкости
        self.minus_agility = Button(self, text="-", command = self.minus_agility_but)
        self.minus_agility.grid(row=5, column=4, ipadx=3, ipady=2, padx=10, pady =10)

    def plus_force_but(self):
        while self.point != 0:
            self.force += 1
            self.point -= 1
            self.l_force["text"] = "Сила - " + str(self.force)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break
    def minus_force_but(self):
        while self.force != 0:
            self.force -= 1
            self.point += 1
            self.l_force["text"] = "Сила - " + str(self.force)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break

    def plus_health_but(self):
        while self.point != 0:
            self.health += 1
            self.point -= 1
            self.l_health["text"] = "Здоровье - " + str(self.health)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break
    def minus_health_but(self):
        while self.health != 0:
            self.health -= 1
            self.point += 1
            self.l_health["text"] = "Здоровье - " + str(self.health)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break

    def plus_wisdom_but(self):
        while self.point != 0:
            self.wisdom += 1
            self.point -= 1
            self.l_wisdom["text"] = "Мудрость - " + str(self.wisdom)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break
    def minus_wisdom_but(self):
        while self.wisdom != 0:
            self.wisdom -= 1
            self.point += 1
            self.l_wisdom["text"] = "Мудрость - " + str(self.wisdom)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break

    def plus_agility_but(self):
        while self.point != 0:
            self.agility += 1
            self.point -= 1
            self.l_agility["text"] = "Ловкость - " + str(self.agility)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break
    def minus_agility_but(self):
        while self.agility != 0:
            self.agility -= 1
            self.point += 1
            self.l_agility["text"] = "Ловкость - " + str(self.agility)
            self.l_point_num["text"] = "Осталось очков: " + str(self.point)
            break

root = Tk()
root.title("Генератор персонажей")
root.geometry("250x215")
app = Application(root)
root.mainloop()