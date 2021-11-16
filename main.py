game_list_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''
x_winner = ['X','X','X']
o_winner = ['O','O','O']

# Instructions

def instructions():
    print('In order to play the game you need to select the number where to want to put your choice: ')
    print('7|8|9')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('1|2|3')


def display_board(glb): 
    '''glb --> game list board, function that display the current game board'''
    print(f'{glb[6]}|{glb[7]}|{glb[8]}')
    print('-+-+-')
    print(f'{glb[3]}|{glb[4]}|{glb[5]}')
    print('-+-+-')
    print(f'{glb[0]}|{glb[1]}|{glb[2]}')

# validate the winner
def validate_winner(game, player1, player2):

    # Validate if X win
    if game[0:3] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[0::4] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[0:7:3] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[2:7:2] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[3:6] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[6::] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[1:9:3] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[2::3] == x_winner:
        if player1 == 'X':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'

    # Validate if O wins
    if game[0:3] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[0::4] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[0:7:3] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[2:7:2] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[3:6] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[6::] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[1:9:3] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'
    elif game[2::3] == o_winner:
        if player1 == 'O':
            return 'Player 1 win!!'
        else:
            return 'Player 2 win!!'


# choose X or O for the players
def choose_first_player(p1, p2):
    while p1 not in ['X', 'O']:
        print('\n')
        p1 = input('Player 1 choose X or O:  ').upper()

        if p1 not in ['X', 'O']:
            print('Wrong choice, please choose X or O')
        
        if p1 == 'X':
            p2 = 'O'
        elif p1 == 'O':
            p2 = 'X'
    return p1,p2

#Validate if position is already played
def validate_position(index):
    '''Function validate if the position choose by the user is already taken'''
    if game_list_board[index] == 'X' or game_list_board[index] == 'O':
        print('Value already selected')
        return True
    else:
        return False

def clear_all():
    global game_list_board
    global player1
    global player2
    game_list_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1 = ''
    player2 = ''
    return game_list_board, player1, player2

def start_game(game_list_board, player1,player2, x_winner, o_winner):
    keep_playing = True
    while keep_playing:   
        counter = 0
        winner = 'The game is a tie'
        
        instructions()
        player1, player2 = choose_first_player(player1, player2)
        
        while counter < 9:
            canContinue = True
            
            
            while canContinue:
                move1 = 100
                while move1 not in range(0,10):
                    move1 = int(input('Player 1 choose your position: ')) -1                                         
                    if move1 not in range(0,10):
                        print('Value out of the game range, try again')
                        
                canContinue = validate_position(move1)
                game_list_board[move1] = player1
            display_board(game_list_board)
            winner = (validate_winner(game_list_board, player1, player2))
            if winner == 'Player 1 win!!' or winner == 'Player 2 win!!':
                break
            print('\n')
            print('\n')

            canContinue = True
            
            while canContinue:
                move2 = 100
                while move2 not in range(0,10):
                    move2 = int(input('Player 2 choose your position: ')) -1
                    if move2 not in range(0,10):
                        print('Value out of the game range, try again')
                        
                canContinue = validate_position(move2)
                game_list_board[move2] = player2
            display_board(game_list_board)
            winner = (validate_winner(game_list_board, player1, player2))
            if winner == 'Player 1 win!!' or winner == 'Player 2 win!!':
                break
            print('\n')
            print('\n')
            counter += 1
        print(winner)
        
        want_to_play = 'want to play'
        while want_to_play not in ['Y','N']:
            want_to_play = input('Do you want to play again? Y/N: ').upper()
            
            if want_to_play not in ['Y','N']:
                print('Wrong value, choose again.')
                
        if want_to_play == 'Y':
                keep_playing = True
                game_list_board, player1, player2 =  clear_all()
                print('\n' * 100)
        else:
            keep_playing = False

    print('Good bye!')
start_game(game_list_board,player1, player2, x_winner, o_winner)