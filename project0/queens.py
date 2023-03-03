# queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# A module containing tools that could assist in solving variants of the
# well-known "n-queens" problem.  Note that we're only implementing one part
# of the problem: immutably managing the "state" of the board (i.e., which
# queens are arranged in which cells).
#
# Your goal is to complete the QueensState class described below, though
# you'll need to build it incrementally, as well as test it incrementally by
# writing unit tests in test_queens.py.  Make sure you've read the project
# write-up before you proceed, as it will explain the requirements around
# following (and documenting) an incremental process of solving this problem.
#
# DO NOT MODIFY THE Position NAMEDTUPLE OR THE PROVIDED EXCEPTION CLASSES.

from collections import namedtuple



Position = namedtuple('Position', ['row', 'column'])

# Ordinarily, we would write docstrings within classes or their methods.
# Since a namedtuple builds those classes and methods for us, we instead
# add the documentation by hand afterward.
Position.__doc__ = 'A position on a chessboard, specified by zero-based row and column numbers.'
Position.row.__doc__ = 'A zero-based row number'
Position.column.__doc__ = 'A zero-based column number'



class DuplicateQueenError(Exception):
    """An exception indicating an attempt to add a queen where one is already present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where the duplicate queen exists."""
        self._position = position


    def __str__(self) -> str:
        return f'duplicate queen in row {self._position.row} column {self._position.column}'



class MissingQueenError(Exception):
    """An exception indicating an attempt to remove a queen where one is not present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where a queen is missing."""
        self._position = position


    def __str__(self) -> str:
        return f'missing queen in row {self._position.row} column {self._position.column}'


class QueensState:
    """Immutably represents the state of a chessboard being used to assist in
    solving the n-queens problem."""

    def __init__(self, rows: int, columns: int):
        """Initializes the chessboard to have the given numbers of rows and columns,
        with no queens occupying any of its cells."""
        self.board = []
        self.list_of_position = []
        for row in range(rows+1):
            self.board.append([])
            for column in range(columns+1):
                self.board[row].append(0)
        self.queen_count_num = 0
        self.A = 0


    def queen_count(self) -> int:
        """Returns the number of queens on the chessboard."""
        for a in self.board:
            for b in a:
                if b == 1:
                    self.queen_count_num += 1
        return self.queen_count_num

    def queens(self) -> list[Position]:
        """Returns a list of the positions in which queens appear on the chessboard,
        arranged in no particular order."""

        for b in range(len(self.board)):
            if self.board[b].count(1) != 0:
                c = self.board[b].index(1)
                self.list_of_position.append((b, c))
        return self.list_of_position

    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        row_tracker = position[0][0]
        column_tracker = position[0][1]
        if self.board[row_tracker][column_tracker] == 1:
            return True
        else:
            return False

    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        self.list_of_position = self.queens()
        for position in self.list_of_position:
            list_of_position1 = self.queens()
            list_of_position1.remove(position)
            conflict_position_list = []
            list_of_coordinates = []
            for a in range(len(self.board)):
                for b in range(len(self.board[a])):
                    list_of_coordinates.append([a, b])
            for po in list_of_coordinates:
                if position[0] == po[0] or position[1] == po[1]:
                    conflict_position_list.append(po)
                elif position[0] - position[1] == po[0] - po[1]:
                    conflict_position_list.append(po)
                elif position[0] + position[1] == po[0] + po[1]:
                    conflict_position_list.append(po)
            conflict_position_list.remove(list(position))
            for exist_queen_position in list_of_position1:
                if conflict_position_list.count(list(exist_queen_position)) != 1:
                    self.A = 0
                else:
                    self.A = 1
            if self.A == 1:
                return True
            else:
                return False

    def with_queens_added(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""
        for position in positions:
            row_tracker = position[0]
            column_tracker = position[1]
            if self.board[row_tracker][column_tracker] == 0:
                self.board[row_tracker][column_tracker] = 1
            else:
                raise DuplicateQueenError((row_tracker,column_tracker))

    def with_queens_removed(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        for position in positions:
            row_tracker = position[0]
            column_tracker = position[1]
            if self.board[row_tracker][column_tracker] == 1:
                self.board[row_tracker][column_tracker] = 0
            else:
                raise MissingQueenError((row_tracker, column_tracker))

    def draw_board(self):
        """For testing purposes."""
        return self.board

