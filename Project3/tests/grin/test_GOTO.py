import grin
import unittest

class TestgotoandRETURN(unittest.TestCase):
    def test_goto_1(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        grin.goto([variable_1])
        self.assertEqual(grin.line_number, 6)

    def test_goto(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 0)
        with self.assertRaises(SystemExit):
            grin.goto([variable_1])

    def test_goto_4(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(KeyError and SystemExit):
            grin.goto([variable_1])


    def test_goto_2(self):
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
        grin.goto([variable_1,variable_2,variable_3,variable_4,variable_5])
        self.assertEqual(grin.line_number, 11)

    def test_goto_3(self):
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
        grin.goto([variable_1,variable_2,variable_3,variable_4,variable_5])
        self.assertEqual(grin.line_number, 12)

    def test_goto_5(self):
        grin.global_dictionary = {"0": 5}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        grin.goto([variable_1])
        self.assertEqual(grin.line_number, 17)

    def test_goto_6(self):
        grin.global_dictionary = {"0": "ntr"}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(KeyError and SystemExit):
            grin.goto([variable_1])

    def test_goto_7(self):
        grin.global_dictionary = {"0": 0}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(SystemExit):
            grin.goto([variable_1])