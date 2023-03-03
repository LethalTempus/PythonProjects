import grin
import unittest

class testtokenhandler(unittest.TestCase):

    def test_token_handler(self):
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_1(self):
        grin.global_dictionary = {"A": "like"}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'ADD',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'ADD')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_STRING, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = "3")
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_2(self):
        grin.global_dictionary = {"A": "like", "3": "wow"}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'ADD',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'ADD')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = "3")
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_3(self):
        grin.global_dictionary = {"A": 5, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'SUB',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'SUB')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = "3")
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_4(self):
        grin.global_dictionary = {"A": "like", "3": 5}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'MULT',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'MULT')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = "3")
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_5(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'DIV',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = "3")
        grin.handle_token([self.variable_0, self.variable_1, self.variable_2])

    def test_token_handler_6(self):
        grin.global_dictionary = {"A": 4, "3": 2, "B":8}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'GOTO',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'B',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'B')
        grin.handle_token([self.variable_0, self.variable_1])

    def test_token_handler_7(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'GOSUB',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        grin.handle_token([self.variable_0, self.variable_1])

    def test_token_handler_8(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'RETURN',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        grin.handle_token([self.variable_0])

    def test_token_handler_9(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'END',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        with self.assertRaises(SystemExit):
            grin.handle_token([self.variable_0])

    def test_token_handler_10(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LET, text = 'PRINT',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'DIV')
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        grin.handle_token([self.variable_0,self.variable_1])

    def test_token_handler_11(self):
        grin.global_dictionary = {"A": 4, "3": 2}
        self.variable_0 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 5)
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'A',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'A')
        with self.assertRaises(SystemExit):
            grin.handle_token([self.variable_0,self.variable_1])
