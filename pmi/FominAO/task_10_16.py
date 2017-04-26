# Задача 10. Вариант 16.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
# Фомин Александр Олегович
# 04.04.2017
fstats = 30
strenth = 0
health = 0
intellect = 0
agility = 0
from tkinter import *
root = Tk()
root.title("RPG Simulator")
root.minsize(110, 120)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()

fst = Label(frame, text="Free stats: ")
fst.grid(row=1, column=0)
freestats = Label(frame, text=fstats)
freestats.grid(row=1, column=1)


def inc(lableName):
    global fstats
    if fstats < 1: return
    fstats = fstats - 1
    x = lableName.cget("text") + 1;
    lableName.configure(text=x)
    freestats.configure(text=fstats)

def dec(field, lableName):
    x = lableName.cget("text") - 1;
    if x < 0: return
    lableName.configure(text=x)
    global fstats
    fstats = fstats + 1
    freestats.configure(text=fstats)

def createRow(textField, _row, opt):
    str_lab = Label(frame, text=textField)
    str_lab.grid(row=_row, column=0)
    strh = Label(frame, text=opt)
    strh.grid(row=_row, column=1)
    str_but = Button(frame, width=2, text="+", command=lambda: inc(strh))
    str_but.grid(row=_row, column=2)
    str_but1 = Button(frame, width=2, text="-", command=lambda: dec(opt, strh))
    str_but1.grid(row=_row, column=3)
createRow("Strenth", 2, strenth)
createRow("Intellect", 3, intellect)
createRow("Health", 4, health)
createRow("Agility", 5, agility)

root.mainloop()