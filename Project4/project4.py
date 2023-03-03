# project4.py
#
# ICS 33 Fall 2022
# Project 4: Still Looking for Something
import pathlib, grammar, variable_symbol, option

def main() -> None:
    file_path = pathlib.Path(input())


    with open(file_path) as file:
        file_lines = file.readlines()


    big_list = []
    rule_cap = 0
    big_list_index = 0
    for item in file_lines:
        if item.startswith("{"):
            rule_cap = 1
        elif item.startswith("}"):
            rule_cap = 0
        if rule_cap == 1:
            big_list.append([])
            big_list_index += 1
            rule_cap = 2
        elif rule_cap == 2:
            big_list[big_list_index - 1].append(item.strip("\n"))


    number_of_lines = int(input())
    starting_var = input()


    A = grammar.grammar(big_list)
    variable_symbol.variable_symbol.rule = big_list


    for _ in range(number_of_lines):
        option.option.final_list = []
        print(''.join(list(A.generate(starting_var))))


if __name__ == '__main__':
    main()


"""
grin_1.txt
10
Sentence

"""