import grin
import unittest


class TestLet(unittest.TestCase):


    def test_let_1(self):
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        token = grin.let(self.variable_1, self.variable_2)
        self.assertEqual(token.variable, "LET")
        self.assertEqual(token.value, 3)

    def test_let_2(self):
        grin.global_dictionary = {"3": 5}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        token = grin.let(self.variable_3, self.variable_4)
        self.assertEqual(token.variable, "LET")
        self.assertEqual(token.value, "3")