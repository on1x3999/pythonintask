size = 3
from tkinter import *
from tkinter import messagebox
arrBut =[[]]
lastTurn = (size-1,size-1)
closeFlag = "no"
def diffWin():    
    rootAsk = Tk()
    rootAsk.title("Уровень сложности")
    rootAsk.minsize(247, 35)
    w = 247
    h = 35
    ws = rootAsk.winfo_screenwidth()
    hs = rootAsk.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    rootAsk.geometry('%dx%d+%d+%d' % (w, h, x, y))
    rootAsk.resizable(width=False, height=False)
    frame1 = Frame(rootAsk)
    frame1.grid()
    diff = True   
    def diffChoise(choise):
        global diff
        def asf():
            infoBox = messagebox.showinfo('Крестики-Нолики','Вы играете за крестики\nУдачи!')
        if choise == True: diff = True
        else: diff = False
        asf()
        rootAsk.destroy()    
    diffButton1 = Button(frame1, text="Сложно", width = 19, height = 2, command = lambda : diffChoise(False))
    diffButton2 = Button(frame1, text="Невозможно", width = 19, height = 2, command = lambda : diffChoise(True) )
    diffButton1.grid(row=5, column=1) 
    diffButton2.grid(row=5, column=4)
    rootAsk.mainloop()
diffWin()

root = Tk()
root.title("Крестики-Нолики")
root.minsize(210, 245)
w = 210
h =245
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
frame = Frame(root)
frame.grid()
def winChance():
    summ = 0
    cur_j = 0
    cur_i = 0
    for row in range(size):
        for col in range(size):
            if arrBut[row][col]["text"] == "O": summ+=1
            if arrBut[row][col]["text"] == " ":
                cur_j = col
        if summ == size - 1 and arrBut[row][cur_j]["text"] == " ":
            placeTik(row, cur_j)
            colorWin(row, "row")
            
            return True
        summ = 0
    for col in range(size):
        for row in range(size):
            if arrBut[row][col]["text"] == "O": summ+=1
            if arrBut[row][col]["text"] == " ":
                cur_i = row
        if summ == size - 1 and arrBut[cur_i][col]["text"] == " ":
            placeTik(cur_i, col)
            colorWin(col, "col")
            return True
        summ = 0
    for i in range(size):
        if arrBut[i][i]["text"] == "O": summ+=1
        if arrBut[i][i]["text"] == " ":
            cur_i = i
        if summ == size - 1 and arrBut[cur_i][cur_i]["text"] == " ":
            placeTik(cur_i, cur_i)
            colorWin(i, "gd")
            return True
    summ = 0
    for i in range(size):
        if arrBut[size -1 - i][i]["text"] == "O": summ+=1
        if arrBut[size -1 - i][i]["text"] == " ":
            cur_i = i
        if summ == size - 1 and arrBut[size - 1 - cur_i][cur_i]["text"] == " ":
            placeTik(size - 1 - cur_i, cur_i)
            colorWin(cur_i, "pd")
            return True
    summ = 0
def loseChance():
    summ = 0
    cur_j = 0
    cur_i = 0
    for row in range(size):
        for col in range(size):
            if arrBut[row][col]["text"] == "X": summ+=1
            if arrBut[row][col]["text"] == " ":
                cur_j = col
        if summ == size - 1 and arrBut[row][cur_j]["text"] == " ":
            placeTik(row, cur_j)
            return True
        summ = 0
    for col in range(size):
        for row in range(size):
            if arrBut[row][col]["text"] == "X": summ+=1
            if arrBut[row][col]["text"] == " ":
                cur_i = row
        if summ == size - 1 and arrBut[cur_i][col]["text"] == " ":
            placeTik(cur_i, col)
            return True
        summ = 0
    for i in range(size):
        if arrBut[i][i]["text"] == "X": summ+=1
        if arrBut[i][i]["text"] == " ":
            cur_i = i
        if summ == size - 1 and arrBut[cur_i][cur_i]["text"] == " ":
            placeTik(cur_i, cur_i)
            return True
        summ = 0
    for i in range(size):
        if arrBut[size -1 - i][i]["text"] == "X": summ+=1
        if arrBut[size -1 - i][i]["text"] == " ":
            cur_i = i
        if summ == size - 1 and arrBut[size - 1 - cur_i][cur_i]["text"] == " ":
            placeTik(size -1 - i, i)
            return True
        summ = 0
def colorWin(workNum, dir):
    if dir == "row":
        for i in range(size): arrBut[workNum][i]["bg"] = "#ff8888"
        infoBox = messagebox.showinfo('Крестики-Нолики', "\"" + arrBut[workNum][i]["text"] + "\"" + ' победили!')
    if dir == "col":
        for i in range(size): arrBut[i][workNum]["bg"] = "#ff8888"
        infoBox = messagebox.showinfo('Крестики-Нолики', "\"" + arrBut[i][workNum]["text"] + "\"" + ' победили!')
    if dir == "gd":
        for i in range(size): arrBut[i][i]["bg"] = "#ff8888"
        infoBox = messagebox.showinfo('Крестики-Нолики', "\"" + arrBut[i][i]["text"] + "\"" + ' победили!')
    if dir == "pd":
        for i in range(size): arrBut[size - 1 - i][i]["bg"] = "#ff8888"
        infoBox = messagebox.showinfo('Крестики-Нолики', "\"" + arrBut[size - 1 - i][i]["text"] + "\"" + ' победили!')
    for i in range(size):       
        for j in range(size): arrBut[i][j]["state"] = DISABLED
def randPlace():    
    cur_i=0
    cur_j=0
    for i in range(size):
        for j in range(size):
            if arrBut[i][j]["text"] == " ":
                if abs(i-lastTurn[0])>=cur_i: cur_i = i
                if abs(j-lastTurn[1])>=cur_j: cur_j = j
                placeTik(cur_i,cur_j)
                return
def intelPlace():
    cur_i=0
    cur_j=0
    max = 0
    i = lastTurn[0]
    j = lastTurn[1]
    for row in range(size):
        for col in range(size):
            if arrBut[row][col]["text"] == " ":
                max+=1
    if max == 0: return False 
    if arrBut[1][1]["text"] == "X": 
        if arrBut[0][0]["text"] == " ":
            placeTik(0,0)
            return True
        if arrBut[size-1][0]["text"] == " ":
            placeTik(size-1,0)
            return True
        if arrBut[0][size-1]["text"] == " ":
            placeTik(0,size-1)
            return True
        if arrBut[size-1][size-1]["text"] == " ":
            placeTik(size-1, size-1)
            return True
    if arrBut[1][1]["text"] == " ":
        placeTik(1,1)
        return True
    if (arrBut[0][0]["text"] == "X") or (arrBut[size-1][0]["text"] == "X") or (arrBut[0][size-1]["text"] == "X") or (arrBut[size-1][size-1]["text"] == "X"):
        
        if arrBut[0][0]["text"] == " ":
            placeTik(0,0)
            print("3")
            return True
        if arrBut[size-1][0]["text"] == " ":
            placeTik(size-1,0)
            return True
        if arrBut[0][size-1]["text"] == " ":
            placeTik(0,size-1)
            return True
        if arrBut[size-1][size-1]["text"] == " ":
            placeTik(size-1, size-1)
            return True 
    for row in range(size):
        for col in range(size):
            if arrBut[row][col]["text"] == " " and abs(row-i) + abs(col-j) >= max:
                max = abs(row-i) + abs(col-j)
                cur_i=row
                cur_j=col
    placeTik(cur_i, cur_j)
    return True            
def crossWin():
    summ = 0
    cur_j = 0
    cur_i = 0
    for row in range(size):
        for col in range(size):
            if arrBut[row][col]["text"] == "X": summ+=1
        if summ == size:
            colorWin(row, "row")
            return True
        summ = 0
    for col in range(size):
        for row in range(size):
            if arrBut[row][col]["text"] == "X": summ+=1
        if summ == size:
            colorWin(col, "col")
            return True
        summ = 0
    for i in range(size):
        if arrBut[i][i]["text"] == "X": summ+=1
        if summ == size:
            colorWin(i, "gd")
            return True
    summ = 0
    for i in range(size):
        if arrBut[size -1 - i][i]["text"] == "X": summ+=1
        if summ == size:
            colorWin(i, "pd")
            return True
    summ = 0        
def placeTik(row, col): 
    arrBut[row][col]["text"] = "O"    
def change(a,b):
    print("1")
    if arrBut[a][b]["text"] == " ":
        arrBut[a][b]["text"]="X"
        lastTurn = (a, b)
        if crossWin() != True:
            if winChance() != True: 
                if loseChance() != True:
                    if diff == True: intelPlace()
                    else: randPlace()
    return arrBut
def func(a,b):
    return Button(frame, text=" ", bg="white", font=("Helvetica", 26), width = 3, height = 1, command= lambda : change(a,b))
def againAsk():
    closeFlag =  messagebox.askquestion("Сыграть снова?", "Хотите попытаться еще раз?")
    if closeFlag == "yes":
        for row in range(size):
            for col in range(size):
                arrBut[row][col]["state"] = NORMAL
                arrBut[row][col]["text"] = " "
                arrBut[row][col]["bg"] = "white"
def createBoard():
    arrBut = [[" "]*size for b in range(size)]
    for a in range(size):
        for b in range(size):
            arrBut[a][b] = func(a,b)
            arrBut[a][b].grid(row=a, column=b)    
    againButt = Button(frame, text="Заново", width = 10, height = 2, command = againAsk)
    againButt.grid(row = size + 1, column = 0)
    levelButt = Button(frame, text="Сложность", width = 10, height = 2, command = diffWin)
    levelButt.grid(row = size + 1, column = size-1)
    return arrBut

arrBut = createBoard()
root.mainloop()
