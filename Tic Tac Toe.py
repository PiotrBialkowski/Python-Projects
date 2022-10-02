import random


def show_board(board):
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')       # Board is like a numpad
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')

def player_marker():
    marker = str(input("Player 1 do you want to be 'X' or 'O'? "))
    while marker.upper() not in ['X','O']:
        marker = str(input("Do you want to be 'X' or 'O'? "))
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,position,marker):
    board[position] = marker

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
    return position
    
def space_check(board,position):
    if board[position] == ' ':
        return True

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def win_check(board,marker):
    return (board[7] == board[8] == board[9] == marker) or \
    (board[4] == board[5] == board[6] == marker) or \
    (board[1] == board[2] == board[3] == marker) or \
    (board[1] == board[4] == board[7] == marker) or \
    (board[2] == board[5] == board[8] == marker) or \
    (board[3] == board[6] == board[9] == marker) or \
    (board[7] == board[5] == board[3] == marker) or \
    (board[1] == board[5] == board[9] == marker)        # RETURN TRUE IF SOMEONE WINS

def replay():
    return input("Do you want to play again? Y/N ").upper().startswith('Y')


def first_player():

    flip = random.randint(1,2)

    if flip == 1:
        return("Player 1")
    else:
        return("Player 2")



game_on = True

while True:

    board = [' '] * 10
    player1,player2 = player_marker()
    turn = first_player()
    print(turn + ' will start!')

    play_game = str(input("Do you want to play? Y/N ".upper()))

    if play_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on == True:

        if turn == 'Player 1':

            show_board(board)
            position = player_choice(board)
            place_marker(board,position,player1)

            if win_check(board,player1):
                show_board(board)
                print('Player 1 wins the game!!!')
                game_on = False

            else:
                if full_board_check(board):
                    show_board(board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            show_board(board)
            position = player_choice(board)
            place_marker(board,position,player2)

            if win_check(board,player2):
                show_board(board)
                print('Player 2 wins the game!!!')
                game_on = False

            else:
                if full_board_check(board):
                    show_board(board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break






