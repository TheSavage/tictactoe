"""
Tic Tac Toe Player    # Another change
"""

import math
import copy
from tkinter.tix import MAX

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    # return [[EMPTY, EMPTY, X],
    #         [O, O, EMPTY],
    #         [O, X, X]]
    # return [[O, O, O],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]   
    # return [[X, X, X],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]   
    # return [[X, X, O],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_y = 0
    for outer in board:
        for inner in outer:
            if inner == X:
                count_x += 1
            elif inner == O:
                count_y += 1
    if count_x <= count_y:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for outer in range(3):
        for inner in range(3):
            if board[outer][inner] == None:
                actions.add((outer, inner))
    return actions            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # if action is None:
    #     raise ValueError("Action cannot be None")
    
    if (action == None):            # debugging
        print ('in result')         # debugging  making a small change
        print (board)               # debugging
    
    mycopy = copy.deepcopy(board)
    if (mycopy[action[0]][action[1]] != None):   # error here:  Action is None
        raise ValueError
    
    myplayer = player(board)
    mycopy[action[0]][action[1]] = myplayer
    return mycopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for outer in board:
        if outer[0] == outer[1] == outer[2] and outer[0] != None:
            return outer[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]
    
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and board[1][1] != None):
        return board[1][1]
    if (board[2][0] == board[1][1] == board[0][2] and board[1][1] != None):
        return board[1][1]    

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check rows
    for outer in board:
        if outer[0] == outer[1] == outer[2] and outer[0] != None:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return True
    
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and board[1][1] != None):
        return True
    if (board[2][0] == board[1][1] == board[0][2] and board[1][1] != None):
        return True
    
    # check for full board
    for outer in board:
        for inner in outer:
            if inner == None:
                return False
            
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'O':
        return -1
    elif win == 'X':
        return 1
    else:
        return 0
    


def MinValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board): 
        v = min(v, MaxValue(result(board, action)))
    return v 
    #raise NotImplementedError   

def MaxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):  
        v = max(v, MinValue(result(board, action)))
    return v

    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # return the optimal move for the player to move on that board.
    # The move returned should be the optimal action (i, j) that is one of the 
    # allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.

   
    # If the board is a terminal board, the minimax function should return None.
    if terminal(board):
        return None
    
    current_player = player(board)
    possible_actions = actions(board)

    best_move = None
    if current_player == X:
        best_move = MaxValue(board)
            
    if current_player == O:
        best_move = MinValue(board)

    return best_move



# iterate over all possible actions
# , simulate the result
# , and pick the move with the best outcome.
# Notes

#     if current_player == X:
#         value = -math.inf
#         for action in actions(board):
#             min_value = MinValue(result(board, action))
#             if min_value > value:
#                 value = min_value
#                 best_action = action
#     else:
#         value = math.inf
#         for action in actions(board):
#             max_value = MaxValue(result(board, action))
#             if max_value < value:
#                 value = max_value
#                 best_action = action
#     return best_action


    #raise NotImplementedError

