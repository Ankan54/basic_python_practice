"""
Tic-Tac-Toe game with Computer player having easy and hard difficulty
"""
import math
import time

from player import ComputerPlayer,HumanPlayer, BossPlayer

class TicTacToe:
    def __init__(self):
        self.board= [' ' for _ in range(9)]
        self.current_winner= None  # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+ ' |')

    @staticmethod
    def print_board_num():
        number_board= [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')

    def available_moves(self):
        # moves=[]
        # for (i,spot) in enumerate(self.board):
        #     # [X,X,O] ---> [(0,X), (1,X), (2,O)]
        #     if spot== " ":
        #         moves.append(i)  #alternative below

        return [i for i,spot in enumerate(self.board) if spot==" "]

    def empty_squares(self):
        return ' ' in self.board  # returns boolean

    def empty_square_count(self):
        return self.board.count(' ')

    def make_move(self, move,letter):
        if self.board[move]==" ":
            self.board[move]= letter
            if self.check_winner(move,letter):
                self.current_winner= letter
            return True
        return False

    def check_winner(self,move,letter):
        row_index= move // 3
        row= self.board[row_index*3 : (row_index+1)*3]
        if all([spot == letter for spot in row]): # check row wise
            return True
        
        col_index= move % 3
        column= [self.board[col_index+i*3] for i in range(3)]  
        if all(spot==letter for spot in column):  #check column wise
            return True
        
        if move%2 ==0:   #check diagonal wise
            diagonal1= [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play_game(game,x_player, o_player, print_game=True):
    if print_game:
        game.print_board_num()

    letter= 'X'  #starting letter (let)

    while game.empty_squares():
        if letter=="O":
            move= o_player.get_move(game)
        else:
            move= x_player.get_move(game)
        
        if game.make_move(move,letter):
            if print_game:
                game.print_board()
                print("\n")
        
        if game.current_winner:
            print(('Player' if letter=="X" else 'Computer') + " wins!")
            return letter

        letter= "O" if letter=="X" else "X"
    
    if print_game:
        print("It's a tie!")
        return None

if __name__== "__main__":
    print("****************** Welcome to Tic-Tac-Toe game ******************")
    while True:
        level= input("Choose your level: [E] for Easy, [H] for Hard\n")
        if level.upper() not in ['H','E']:
            print('Invalid input. Try again')
            continue 
        break
    x_player= HumanPlayer('X')
    o_player= BossPlayer('O') if level.upper()== 'H' else ComputerPlayer('O')
    t= TicTacToe()
    play_game(t,x_player,o_player)

