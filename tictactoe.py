from tabulate import tabulate
import os
import random
from termcolor import colored

board_items = [['*', '*', '*'],
               ['*', '*', '*'],
               ['*', '*', '*']]
index_map = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}
pos_list = []


def display_board(board, selection=''):
    os.system('clear')
    if selection != '':
        for i in selection:
            index = index_map[int(i)]
            board_items[index[0]][index[1]] = colored(board_items[index[0]][index[1]], 'red')
        print(tabulate(board, tablefmt='simple_grid'))
    else:
        print(tabulate(board, tablefmt='simple_grid'))


def update_board(pos, value):
    index = index_map[pos]
    board_items[index[0]][index[1]] = value


def validate_game(mark):
    if board_items[0][0] == mark and board_items[1][0] == mark and board_items[2][0] == mark:
        return True, '147'
    elif board_items[0][1] == mark and board_items[1][1] == mark and board_items[2][1] == mark:
        return True, '258'
    elif board_items[0][2] == mark and board_items[1][2] == mark and board_items[2][2] == mark:
        return True, '369'
    elif board_items[0] == [mark] * 3:
        return True, '123'
    elif board_items[1] == [mark] * 3:
        return True, '456'
    elif board_items[2] == [mark] * 3:
        return True, '789'
    elif board_items[0][0] == mark and board_items[1][1] == mark and board_items[2][2] == mark:
        return True, '159'
    elif board_items[0][2] == mark and board_items[1][1] == mark and board_items[2][0] == mark:
        return True, '357'
    else:
        return False, ''


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Chose X or O: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_choice(turn):
    choice = 0
    while (choice not in list(range(1, 10))) or (choice in pos_list):
        choice = int(input(f'{turn} Chose a position (1-9): '))
    pos_list.append(choice)
    pos_list.sort()
    return choice


def replay():
    choice = input('Play again? Enter Yes or No: ')
    return choice.lower() == 'yes'


print('Welcom to Tic Tac Toe')

while True:
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first')
    play_game = input('ready to play? y or n?: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board_items)
            position = player_choice(turn)
            update_board(position, player1_marker)
            validate, raw = validate_game(player1_marker)
            if validate:
                display_board(board_items, raw)
                print('Player1 Won')
                game_on = False
            else:
                if pos_list == list(range(1, 10)):
                    display_board(board_items)
                    print('Its a Tie')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(board_items)
            position = player_choice(turn)
            update_board(position, player2_marker)
            validate, raw = validate_game(player2_marker)
            if validate:
                display_board(board_items, raw)
                print('Player2 Won')
                game_on = False
            else:
                if pos_list == list(range(1, 10)):
                    display_board(board_items)
                    print('Its a Tie')
                    game_on = False
                else:
                    turn = 'Player 1'
    if replay():
        board_items = [['*', '*', '*'],
                       ['*', '*', '*'],
                       ['*', '*', '*']]
        pos_list = []
    else:
        os.system('clear')
        break
