from itertools import cycle
from player import Player
from board import Board
from tree import Node
from monte_carlo import MonteCarlo
ITERATIONS = 10000


class Game(object):
  def __init__(self):
    self.players = cycle([Player('X', 'Player 1'), Player('O', 'Computer')])
    self.board = Board()
    self.current_player = None
    self.__advance_turn()

  def play(self):
    node = Node(self.board, self.current_player.piece)
    print self.current_player.name, ' goes first'
    self.board.print_board()

    while True:
      if self.current_player.name != 'Computer':
        column = self.get_move()

        while not self.board.add_piece(self.current_player.piece, column):
          print 'That is not a valid move. Please select a different column'
          column = self.get_move()

      else:
        node, column = MonteCarlo(self.board.make_copy(), 'O', ITERATIONS, last_node=node).get_move()
        print 'Computer chooses column', column
        self.board.add_piece(self.current_player.piece, column)

      self.board.print_board()
      node = self.__navigate_to_node_for_move(node, column, self.board)
      if self.board.winner_found():
        print '***** ' + self.current_player.name + ' wins!'
        break

      if self.board.spaces_left() == 0:
        print '***** Tie game'
        break

      self.__advance_turn()

  def get_move(self):
    msg = self.current_player.name + ' which column number would you like to play? '
    col = raw_input(msg)
    return int(col)

  def __advance_turn(self):
    self.current_player = next(self.players)

  def __navigate_to_node_for_move(self, node, column, board):
    for child in node.children:
      if child.column == column:
        return child
    return Node(board, node.current_player_piece)
