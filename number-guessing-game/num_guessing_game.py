# Jeremy Brensinger
import random

random_number = random.randint(1,100)
times_guessed = 0
guessed = False

# Prompt
print('Enter a number between 1 and 100, you get five guesses!')

# Game functionality
while (times_guessed < 5) and (guessed == False):
    guess = int(input('Enter number: '))

    if guess == random_number:
        guessed = True
    elif guess < random_number:
        print('Higher!')
    else:
        print('Lower!')

    times_guessed += 1

# Win or lose output
if guessed == True:
    print(f'You guessed the number! The number is {random_number}!')
else:
    print(f'Sorry, you didn\'t guees the number! The number is {random_number}!')