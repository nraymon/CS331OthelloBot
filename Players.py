'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''

import copy
import sys

sys.setrecursionlimit(5555555)

class Node:
    node = None
    action = (None, None)

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()



class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol);

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return  (col, row)


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol);
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
       
    def minimax_decision(self, node):
        min = float("inf")
        min_action = None
        for a in self.min_actions(node):
            tmp = self.max_value(a)
            if min > tmp:
                min = tmp
                min_action = a

        return min_action.action

    def max_value(self, node):
        if self.terminal_state(node):
            return self.utility(node)

        v = float("-inf")

        for a in self.max_actions(node):
            v = max(v, self.min_value(a))

        return v

    def min_value(self, node):
        if self.terminal_state(node):
            return self.utility(node)

        v = float("inf")

        for a in self.min_actions(node):
            v = min(v, self.max_value(a))

        return v

    def min_actions(self, node):
        succs = []
        for i in range(node.state.get_num_cols()):
            for j in range(node.state.get_num_rows()):
                if node.state.is_legal_move(i, j, 'O'):
                    child = copy.deepcopy(node)
                    child.action = (i, j)
                    child.state.play_move(i, j, 'O')
                    succs.append(child)

        return succs

    def max_actions(self, node):
        succs = []
        for i in range(node.state.get_num_cols()):
            for j in range(node.state.get_num_rows()):
                if node.state.is_legal_move(i, j, 'X'):
                    child = copy.deepcopy(node)
                    child.action = (i, j)
                    child.state.play_move(i, j, 'X')
                    succs.append(child)

        return succs

    def get_move(self, state):
        node = Node()
        node.state = copy.deepcopy(state)
        act = self.minimax_decision(node)
        print(act)
        return act

    def terminal_state(self, node):
        if node.state.has_legal_moves_remaining('O') or node.state.has_legal_moves_remaining('X'):
            return False
        else:
            return True

    def utility(self, node):
        util = node.state.count_score('X') - node.state.count_score('O')

        if util == 0:
            return 0

        elif util > 0:
            return 1

        else:
            return -1
