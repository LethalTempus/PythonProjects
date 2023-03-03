import grin


class gosub:


    remembered_line = []


    def __init__(self, *target):

        self.GO = True

        if len(target[0]) > 1:
            self.GO = grin.IF(target[0][2], target[0][3], target[0][4]).calculate_result()

        if self.GO is True:
            gosub.remembered_line.append(grin.line_number + 1)
            self.gosub_decide_and_update(target[0][0])
        elif self.GO is False:
            grin.line_number += 1


    def gosub_decide_and_update(self, v):

        if v.kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if grin.global_dictionary[v.value] == 0:
                exit("runtime error, infinite loop")
            elif type(grin.global_dictionary[v.value]) is int:
                grin.line_number += grin.global_dictionary[v.value]
            elif type(grin.global_dictionary[v.value]) is str:
                try:
                    grin.line_number = grin.global_label_dictionary[grin.global_dictionary[v.value]]
                except KeyError:
                    exit("runtime error, label not found")

        elif v.kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            if v.value == 0:
                exit("runtime error, infinite loop")
            if type(v.value) is int:
                grin.line_number += v.value
            elif type(v.value) is str:
                try:
                    grin.line_number = grin.global_label_dictionary[v.value]
                except KeyError:
                    exit("runtime error, label not found")


class Return:


    def __init__(self):
        if len(gosub.remembered_line) == 0:
            exit("runtime error, return with no corresponding gosub")
        grin.line_number = gosub.remembered_line[-1]
        gosub.remembered_line.pop(-1)