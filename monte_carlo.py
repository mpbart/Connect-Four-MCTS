import time


class MonteCarlo(object):
  def __init__(self, tree):
    self.tree = tree

  def next_move(self, board):
    end_time = time.time() + 0.60

    while time.time() <= end_time:
      node = self.tree.root.select_move()
      if not node.board.winner_found() and not node.board.spaces_left() == 0:
        node.expand()

      next_node = node
      if len(node.children) > 0:
        next_node = node.get_random_child()

      result = self.simulate_to_end(next_node)
      self.record_results(next_node, result)

    child = self.tree.root.get_max_score_child()
    _, col = child.board.coordinate_of_most_recent_piece
    return col
