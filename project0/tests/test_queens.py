# test_queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from collections import namedtuple
from queens import QueensState, DuplicateQueenError, MissingQueenError
import unittest

Position = namedtuple('Position', ['row', 'column'])
class TestQueensState(unittest.TestCase):
    def test_zero_queen_count_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_queen_added(self):
        state = QueensState(3,3)
        state.with_queens_added([(1, 3), (2, 3)])
        self.assertEqual(state.draw_board(),[[0,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]])

    def test_queen_added_1(self):
        state = QueensState(2, 2)
        with self.assertRaises(DuplicateQueenError):
            state.with_queens_added([(1, 1), (1, 1)])

    def test_queen_removed(self):
        state = QueensState(3, 3)
        state.with_queens_added([(1, 3), (2, 3)])
        state.with_queens_removed([(1, 3), (2, 3)])
        self.assertEqual(state.draw_board(),[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_queen_removed_1(self):
        state = QueensState(3, 4)
        state.with_queens_added([(1, 3), (2, 3)])
        with self.assertRaises(MissingQueenError):
            state.with_queens_removed([(0, 3), (2, 3)])

    def test_queen_count(self):
        state = QueensState(4,3)
        state.with_queens_added([(0, 3), (2, 2)])
        self.assertEqual(state.queen_count(), 2)

    def test_find_queen_position(self):
        state = QueensState(5,5)
        state.with_queens_added([(4, 3), (5, 1)])
        self.assertEqual(state.queens(), [(4, 3), (5, 1)])

    def test_has_queen(self):
        state = QueensState(6,7)
        state.with_queens_added([(6, 3), (2, 3)])
        self.assertTrue(state.has_queen([(6, 3)]))

    def test_has_queen_1(self):
        state = QueensState(7, 7)
        state.with_queens_added([(7, 3), (2, 3)])
        self.assertFalse(state.has_queen([(3, 3)]))

    def test_any_queen_unsafe(self):
        state = QueensState(8, 8)
        state.with_queens_added([(8, 8), (1, 1)])
        self.assertTrue(state.any_queens_unsafe())

    def test_any_queen_unsafe_1(self):
        state = QueensState(9, 9)
        state.with_queens_added([(1, 2), (7, 7)])
        self.assertFalse(state.any_queens_unsafe())

    def test_any_queen_unsafe_2(self):
        state = QueensState(3, 3)
        state.with_queens_added([])
        self.assertFalse(state.any_queens_unsafe())

    def test_any_queen_unsafe_3(self):
        state = QueensState(6, 6)
        state.with_queens_added([(0,0)])
        self.assertFalse(state.any_queens_unsafe())


    def test_exception(self):
        p = Position(1,2)
        self.assertEqual(str(DuplicateQueenError(p)),'duplicate queen in row 1 column 2')

    def test_exception_1(self):
        p = Position(3, 3)
        self.assertEqual(str(MissingQueenError(p)),'missing queen in row 3 column 3')



if __name__ == '__main__':
    unittest.main()
