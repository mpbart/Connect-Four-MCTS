COLUMNS = 7
ROWS = 6
EMPTY_SPACE = '.'


class Board(object):
  def __init__(self):
    self.__last_row = 0
    self.__last_column = 0
    self.board = []
    for row in xrange(ROWS):
      self.board.append([])
      for col in xrange(COLUMNS):
        self.board[row].append(EMPTY_SPACE)

  def make_copy(self):
    b = Board()
    for row in xrange(ROWS):
      for col in xrange(COLUMNS):
        b.board[row][col] = self.board[row][col]
    return b

  def print_board(self):
    for row in xrange(len(self.board)):
      for space in self.board[row]:
        print space,
      print
    print '-' * 50

  def add_piece(self, piece, column):
    if self.__column_filled(column):
      return False

    for row in xrange(1, len(self.board)):
      if self.board[row][column] != EMPTY_SPACE:
        self.board[row - 1][column] = piece
        self.__last_row = row - 1
        self.__last_column = column
        return True

    # If this is the first piece in the column
    self.board[-1][column] = piece
    self.__last_row = len(self.board) - 1
    self.__last_column = column
    return True

  @property
  def coordinate_of_most_recent_piece(self):
    return (self.__last_row, self.__last_column)

  @property
  def last_added_piece(self):
    return self.board[self.__last_row][self.__last_column]

  """
  This function gives the weights to wins(1.0), losses(0.0), and draws(0.5)
  """
  def get_result_for_player(self, player_piece):
    if self.is_draw():
      return 0.5
    elif self.last_added_piece == player_piece:
      return 1.0
    else:
      return 0.0

  def is_draw(self):
    not self.winner_found and self.spaces_left == 0

  def winner_found(self):
    row, column = self.coordinate_of_most_recent_piece
    return self.vertical_winner(column) or self.horizontal_winner(row) or self.diagonal_winner(row, column)

  def possible_moves(self):
    if self.winner_found():
      return []
    return [i for i in xrange(COLUMNS) if not self.__column_filled(i)]

  def spaces_left(self):
    count = 0
    for row in self.board:
      for space in row:
        if space == EMPTY_SPACE:
          count += 1
    return count

  def __column_filled(self, col):
    for row in self.board:
      if row[col] == EMPTY_SPACE:
        return False
    return True

  def vertical_winner(self, column):
    for row in xrange(len(self.board)-3):
      if (self.board[row][column] == 'X' and
          self.board[row+1][column] == 'X' and
          self.board[row+2][column] == 'X' and
          self.board[row+3][column] == 'X'):
        return True
      if (self.board[row][column] == 'O' and
          self.board[row+1][column] == 'O' and
          self.board[row+2][column] == 'O' and
          self.board[row+3][column] == 'O'):
        return True
    return False


  def horizontal_winner(self, row):
    for col in xrange(len(self.board[row])-3):
      if (self.board[row][col] == 'X' and
          self.board[row][col+1] == 'X' and
          self.board[row][col+2] == 'X' and
          self.board[row][col+3] == 'X'):
        return True
      if (self.board[row][col] == 'O' and
          self.board[row][col+1] == 'O' and
          self.board[row][col+2] == 'O' and
          self.board[row][col+3] == 'O'):
        return True
    return False


  def diagonal_winner(self, row, column):
    return self.__check_upper_right_diagonal(row, column) or self.__check_upper_left_diagonal(row, column)

  def __check_upper_left_diagonal(self, row, column):
    tmp_row, tmp_col = row, column
    run = []
    while tmp_row < ROWS-1 and tmp_col < COLUMNS-1:
      tmp_row += 1
      tmp_col += 1
    while tmp_col >= 0 and tmp_row >= 0:
      run.append(self.board[tmp_row][tmp_col])
      tmp_row -= 1
      tmp_col -= 1
    return self.check_run(run)

  def __check_upper_right_diagonal(self, row, column):
    tmp_row, tmp_col = row, column
    run = []
    while tmp_col < COLUMNS-1 and tmp_row > 0:
      tmp_col += 1
      tmp_row -= 1

    while tmp_col >= 0 and tmp_row < ROWS:
      run.append(self.board[tmp_row][tmp_col])
      tmp_row += 1
      tmp_col -= 1
    return self.check_run(run)


  def check_run(self, run):
    if len(run) < 4:
      return False

    for i in xrange(len(run)-3):
      if (run[i] == 'X' and
          run[i+1] == 'X' and
          run[i+2] == 'X' and
          run[i+3] == 'X'):
        return True
      if (run[i] == 'O' and
          run[i+1] == 'O' and
          run[i+2] == 'O' and
          run[i+3] == 'O'):
        return True
    return False
