import grin


class innum:


    def __init__(self, identifier):
        self.id = identifier
        self.innum_operation()
        grin.line_number += 1


    def innum_operation(self):
        number = input()
        try:
            try:
                grin.global_dictionary[self.id.value] = int(number)
            except ValueError:
                grin.global_dictionary[self.id.value] = float(number)
        except ValueError:
            exit("input must be a number")


class instr:


    def __init__(self, identifier):
        self.id = identifier
        self.instr_operation()
        grin.line_number += 1


    def instr_operation(self):
        string = input()
        grin.global_dictionary[self.id.value] = str(string)