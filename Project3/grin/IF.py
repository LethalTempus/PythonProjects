import grin


class IF(grin.goto,grin.gosub):


    def __init__(self, var1, comp, var2):
        self.var1 = var1
        self.comp = comp
        self.var2 = var2
        self.a = 0
        self.b = 0
        self.determine_a_b_c()


    def determine_a_b_c(self):

        if self.var1.kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if self.var1.value not in grin.global_dictionary.keys():
                grin.global_dictionary[self.var1.value] = 0
                self.a = 0
            elif self.var1.value in grin.global_dictionary.keys():
                self.a = grin.global_dictionary[self.var1.value]
        elif self.var1.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            self.a = self.var1.value

        if self.var2.kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if self.var2.value not in grin.global_dictionary.keys():
                grin.global_dictionary[self.var2.value] = 0
                self.b = 0
            elif self.var2.value in grin.global_dictionary.keys():
                self.b = grin.global_dictionary[self.var2.value]
        elif self.var2.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            self.b = self.var2.value


    def calculate_result(self):
        try:
            if self.comp.text == "<":
                if self.a < self.b:
                    return True
                else:
                    return False
            elif self.comp.text == "<=":
                if self.a <= self.b:
                    return True
                else:
                    return False
            elif self.comp.text == ">":
                if self.a > self.b:
                    return True
                else:
                    return False
            elif self.comp.text == ">=":
                if self.a >= self.b:
                    return True
                else:
                    return False
            elif self.comp.text == "<>":
                if self.a != self.b:
                    return True
                else:
                    return False
            elif self.comp.text == "=":
                if self.a == self.b:
                    return True
                else:
                    return False
        except TypeError:
            exit("runtime error, cannot compare number to string")

