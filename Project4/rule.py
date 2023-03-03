import random
import option


class rule:


    def __init__(self, line):
        self.my_rule = line
        self.rule_name = line[0]
        self.weighted_list = []
        for weighted_option in self.my_rule[1:]:
            self.weighted_list.append(int(weighted_option.split()[0]))


    def generate(self):
        A = option.option((random.choices(self.my_rule[1:], self.weighted_list))[0].split()[1:])
        return A.generate()