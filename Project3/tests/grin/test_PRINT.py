import grin
import unittest
import io
import contextlib

class testprint(unittest.TestCase):

    def test_print1(self):
        grin.global_dictionary = {"LET": 0}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.IDENTIFIER, text = 'LET',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 'LET')
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.Print(variable_1)
        self.assertEqual(output.getvalue(),"0\n")

    def test_print2(self):
        grin.global_dictionary = {"LET": 0}
        variable_1 = grin.GrinToken(kind = grin.GrinTokenKind.LITERAL_INTEGER, text = 'LET',
                                    location = grin.GrinLocation(line = 1, column = 24),
                                    value = 'LET')
        with contextlib.redirect_stdout(io.StringIO()) as output:
            grin.Print(variable_1)
        self.assertEqual(output.getvalue(),"LET\n")