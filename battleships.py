import random

board=[]

for x in range(0,5):
    board.append(["O"]*5)


def print_board(board):
    for row in board:
        print("  ".join(row))

print_board(board)


def random_row(board):
    return random.randint(1, len(board))

def random_col(board):
    return random.randint(1, len(board))

ship_row, ship_collum = random_row(board), random_col(board)
print(ship_row)
print(ship_collum)


for turn in range(1, 5):
    guess_row = int(input('guess a row: '))
    guess_collum = int(input('guess a collum: '))
    if guess_row == ship_row and guess_collum == ship_collum:
        print('HIT!!\nyou won!')
        break
    else:
        if guess_row - 1 not in range(0, 5) or guess_collum - 1 not in range(0, 5):
            print("Oops, that's not even in the ocean.")
            print('please guess again')
        elif board[guess_row - 1][guess_collum - 1] == 'X':
            print("You guessed that one already.")
            print('please guess again')
        else:
            print('you missed! ')
            board[guess_row - 1][guess_collum - 1] = 'X'
            print_board(board)
            turn += 1
        if turn < 5:
            print("Turn:", turn)
    if turn == 5:
        print('you lost')