"""
Simple command-line implementation of minesweeper
Author: Ankan Bera

step 1: create the board and plant the bombs
step 2: show user the board and ask for input
step 3a: if location is a bomb, game over
step 3b: if not a bomb, proceed recursively until each square is next to a bomb
step 4: repeat step 2 and 3, until no more position left to choose ---> Victory 
"""
import random
import re

class Board:
    def __init__(self,size, bombs):
        self.size= size
        self.bombs= bombs

        self.dug= set()   # will have (row,col) tuples, to store the used positions

        self.board= self.make_new_board()
        self.assign_values_to_board()

    def make_new_board(self):
        # create a list of list with None value. eg: [[None,None], [None,None], ......]
        board = [[None for _ in range(self.size)] for _ in range(self.size)]

        bombs_planted= 0
        while bombs_planted < self.bombs:
            loc= random.randint(0,self.size**2 - 1)
            row= loc // self.size
            col= loc % self.size

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted+=1
        return board

    def assign_values_to_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c]== "*":
                    continue
                self.board[r][c]= self.get_neighbouring_bombs(r,c)
    
    def __str__(self):
        # print the board
        visible_board= [[None for _ in range(self.size)] for _ in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                if (row,col) in self.dug:
                    visible_board[row][col]= str(self.board[row][col])
                else:
                    visible_board[row][col]= " "
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

    def dig(self,row,col):
        self.dug.add((row,col))

        if self.board[row][col]== "*":
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0,row-1), min(self.size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c) #recursive

        return True
    
    def get_neighbouring_bombs(self,row,col):
        # all the neighbouring positions as below:
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)       
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        num_bombs=0    # min max is to check for out of bound positions
        for r in range(max(0,row-1), min(self.size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.size-1,col+1)+1):
                if r==row and c==col:
                    continue
                if self.board[r][c] == "*":
                    num_bombs+=1
        return num_bombs

        
def play(size,bombs):
    #follow the steps from header
    board= Board(size,bombs)
    safe= True
    while len(board.dug) < (board.size**2 - bombs):
        print(board)
        user_input= re.split(",(\\s)*",input("Select a place to dig. eg:(row,col) : "))
        try:
            row,col= int(user_input[0]), int(user_input[-1])
        except Exception as E:
            print("Invalid input. Reason: {}".format(E))
            continue

        if row<0 or row>=board.size or col<0 or col>= board.size:
            print("Invalid location! Try again")
            continue

        safe= board.dig(row,col)

        if not safe:
            break
        
    if safe:
        print("You have Won!")
    else:
        print('Game Over')
        board.dug = [(r,c) for r in range(board.size) for c in range(board.size)]
        print(board)


if __name__ == "__main__":
    play(10,10)
