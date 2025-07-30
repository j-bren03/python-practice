import random

def get_play():
    random_number = random.randint(1,3)

    if random_number == 1:
        return 'rock'
    elif random_number == 2:
        return 'paper'
    else:
        return 'scissors'
    
def get_win(player_play, bot_play):
    if player_play == 'rock' and bot_play == 'paper':
        return 'bot', bot_play
    elif player_play == 'paper' and bot_play == 'scissors':
        return 'bot', bot_play
    elif player_play == 'scissors' and bot_play == 'rock':
        return 'bot', bot_play
    elif player_play == 'paper' and bot_play == 'rock':
        return 'player', bot_play
    elif player_play == 'scissors' and bot_play == 'paper':
        return 'player', bot_play
    else:
        return 'player', bot_play
    
if __name__ == '__main__':
    print('test')