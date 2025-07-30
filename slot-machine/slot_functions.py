import random

def create_slot_machine(slots, num_on_slots):
    # Create slot machine list
    slot_machine = []

    for i in range (slots):
        # Create empty lists for each slot wheel
        slot_machine.append([])
        for j in range(1, num_on_slots + 1):
            # Put the values in each slot wheel
            slot_machine[i].append(j)

    # Return slot machine list
    return slot_machine

def spin_slot_machine(slot_machine):
    # Empty list for each wheel result
    spin_result = []

    for i in slot_machine:
        # Get a random value for each individual slot wheel
        spin_result.append(random.choice(i))

    # Return the spin result
    return spin_result

def print_stats(balance, amount_won):
    print(f'You ended with a balance of ${balance:.2f}')
    if amount_won < 0:
        print(f'You lost ${-amount_won:.2f}, sorry!')
    elif amount_won == 0:
        print('You broke even!')
    else:
        print(f'You won ${amount_won:.2f}, congratulations!')
    print('Thank you for playing!')