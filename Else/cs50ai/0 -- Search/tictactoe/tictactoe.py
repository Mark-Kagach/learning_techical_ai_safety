"""
Tic Tac Toe Player
"""

import math
import copy


# possible moves on the board
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

    count=0

    for row in board:
        for item in row:
            if item != None: 
                count=count+1
    #print(count)

    if count % 2 == 0:
        #print(X)
        return X
    else:
        #print(O)
        return O


    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    count=0

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == None:
                possible_actions.add((i,j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #1️⃣❗seems to be the heart/ essence, highest risk part I should start with. 
    # doesn't modify original board, just possible boards from where we are right now.

    # if action is not valid, raise an exception
    # make a deep copy of the board before making changes to it.
    
    #0. make a deep copy of the board.
    cboard = copy.deepcopy(board)
    #print("cboard:", cboard)

    #1. understand whose turn it is.
    turn = player(board)
    #print("turn:", turn)

    #1.5 check if action is valid for the copied board
    valid_actions = actions(board)
    #print("valid_actions:",valid_actions)
    for item in valid_actions:
        if item==action:
            #print(item, action, "similar!")

            #2. take an action and apply it to the copied board
            #put turn to the action place in a board
            cboard[action[0]][action[1]]=turn
            #print(cboard)

            #3. output the result
            #print(cboard)
            return cboard

    raise NameError("Not Valid Move!")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Output X or O depending on who won.
    # Check if one wins the game by comparing it whether there is a 3 in a row diagonally, vertically or horizontally.
    # return None if no winner yet.

    for row in board:
        if row[0]==row[1]==row[2] and row[0] is not None:
            return row[0]
    for j in range(3):
        if board[0][j]== board[1][j]== board[2][j] and board[0][j] is not None:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # be it because someone won, or just out of cells return true, else return false.
    if winner(board) != None or len(actions(board))==0: 
        #print(True)
        return True
    else:
        #print(False)
        return False
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    #You may assume utility will only be called on a board if terminal(board) is True.
    if winner(board)==X: 
        return 1
    if winner(board)==O: 
        return -1
    return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -100
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return(v)

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return(v)

def minimax(board):
    """
    Returns the optimal action (i,j) for the current player on the board.
    """
    if terminal(board) == True: 
        return None

    if player(board) == X:
        plays=[]
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    if player(board) == O:
        plays=[]
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]
