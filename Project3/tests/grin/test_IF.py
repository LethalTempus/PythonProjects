import grin
import unittest

class TestGOSUBandRETURN(unittest.TestCase):

    def test_if_1(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '>',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = ">")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '4',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 4)
        grin.gosub([variable_1,variable_2,variable_3,variable_4,variable_5])
        self.assertEqual(grin.line_number, 6)

    def test_if_2(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '>',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = ">")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        grin.gosub([variable_1,variable_2,variable_3,variable_4,variable_5])
        self.assertEqual(grin.line_number, 7)

    def test_if_3(self):
        grin.global_dictionary = {"5": 4}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(),True)

    def test_if_4(self):
        grin.global_dictionary = {"5": 8}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(),False)

    def test_if_5(self):
        grin.global_dictionary = {}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<>',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(),True)

    def test_if_6(self):
        grin.global_dictionary = {}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<>',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(),False)

    def test_if_7(self):
        grin.global_dictionary = {}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "5")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "757")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(),True)

    def test_if_8(self):
        grin.global_dictionary = {"o": 888, "85": 0}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<>")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(), False)

    def test_if_9(self):
        grin.global_dictionary = {"o": "sre", "85": 0}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '<=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<=")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3, variable_4, variable_5)
        with self.assertRaises(TypeError and SystemExit):
            A.calculate_result()

    def test_if_10(self):
        grin.global_dictionary = {"o": 85, "85": 100}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '>=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<=")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(), False)

    def test_if_11(self):
        grin.global_dictionary = {"o": 85, "85": 0}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '>=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<=")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(), True)

    def test_if_12(self):
        grin.global_dictionary = {"o": 0, "85": 0}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<=")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(), True)

    def test_if_13(self):
        grin.global_dictionary = {"o": 85, "85": 0}
        variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'o',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "o")
        variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.GREATER_THAN, text = '=',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "<=")
        variable_5 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '85',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "85")
        A = grin.IF(variable_3,variable_4,variable_5)
        self.assertEqual(A.calculate_result(), False)

