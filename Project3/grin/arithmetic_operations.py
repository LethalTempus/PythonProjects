import grin


class add(grin.let):


    def __init__(self, variable, value):
        self.variable = variable.value
        self.value = value.value
        self.add_decide_and_update(value)
        grin.line_number += 1


    def add_decide_and_update(self, value):
        try:
            if value.kind.category == grin.GrinTokenCategory.IDENTIFIER:
                grin.global_dictionary[self.variable] += grin.global_dictionary[value.value]
            elif value.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
                grin.global_dictionary[self.variable] += self.value
        except TypeError:
            exit("runtime error, invalid addition")


class sub(grin.let):


    def __init__(self, variable, value):
        self.variable = variable.value
        self.value = value.value
        self.sub_decide_and_update(value)
        grin.line_number += 1


    def sub_decide_and_update(self, value):
        try:
            if value.kind.category == grin.GrinTokenCategory.IDENTIFIER:
                grin.global_dictionary[self.variable] -= grin.global_dictionary[value.value]
            elif value.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
                grin.global_dictionary[self.variable] -= self.value
        except TypeError:
            exit("runtime error, invalid subtraction")


class mult(grin.let):


    def __init__(self, variable, value):
        self.variable = variable.value
        self.value = value.value
        self.mult_decide_and_update(value)
        grin.line_number += 1


    def mult_decide_and_update(self, value):
        try:
            if value.kind.category == grin.GrinTokenCategory.IDENTIFIER:
                grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] * grin.global_dictionary[value.value]
            elif value.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
                grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] * self.value
        except TypeError:
            exit("runtime error, invalid multiplication")


class div(grin.let):


    def __init__(self, variable, value):
        self.variable = variable.value
        self.value = value.value
        self.div_decide_and_update(value)
        grin.line_number += 1


    def div_decide_and_update(self, value):
        try:
            if value.kind.category == grin.GrinTokenCategory.IDENTIFIER:
                if type(grin.global_dictionary[self.variable]) is int and type(grin.global_dictionary[value.value]) is int:
                    grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] // grin.global_dictionary[value.value]
                else:
                    grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] / grin.global_dictionary[value.value]
            elif value.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
                if type(grin.global_dictionary[self.variable]) is int and type(self.value) is int:
                    grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] // self.value
                else:
                    grin.global_dictionary[self.variable] = grin.global_dictionary[self.variable] / self.value
        except TypeError:
            exit("runtime error, invalid division")
        except ZeroDivisionError:
            exit("runtime error, cannot divide by zero")