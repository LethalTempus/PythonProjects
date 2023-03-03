import grin


class Print:


    def __init__(self, target):
        self.print_decide_and_update(target)
        grin.line_number += 1


    def print_decide_and_update(self, v):
        if v.kind.category == grin.GrinTokenCategory.IDENTIFIER:
            print(grin.global_dictionary[v.value])
        elif v.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            print(v.value)