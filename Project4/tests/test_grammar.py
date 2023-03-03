import grammar
import unittest

class test_grammar(unittest.TestCase):
    def test_grammar_work(self):
        A = grammar.grammar([['ReturnStatement', '1 RETURN'], ['EndStatement', '1 END']])
        self.assertEqual(A.generate("EndStatement"), "END")

    def test_grammar_work_1(self):
        A = grammar.grammar([['FirstName', '1 Alex', '1 Haruki', '1 William', '1 John', '1 Anya', '1 Boochi', '1 Aatrox', '1 Victor', '1 Viego', '1 Graves', '1 Ekko'], ['EndStatement', '1 FirstName']])
        self.assertEqual(A.generate("EndStatement"), "END FirstName")
