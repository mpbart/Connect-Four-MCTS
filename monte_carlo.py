import random
from tree import Node


class MonteCarlo(object):
  def __init__(self, state, piece, iterations, last_node=None):
    if last_node is not None:
      self.root = last_node
    else:
      self.root = Node(state.make_copy(), piece)
    self.original_state = state
    self.iterations = iterations

  def get_move(self):
    for _ in xrange(self.iterations):
      node = self.root
      state = self.original_state.make_copy()
      node = self.select(node, state)
      node = self.expand(node, state)
      state = self.rollout(state)
      self.backpropagate(node, state)
    return self.root, sorted(self.root.children, key=lambda c: c.wins/c.visits)[-1].column

  def select(self, node, state):
    while len(node.untried_moves) == 0 and len(node.children) != 0:
      node = node.uct_select_child()
      state.add_piece(node.current_player_piece, node.column)
    return node

  def expand(self, node, state):
    if len(node.untried_moves) != 0:
      col = random.choice(node.untried_moves)
      state.add_piece(node.current_player_piece, col)
      node = node.add_child(col, state)
    return node

  def rollout(self, state):
    while len(state.possible_moves()) != 0:
      column = random.choice(state.possible_moves())
      piece = self.__get_next_piece(state.last_added_piece)
      state.add_piece(piece, column)
    return state

  def backpropagate(self, node, state):
    while node is not None:
      node.update(state.get_result_for_player(node.current_player_piece))
      node = node.parentNode

  def __get_next_piece(self, piece):
    if piece == 'X':
      return 'O'
    return 'X'
