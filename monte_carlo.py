import random
from tree import Node


class MonteCarlo(object):
    def __init__(self, state, piece, iterations):
      self.root = Node(state, piece)
      self.computer_piece = piece
      self.original_state = state
      self.iterations = iterations

    def get_move(self):
      for i in xrange(self.iterations):
          node = self.root
          state = self.original_state.make_copy()

          # Select
          while len(node.untried_moves) == 0 and len(node.children) != 0:
              node = node.uct_select_child()
              state.add_piece(node.player_piece, node.column)

          # Expand
          if len(node.untried_moves) != 0:
              col = random.choice(node.untried_moves)
              state.add_piece(node.player_piece, col)
              node = node.add_child(col, state)

          # Rollout
          while state.spaces_left() != 0:
              column = random.choice(state.possible_moves())
              piece = self.get_next_piece(state.last_added_piece)
              state.add_piece(piece, column)

          # Backpropagate
          while node is not None:
              node.update(state.get_result_for_player(self.computer_piece))
              node = node.parentNode

      return sorted(self.root.children, key=lambda c: c.visits)[-1].column

    def get_next_piece(self, piece):
      if piece == 'X':
        return 'O'
      return 'X'

