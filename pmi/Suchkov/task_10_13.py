#Задача 10. 
#Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.

#Сучков Р.А
#03.04.2017

available=30
characteristics = ("Сила", "Здоровье", "Мудрость", "Ловкость")
values=[0, 0, 0, 0]

print(
"""
Добро пожаловать в Генератор персонажей.
Сейчас вы сможете распределенить некоторое количество пунктов между несколькими характеристиками персонажа.
Чтобы добавить один пункт в характеристику, просто напишите название характеристики. Чтобы добавить сразу несколько пунктов, 
поставьте пробел и укажите количество пунктов.

Например:
    "Сила" - добавит один пункт к Силе.
    "Сила 10" - добавит 10 пунктов к Силе.
Чтобы удалить один пункт, поставьте знак минус и напишите название характеристики. 
Чтобы удалить сразу несколько пунктов, поставьте пробел и укажите количество пунктов.

Например:
    "-Здоровье" - уберет один пункт от Здоровья.
    "-Здоровье 10" - уберет 10 пунктов от Здоровья.
"""
)

cmd="start"
while cmd != "":
    print()
    if cmd[0] == "-":
        space_pos = cmd.find(" ")
        if space_pos > 0:
            characteristic = cmd[1:space_pos]
            count = int(cmd[space_pos:])
        else:
            characteristic = cmd[1:]
            count = 1

        if characteristics.count(characteristic) > 0:
            i = characteristics.index(characteristic)
            if values[i] == 0:
                print("Данная характеристика не имеет пунктов.")
                print()
            else:
                if values[i] < count:
                    count = values[i]

                values[i] -= count
                available += count
    else:
        if cmd != "start":
            if available == 0:
                print("Свободных пунктов не осталось. Снимите пункты с других характеристик.")
            else:
                space_pos = cmd.find(" ")
                if space_pos > 0:
                    characteristic = cmd[0:space_pos]
                    count = int(cmd[space_pos:])
                else:
                    characteristic = cmd[0:]
                    count = 1

                if characteristics.count(characteristic) > 0:
                    i = characteristics.index(characteristic)
                    if available < count:
                        count = available
                    values[i] += count
                    available -= count
                    print()

    print("Текущее распределение: ")
    for i, char in enumerate(characteristics):
        print(char + "(" + str(values[i]) + "):" + str("+" * values[i]))
    print("Доступно пунктов: " + str(available))

    cmd=input("\nВведите команду или нажмите Enter для завершения: ")
