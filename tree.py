from math import sqrt, log
MAX_INT = 2**32


class Tree(object):
  def __init__(self):
    self.root = Node(None)


class Node(object):
  def __init__(self, parent, board):
    self.children = []
    self.parent = parent
    self.board = board
    self.state = State()

  def select_move(self, node):
    tmp_node = node
    while len(tmp_node.children) != 0:
      tmp_node = self.max_child_uct_score(tmp_node)
    return tmp_node

  def calculate_score(self):
    if self.state.visit_count == 0:
      return MAX_INT
    return ((self.state.win_score / visit_count) +
        (1.41 * sqrt(log(self.state.parent_visits) / self.state.visit_count)))

  def expand(self):
    for i in possible_states:
      pass

  def __max_child_uct_score(self, node):
    max_child, max_child_score = 0, None
    for child in node.children:
      if child.calculate_score() > max_child_score:
        max_child_score = child.calculate_score()
        max_child = child
    return  max_child



def State(object):
  def __init__(self):
    self.win_score = 0
    self.parent_visits = 0
    self.visit_count = 0
