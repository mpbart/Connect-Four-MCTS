from itertools import cycle
from player import Player
from board import Board


class Game(object):
  def __init__(self):
    self.players = cycle([Player('X', 'Player 1'), Player('O', 'Player 2')])
    self.board = Board()
    self.__advance_turn()

  def play(self):
    print self.current_player.name, ' goes first'
    self.board.print_board()

    while True:
      column = self.get_move()

      while not self.board.add_piece(self.current_player.piece, column):
        print 'That is not a valid move. Please select a differnt column'
        column = self.get_move()

      self.board.print_board()
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
