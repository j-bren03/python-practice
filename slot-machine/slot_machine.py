import slot_functions

# Create slot machine
slot_machine = slot_functions.create_slot_machine(3,7)

balance = 0
playing = 'y'
bet = 0
amount_won = 0
num_of_sevens = 0

# Get playing balance
balance = int(input('Enter a balance to play with ($1 minimum): '))
while balance < 1:
    balance = int(input('Enter a valid balance: '))

while playing != 'n' and balance > 0:
    # Display balance
    print(f'\nCurrent balance: ${balance:.2f}')

    # Get user bet
    bet = int(input('Enter a bet amount ($1 minimum): '))
    while bet < 1 or bet > balance:
        bet = int(input('Enter a valid bet: '))

    # Spin the slot machine
    slot_results = slot_functions.spin_slot_machine(slot_machine)
    print(f'\n{slot_results}')

    # Find the number of 7's in result
    for i in range(3):
        if slot_results[i] == 7:
            num_of_sevens += 1

    # Calculate amount won
    if num_of_sevens == 1:
        print(f'You won ${bet * 1}!')
        amount_won = amount_won - bet + (bet * 1)
        balance += bet * 1
    elif num_of_sevens == 2:
        print(f'You won ${bet * 10}!')
        amount_won = amount_won - bet + (bet * 10)
        balance += bet * 10
    elif num_of_sevens == 3:
        print(f'You won ${bet * 100}!')
        amount_won = amount_won - bet + (bet * 100)
        balance += bet * 100
    else:
        print('You didn\'t win anything!')
        amount_won -= bet

    # Update balance and number of 7s
    balance -= bet
    num_of_sevens = 0

    # Ask to play again
    if balance > 0:
        playing = input('Would you like to play again (y/n)? ')
        while playing not in ['y', 'n']:
            playing = input('Enter \'y\' or \'n\': ')
    else:
        print('You don\'t have enough to play!')

# Print stats
print()
slot_functions.print_stats(balance, amount_won)