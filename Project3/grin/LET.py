import grin


class let:


    def __init__(self, variable, value):
        self.variable = variable.value
        self.value = value.value
        self.let_decide_and_update(value)
        grin.line_number += 1


    def let_decide_and_update(self, value):
        if value.kind.category == grin.GrinTokenCategory.IDENTIFIER:
            grin.global_dictionary[self.variable] = grin.global_dictionary[value.value]
        elif value.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            grin.global_dictionary[self.variable] = value.value

