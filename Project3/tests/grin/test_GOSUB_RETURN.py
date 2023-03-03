import grin
import unittest

class TestGOSUBandRETURN(unittest.TestCase):
    def test_gosub_1(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '5',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 5)
        grin.gosub([variable_1])
        self.assertEqual(grin.line_number, 6)

    def test_gosub(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 0)
        with self.assertRaises(SystemExit):
            grin.gosub([variable_1])

    def test_gosub_4(self):
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(KeyError and SystemExit):
            grin.gosub([variable_1])


    def test_gosub_2(self):
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
        self.assertEqual(grin.line_number, 11)

    def test_gosub_3(self):
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
        self.assertEqual(grin.line_number, 12)

    def test_gosub_5(self):
        grin.global_dictionary = {"0": 5}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        grin.gosub([variable_1])
        self.assertEqual(grin.line_number, 17)

    def test_gosub_6(self):
        grin.global_dictionary = {"0": "ntr"}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(KeyError and SystemExit):
            grin.gosub([variable_1])

    def test_gosub_7(self):
        grin.global_dictionary = {"0": 0}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = '0',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = "0")
        with self.assertRaises(SystemExit):
            grin.gosub([variable_1])

    def test_return(self):
        grin.gosub.remembered_line = [11]
        grin.Return()
        self.assertEqual(grin.line_number, 11)

    def test_return_1(self):
        grin.gosub.remembered_line = []
        with self.assertRaises(SystemExit):
            grin.Return()

