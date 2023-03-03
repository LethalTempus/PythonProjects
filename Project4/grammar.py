import rule


class grammar:
    def __init__(self, entire_grammar):
        self.grammar = entire_grammar


    def generate(self, starting_var):
        try:
            for line in self.grammar:
                if line[0] == starting_var:
                    A = rule.rule(line)
                    return A.generate()
        except TypeError:
            pass