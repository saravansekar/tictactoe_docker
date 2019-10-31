print('Welcome to Tic Tac Toe')

print('Sample Board Enter the number you want your X or O to be positioned')
print('7'+'|'+'8'+'|'+'9')
print('-|-|-')
print('4'+'|'+'5'+'|'+'6')
print('-|-|-')
print('1'+'|'+'2'+'|'+'3')

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Please enter your position 1-9 : ')
    return int(position)

def space_check(board, position):
    return board[position] == ' '

def board_full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def displayBoard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def playerSym():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
     marker = input('Player 1 please select X or O : ')
    
    player1 = marker
    if(player1 == 'X'):
     player2 = 'O'
    else: 
     player2 = 'X'
    return (player1,player2)

def playerInput(board, marker,position):
        board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


while True:
    # Reset the board
    theBoard = [' '] * 10
    player1sym , player2sym = playerSym()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            displayBoard(theBoard)
            position = player_choice(theBoard)
            playerInput(theBoard, player1sym, position)

            if win_check(theBoard, player1sym):
                displayBoard(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if board_full_check(theBoard):
                    displayBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            displayBoard(theBoard)
            position = player_choice(theBoard)
            playerInput(theBoard, player2sym, position)

            if win_check(theBoard, player2sym):
                displayBoard(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if board_full_check(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

