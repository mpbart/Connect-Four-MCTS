from math import sqrt, log


class Node:
    def __init__(self, state, piece, column=None, parent=None):
        self.column = column
        self.parentNode = parent
        self.player_piece = piece
        self.untried_moves = state.possible_moves()
        self.children = list()
        self.wins = 0
        self.visits = 0

    def uct_select_child(self):
        max_score, max_child = 0, None
        for child in self.children:
          score = child.wins / child.visits + sqrt(2*log(self.visits) / child.visits)
          if score > max_score:
            max_child = child
        return max_child

    def add_child(self, col, state):
        node = Node(state, self.get_next_piece(self.player_piece), column=col, parent=self)
        self.untried_moves.remove(col)
        self.children.append(node)
        return node

    def update(self, result):
        self.visits += 1
        self.wins += result

    def get_next_piece(self, piece):
      if piece == 'X':
        return 'O'
      return 'X'

