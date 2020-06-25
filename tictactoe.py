"""
Tic Tac Toe Player
"""

import math
import copy
import time

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_count = 0
    for row_number in range(len(board)):
        for col_number in range(len(board[row_number])):
            if board[row_number][col_number] != EMPTY:
                player_count += 1
    # if the player_count is odd is O's turn
    if (player_count % 2) != 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row_number in range(len(board)):
        for col_number in range(len(board[row_number])):
            if board[row_number][col_number] == EMPTY:
                actions.add((row_number, col_number))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row_number, col_number = action
    if row_number > 3 or row_number < 0 or col_number > 3 or col_number < 0:
        raise ValueError
    new_board = copy.deepcopy(board)
    new_board[row_number][col_number] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    cols = [[],[],[]]
    diagonals = [[],[]]
    back_count = 2
    for row_number in range(len(board)):
        #check if there's winner on row
        if len(set(board[row_number])) == 1:
            return board[row_number][0]
        for col_number in range(len(board[row_number])):
            element = board[row_number][col_number]
            cols[col_number].append(element)
            if col_number == back_count:
                diagonals[1].append(element)
            if row_number == col_number:
                diagonals[0].append(element)
        back_count -= 1
    #check if there's winner on columns
    for col in cols:
        if len(set(col)) == 1:
            return col[0]
    #check if there's winner on diagonals
    for diagonal in diagonals:
        if len(set(diagonal)) == 1:
            return diagonal[0]
    
    return None
        
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        if None in row:
            return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if(winner_player == X):
        return 1
    if winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    start_time = time.time()
    if terminal(board):
        return None
    player_actions = actions(board)
    if player(board) == X:
        max_action = None
        max_score = -10
        for action in player_actions:
            min_value = minValue(result(board, action), None)
            if min_value > max_score:
                max_action = action
                max_score = min_value
        print("--- %s seconds ---" % (time.time() - start_time))
        return max_action
    
    if player(board) == O:
        min_action = None
        min_score = 10
        for action in player_actions:
            max_value = maxValue(result(board, action), None)
            if max_value < min_score:
                min_action = action
                min_score = max_value
        print("--- %s seconds ---" % (time.time() - start_time))
        return min_action
        


def maxValue(board, min_value):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, minValue(result(board, action), v))
        if min_value != None and v > min_value:
            break
    return v

def minValue(board, max_value):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, maxValue(result(board, action), v))
        if max_value != None and v < max_value:
            break
    return v