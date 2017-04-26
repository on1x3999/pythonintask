#Задача 8.
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#Popadin N.V.
#02.04.2017

import random
WORDS = ("ночь", "кочка", "любовь", "лето", "чувства","сериал","ненависть","зависть","симпатия","учеба","кот","звезда","гнездо","еда","кофе","семья","счастье")  
def createJumbled(word):  
    jumble ="" 
    while word: 
        position = random.randrange(len(word))  
        jumble += word[position] 
        word = word[:position] + word[(position + 1):] 
    return jumble  
print(  
"""  
\t\t\tПривет! Добро пожаловать в "Анаграммы"!  
\n\t\tПравила просты! Чем меньше подсказок ты используешь, тем больше баллов получишь! 
""" 
)  
score = 5000 
helpcount = 0 
totalGame = 0 
playMore = "yes"  
while playMore == "yes":  
    word = random.choice(WORDS)  
    index = WORDS.index(word) 
    correct = word  
    jumble = createJumbled(word) 
    print("Анаграмма: ", jumble) 
    print("\nЕсли нужна подсказка, введи 'yes'. Если нет - 'no'.") 
    help = input("Будешь брать подсказку?: ")  
    if help == "yes":  
        hint = word[0] + word [1] 
        print(hint)  
        helpcount += 1 
        guess = input("\nТвой ответ: ") 
    elif help == "no": 
        guess = input("\nТвой ответ: ")  
    while guess != correct and guess != "": 
        print("Неверно!") 
        print("\nЕсли нужна подсказка, введи 'yes'. Если нет - 'no'.")  
        help = input("Будешь брать подсказку?: ") 
        if help == "yes": 
            hint2 = HINTS[index] 
            print(hint2) 
            helpcount += 2 
        guess = input("Твой ответ: ") 
    if guess == correct: 
        print("Верно! Ты угадал!") 
    if helpcount == 0: 
        print("Ты не использовал ни единой подсказки, молодец!\n") 
    totalGame += 1 
    print("\nЧтобы продолжить играть, набери 'yes'.") 
    playMore = input("Ты хочешь сыграть еще?: ") 
print("\n") 
print("Игр сыграно: ",totalGame) 
print("Ты использовал подсказок: ",helpcount) 
print("Твой счёт: ",(score-(totalGame*helpcount)))   
input("\nНажми Enter, чтобы выйти") 
