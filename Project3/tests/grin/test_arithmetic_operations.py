import grin
import unittest


class Test_arithmetic(unittest.TestCase):
    def test_add_1(self):
        grin.global_dictionary = {"LET": 5}
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        grin.add(self.variable_1, self.variable_2)
        self.assertEqual(grin.global_dictionary["LET"],8)

    def test_add_2(self):
        grin.global_dictionary = {"3": 5, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        grin.add(self.variable_3, self.variable_4)
        self.assertEqual(grin.global_dictionary["LET"],13)

    def test_add_3(self):
        grin.global_dictionary = {"3": "I love you", "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        with self.assertRaises(TypeError and SystemExit):
            grin.add(self.variable_3, self.variable_4)

    def test_sub_1(self):
        grin.global_dictionary = {"LET": 5}
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        grin.sub(self.variable_1, self.variable_2)
        self.assertEqual(grin.global_dictionary["LET"],2)

    def test_sub_2(self):
        grin.global_dictionary = {"3": 5, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        grin.sub(self.variable_3, self.variable_4)
        self.assertEqual(grin.global_dictionary["LET"],3)

    def test_sub_3(self):
        grin.global_dictionary = {"3": "I love you", "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        with self.assertRaises(TypeError and SystemExit):
            grin.sub(self.variable_3, self.variable_4)

    def test_div_1(self):
        grin.global_dictionary = {"LET": 5}
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        grin.div(self.variable_1, self.variable_2)
        self.assertEqual(grin.global_dictionary["LET"],1)

    def test_div_2(self):
        grin.global_dictionary = {"3": 5, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        grin.div(self.variable_3, self.variable_4)
        self.assertEqual(grin.global_dictionary["LET"],1)

    def test_div_3(self):
        grin.global_dictionary = {"3": "I love you", "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        with self.assertRaises(TypeError and SystemExit):
            grin.div(self.variable_3, self.variable_4)

    def test_div_4(self):
        grin.global_dictionary = {"3": 0, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        with self.assertRaises(ZeroDivisionError and SystemExit):
            grin.div(self.variable_3, self.variable_4)

    def test_div_5(self):
        grin.global_dictionary = {"3": 4.0, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        grin.div(self.variable_3, self.variable_4)
        self.assertAlmostEqual(grin.global_dictionary["LET"],2.0)

    def test_div_6(self):
        grin.global_dictionary = {"3": 4.0, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                            location = grin.GrinLocation(line = 1, column = 24),
                                            value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_FLOAT, text = '4.0',
                                            location = grin.GrinLocation(line = 1, column = 29),
                                            value = 4.0)
        grin.div(self.variable_3, self.variable_4)
        self.assertAlmostEqual(grin.global_dictionary["LET"], 2.0)

    def test_mult_1(self):
        grin.global_dictionary = {"LET": 5}
        self.variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_2 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = 3)
        grin.mult(self.variable_1, self.variable_2)
        self.assertEqual(grin.global_dictionary["LET"],15)

    def test_mult_2(self):
        grin.global_dictionary = {"3": 5, "LET": 8}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        grin.mult(self.variable_3, self.variable_4)
        self.assertEqual(grin.global_dictionary["LET"],40)

    def test_mult_3(self):
        grin.global_dictionary = {"3": "I love you", "LET": 8.5}
        self.variable_3 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                         location = grin.GrinLocation(line = 1, column = 24),
                                         value = 'LET')
        self.variable_4 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '3',
                                         location = grin.GrinLocation(line = 1, column = 29),
                                         value = '3')
        with self.assertRaises(TypeError and SystemExit):
            grin.mult(self.variable_3, self.variable_4)
