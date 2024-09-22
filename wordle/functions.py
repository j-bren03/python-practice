from termcolor import colored

def get_words(words: list):
    file = open("words.txt")
    for line in file.readlines():
        words.append(line.strip())
    file.close()

def get_map(word: str, guessed_word: str):
    # -1: not in word
    # 0: in word, incorrect position
    # 1: in word, correct position
    # default -1
    mapping = [-1, -1, -1, -1, -1]
    
    # Loop for mapping correct characters
    for index, (guessed_char, actual_char) in enumerate(zip(guessed_word, word)):
        if guessed_char == actual_char:
            mapping[index] = 1
            # Replace the character with an empty placeholder
            word = word.replace(guessed_char, "-", 1)

    # Loop for mapping incorrect position characters
    for index, guessed_char in enumerate(guessed_word):
        if guessed_char in word and mapping[index] == -1:
            mapping[index] = 0
            # Replace the character with an empty placeholder
            # Gets rid of excessive duplicates
            # If the character of the guessed word is in the actual word, replace the first occurrence
            word = word.replace(guessed_char, "-", 1)

    return mapping

# Created because the find method was not working for my map method
def check_word(word: str, search_letter: str):
    for letter in word:
        if letter == search_letter:
            return True
    return False

def print_color_map(word: str, mapping: list):
    for letter, map_value in zip(word, mapping):
        # Correct letter, green
        if(map_value == 1):
            print(colored(letter, "green"), end="")
        # Wrong position, yellow
        elif(map_value == 0):
            print(colored(letter, "yellow"), end="")
        # Incorrect letter
        else:
            print(colored(letter, "red"), end="")

    print()