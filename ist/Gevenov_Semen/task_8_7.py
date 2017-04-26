# Задача 8. Вариант 7.
# Доработайте   игру    "Анаграммы" (см.    М.Доусон    Программируем   на  Python. Гл.4)

# Gevenov S. A.
# 16.04.2017

import random

WORDS = ("python", "anagram", "easy",
         "Hard", "answer", "glass-holder")

word = random.choice(WORDS)

correct = word

i_dont_know = "i dont know"
hint = word[0] + word[1] + word[2]

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

scores = 10

print(
    """

                                           Welcome to the game 'Anagrams'!
                        It is necessary to rearrange the letters so as to obtain a meaningful word.
                               If you need help, enter: "I do not know."
           But remember, if you do not use a hint, the number of points earned will be more.
                            (To exit, press Enter, without introducing its version.)
    """
)
print("Here is an anagram: ", jumble)
guess = input("\nTry to guess the original word: ")
while guess != "" and guess != correct:
    if guess != correct and not guess == i_dont_know:
        print("Unfortunately, you are wrong.")
    if guess == i_dont_know:
        scores -= 5
        print("\nHint! The first three letters of the word!", hint)
    guess = input("Try to guess the original word: ")
    if guess == correct:
        print("Yes exactly! You guessed!\n")

if scores < 0:
    scores = 0
print("Thanks for the game! You scores: ", scores)
input("\n\nPress Enter...")
