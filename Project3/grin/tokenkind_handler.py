import grin


global_dictionary = dict()
line_number = 1
global_label_dictionary = dict()


def handle_token(tokens):


    def var_value_initialization():
        if tokens[1].value not in global_dictionary.keys():
            global_dictionary[tokens[1].value] = 0
        if tokens[2].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if tokens[2].value not in global_dictionary.keys():
                global_dictionary[tokens[2].value] = 0


    def val_initialization():
        if tokens[1].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if tokens[1].value not in global_dictionary.keys():
                global_dictionary[tokens[1].value] = 0

    if tokens[0].kind.category == grin.GrinTokenCategory.KEYWORD:
        if tokens[0].text == "LET":
            var_value_initialization()
            grin.let(tokens[1], tokens[2])
        elif tokens[0].text == "ADD":
            var_value_initialization()
            grin.add(tokens[1], tokens[2])
        elif tokens[0].text == "SUB":
            var_value_initialization()
            grin.sub(tokens[1], tokens[2])
        elif tokens[0].text == "MULT":
            var_value_initialization()
            grin.mult(tokens[1], tokens[2])
        elif tokens[0].text == "DIV":
            var_value_initialization()
            grin.div(tokens[1], tokens[2])
        elif tokens[0].text == "GOTO":
            val_initialization()
            grin.goto(tokens[1:])
        elif tokens[0].text == "GOSUB":
            val_initialization()
            grin.gosub(tokens[1:])
        elif tokens[0].text == "RETURN":
            grin.Return()
        elif tokens[0].text == "END":
            exit()
        elif tokens[0].text == "PRINT":
            val_initialization()
            grin.Print(tokens[1])
        elif tokens[0].text == "INNUM":
            val_initialization()
            grin.innum(tokens[1])
        elif tokens[0].text == "INSTR":
            val_initialization()
            grin.instr(tokens[1])
    else:
        exit()
