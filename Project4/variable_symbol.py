import grammar


class variable_symbol:


    rule = None


    def __init__(self, symbol):
        self.variable = symbol
        self.rule = None


    def generate(self):
        return grammar.grammar.generate(grammar.grammar(variable_symbol.rule), self.variable[1:-1])