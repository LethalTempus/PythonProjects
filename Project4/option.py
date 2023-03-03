import variable_symbol, terminal_symbol


class option:


    final_list = []

    def __init__(self, one_option):
        self.my_option = one_option
        self.final_list = []


    def generate(self):
        for symbol in self.my_option:
            if symbol[0] == "[":
                A = variable_symbol.variable_symbol(symbol)
                A.generate()
            elif symbol[0] != "[":
                A = terminal_symbol.terminal_symbol(symbol)
                option.final_list.append(A.generate())
        return " ".join(option.final_list)