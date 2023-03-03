import grammar
import unittest


class test_variable(unittest.TestCase):
    def test_variable_work(self):
        A = grammar.grammar([['GosubStatement', '1 GOSUB [Target] [Condition]'], ['GOSUB', '1 END'], ['Target', '1 END'], ['Condition', '1 END']])
        self.assertEqual(A.generate("GosubStatement"),"GOSUB")




