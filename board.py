COLUMNS = 7
ROWS = 6
EMPTY_SPACE = '.'


class Board(object):
  def __init__(self):
    self.__last_row = None
    self.__last_column = None
    self.board = []
    for row in range(ROWS):
      self.board.append([])
      for col in range(COLUMNS):
        self.board[row].append(EMPTY_SPACE)

  def print_board(self):
    for row in range(len(self.board)):
      for space in self.board[row]:
        print space,
      print
    print '-' * 50

  def add_piece(self, piece, column):
    if self.__column_filled(column):
      return False

    for row in range(1, len(self.board)):
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

  def winner_found(self):
    row, column = self.coordinate_of_most_recent_piece
    return self.vertical_winner(column) or self.horizontal_winner(row) or self.diagonal_winner(row, column)

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
    for row in range(len(self.board)-3):
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
    for col in range(len(self.board[row])-3):
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
    while tmp_row < len(self.board)-1 and tmp_col < len(self.board[0])-1:
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
    while tmp_col < len(self.board[0])-1 and tmp_row > 0:
      tmp_col += 1
      tmp_row -= 1
    while tmp_col >= 0 and tmp_row < len(self.board[0]):
      run.append(self.board[tmp_row][tmp_col])
      tmp_row += 1
      tmp_col -= 1
    return self.check_run(run)


  def check_run(self, run):
    if len(run) < 4:
      return False

    for i in range(len(run)-3):
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
