"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    countX = 0
    countO = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    if countX <= countO:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    n = len(board)
    A = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] == EMPTY:
                A.add((i,j))
    return A


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    B = deepcopy(board)
    if player(board) == X:
        B[i][j] = X
    else:
        B[i][j] = O
    return B



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    n = len(board)
    count3 = 0
    t3 = board[0][0]
    count4 = 0
    t4 = board[0][n-1]
    for i in range(n):
        # check row win
        t = board[i][0]
        count1 = 0
        for j in range(n):
            if board[i][j] != t:
                break
            count1 += 1
        if count1 == n:
            return t
        # check column win
        count2 = 0
        t2 = board[0][i]
        for j in range(n):
            if board[j][i] != t2:
                break
            count2 += 1
        if count2 == n:
            return t2
        # check diagonal win
        if board[i][i] == t3:
            count3 += 1
        if board[i][n-i-1] == t4:
            count4 += 1
    if count3 == n:
        return t3
    if count4 == n:
        return t4
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 999
    action = actions(board)
    for a in action:
        v = min(v, max_value(result(board,a)))
    return v
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -999
    action = actions(board)
    for a in action:
        print(a)
        v = max(v,min_value((result(board, a))))
    return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    acts = actions(board)
    agent = player(board)
    if agent == X:
        d = list()
        for a in acts:
            d.append((min_value(result(board, a)), a))
        return max(d)[1]
    else:
        d = list()
        for a in acts:
            d.append((max_value(result(board, a)), a))
        return min(d)[1]