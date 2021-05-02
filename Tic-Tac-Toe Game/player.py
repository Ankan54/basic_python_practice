"""
player classes for the game
"""
import math
import time
import random

class Player:   #base player class
    def __init__(self, letter):
        self.letter= letter    #letter can be X or O

    def get_move(self,game):
        pass


class ComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        print("Computer's turn")
        time.sleep(1)
        move= random.choice(game.available_moves())
        return move


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_move=False
        val= None
        while not valid_move:
            move= input(self.letter + '\'s turn, Input move [0-9]: ')
            try:
                val= int(move)
                if val not in game.available_moves():
                    raise ValueError
                valid_move= True
            except ValueError:
                print('Invalid move. Pleae try again.')
        return val 


class BossPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        print("Computer's turn")
        time.sleep(0.8)
        if len(game.available_moves())==9:
            move= random.choice(game.available_moves())
        else:
            move= self.minimax(game,self.letter)['position']
        return move

    def minimax(self,game, letter):
        max_player= self.letter
        other_player= 'O' if letter == 'X' else 'X'

        if game.current_winner == other_player:   #base case, check first if there is a winner
            # we need to keep track of the score for minimax algorithm to work
            return {
                'position': None,
                'score': 1 * (game.empty_square_count() + 1) if other_player==max_player else -1 * (
                    game.empty_square_count() + 1)
            }

        elif not game.empty_squares(): # no empty squares left
            return {'position': None, 'score': 0}

        # initialise a dictionary with the best possible score
        best= {}
        if letter == max_player:
            best= {'position': None , 'score': -math.inf} # minimum possible score, each move should maximize it
        else:
            best= {'position': None , 'score': math.inf} # maximum possible score, each move should minimize it

        for valid_move in game.available_moves():
            # step 1: make a move
            game.make_move(valid_move,letter)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score= self.minimax(game, other_player)
            
            # step 3: undo the move
            game.board[valid_move]= " "
            game.current_winner= None
            sim_score['position']= valid_move  # otherwise we will lose the value of move
            
            # step 4: update the dictionary
            if letter == max_player: # try to maximize the score of this player
                best= sim_score if sim_score['score']> best['score'] else best
            else:  # but minimise the other player
                best= sim_score if sim_score['score']< best['score'] else best

        return best
