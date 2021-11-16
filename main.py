game_list_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''
x_winner = ['X','X','X']
o_winner = ['O','O','O']

# Instructions
print('In order to play the game you need to select the number where to want to put your choice: ')
print('7 8 9')
print('4 5 6')
print('1 2 3')

def display_board(glb): 
    '''glb --> game list board, function that display the current game board'''
    print(f'{glb[6]}|{glb[7]}|{glb[8]}')
    print('-+-+-')
    print(f'{glb[3]}|{glb[4]}|{glb[5]}')
    print('-+-+-')
    print(f'{glb[0]}|{glb[1]}|{glb[2]}')

# validate the winner
def validate_winner(game):

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

while player1 not in ['X', 'O']:
    player1 = input('Player 1 do choose X or O:  ').upper()

    if player1 not in ['X', 'O']:
        print('Wrong choice, please choose X or O')
    
    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'

counter = 0
winner = 'The game is a tie'
while counter < 9:
    move1 = int(input('Player 1 choose your position: ')) -1
    game_list_board[move1] = player1
    print(display_board(game_list_board))
    winner = (validate_winner(game_list_board))
    if winner == 'Player 1 win!!' or winner == 'Player 2 win!!':
        break
    print('\n')
    print('\n')

    move2 = int(input('Player 2 choose your position: ')) -1
    game_list_board[move2] = player2
    print(display_board(game_list_board))
    winner = (validate_winner(game_list_board))
    if winner == 'Player 1 win!!' or winner == 'Player 2 win!!':
        break
    print('\n')
    print('\n')
    counter += 1

print(winner)
