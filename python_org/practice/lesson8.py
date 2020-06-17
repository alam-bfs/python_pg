def play_game():
    print('''Please pick one:
                rock
                scissors
                paper''')

    while True:
        game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
        player_a = str(input('Player A: '))
        player_b = str(input('Player B: '))

        a = game_dict.get(player_a)
        b = game_dict.get(player_b)

        dif = a - b

        if dif in [-1, -2]:
            print('Player A is the Winner')

            if str(input('do you want to continue? ')) == 'yes':
                continue
            else:
                print('Game Over !!!')
                break

        elif dif in [2, 1]:
            print('Player B is the Winner')
            if str(input('do you want to continue? ')) == 'yes':
                continue
            else:
                print('Game Over !!!')
                break
        else:
            print('Draw. Please continue')
            print('')


if __name__ == '__main__':
    play_game()
