from functions_defs import *

bot_wins = 0
player_wins = 0

play_game = input('Would you like to play rock, paper, scissors with me, best out of three? (y/n): ')

# loop to play the game
while play_game == 'y':
    # loop to run the actual game
    while bot_wins != 2 and player_wins != 2:
        # get player play and bot play
        player_play = input('Enter play: ')
        bot_play = get_play()
        # convert to lower
        player_play = player_play.lower()
        bot_play = bot_play.lower()
        
        # logic for plays and wins
        if player_play == bot_play:
            print('Draw')
        else:
            winner, returned_play = get_win(player_play, bot_play)
            if winner == 'bot':
                print(f'You lost to {returned_play}!')
                bot_wins += 1
            else:
                print(f'You won against {returned_play}!')
                player_wins += 1
    
    # check who won the game
    if bot_wins > player_wins:
        print('You lost, better luck next time!')
    else:
        print('Good job, you won!')

    # reset wins
    bot_wins = 0
    player_wins = 0

    play_game = input('Would you like to play again? (y/n): ')

print('Thank you for playing!')