#!/usr/bin/env python

"""TicTacToe.py: Tic-Tac-Toe game application 2 Player"""
#  @author : Ankan Bera
# ---------------------------------------------------
import time
import random
def main_function():
    board= ["1","2","3","4","5","6","7","8","9"]
    first_user = input("Enter player 1 name: ")
    second_user = input("Enter player 2 name: ")
    print("Assigning mark to players...")
    time.sleep(1)
    choice = random.choice([first_user, second_user])
    if choice == first_user:
        first_mark = "X"
        second_mark = "O"
    else:
        first_mark = "O"
        second_mark = "X"
    print("{}: {}, {}: {}".format(first_user, first_mark, second_user, second_mark))
    print("Starting Game...")
    print("Input block numbers as shown in board")
    time.sleep(1)
    #  start game
    play_game(first_user,first_mark,second_user,second_mark,board)
    display_board(board)

def play_game(first_user,first_mark,second_user,second_mark,board):
    turn=True
    count =0
    next = True
    while next:
        display_board(board)
        if turn:
            place = input("{}'s turn: ".format(first_user))
            mark = first_mark
        else:
            place = input("{}'s turn: ".format(second_user))
            mark= second_mark
        if not check_input(board,place):
            print("Invalid input. Try again")
            continue
        count +=1
        board[int(place)-1]= mark
        if check_pattern(board):
            next = False
        else:
            turn = not turn
            if count ==9:
                print("Match drawn")
                return True
    if turn:
        print("{} has won".format(first_user))
    else:
        print("{} has won".format(second_user))
    return True

def check_pattern(board):
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        return True
    return False

def check_horizontal(board):
    if board[0]== board[1] and board[1]== board[2]:
        return True
    elif board[3]== board[4] and board[4]== board[5]:
        return True
    elif board[6] == board[7] and board[7] == board[8]:
        return True
    return False

def check_vertical(board):
    if board[0]== board[3] and board[3]== board[6]:
        return True
    elif board[1]== board[4] and board[4]== board[7]:
        return True
    elif board[2]== board[5] and board[5]== board[8]:
        return True
    return False

def check_diagonal(board):
     if board[0]== board[4] and board[4]== board[8]:
        return True
     elif board[2]== board[4] and board[4]== board[6]:
        return True
     return False

def check_input(board,place):
    if int(place) not in range(1,10):
        return False
    if board[int(place)-1] in  ["X","O"]:
        return False
    return True

def display_board(board):
    print("--------")
    for mark in range(len(board)):
        if mark in [2,5,8]:
            print(board[mark], end=" ")
            print("\n--------")
        else:
            print(board[mark], end="  ")

main_function()
