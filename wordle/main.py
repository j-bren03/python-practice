from functions import *
import random
import os

guessed = False
playing = True
os.system("color")

words = []
get_words(words)

while playing:
    guesses = 0
    word = words[random.randint(0, len(words))]

    while guesses < 6 and guessed == False:
        guessed_word = input("")

        color_map = get_map(word, guessed_word.upper())
        print_color_map(guessed_word.upper(), color_map)

        if(sum(color_map) == 5):
            guessed = True

        guesses += 1

    print(f"The word was {word}!", end="\n\n")
    user_response = input("Would you like to play again (y/n): ")
    if(user_response == 'n'):
        playing = False
    os.system("cls")