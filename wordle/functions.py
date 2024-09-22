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
    mapping = []
    
    for guessed_char, actual_char in zip(guessed_word, word):
        # Character is in word
        if guessed_char == actual_char:
            mapping.append(1)
        # Character is in word, wrong position
        elif (guessed_char != actual_char) and check_word(word, guessed_char):
            mapping.append(0)
        # Character is not in word
        else:
            mapping.append(-1)

    # Handle excessive duplicates
    for index in range(len(mapping)):
        # Current letter to check and its letter count
        curr_letter = guessed_word[index]
        letter_count = word.count(curr_letter)

        # If letter is a duplicate
        if mapping[index] == 0 and letter_count >= 1:
            for letter_index, letter in enumerate(guessed_word):
                # Duplicate letter matches a correctly mapped letter
                if letter == curr_letter and mapping[letter_index] == 1:
                    letter_count -= 1
            
            # Letter is an excessive duplicate
            if letter_count == 0:
                mapping[index] = -1

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