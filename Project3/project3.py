import grin


def main() -> None:

    grin_message = []
    line_dictionary = dict()
    token_list = []


    while True:
        one_line = input()
        if one_line.strip() == ".":
            break
        grin_message.append(one_line)


    try:
        tokens = grin.parse(grin_message)
        token_list = list(tokens)
    except:
        exit("error during parsing")


    A = 0
    for token in token_list:
        A += 1
        if token[0].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if token[1].kind.category == grin.GrinTokenCategory.PUNCTUATION:
                grin.global_label_dictionary[token[0].value] = token[0].location.line
                token_list[A - 1] = token_list[A - 1][2:]


    for token in token_list:
        line_dictionary[token[0].location.line] = token

    while grin.line_number in line_dictionary.keys():
        grin.handle_token(line_dictionary[grin.line_number])


if __name__ == '__main__':
    main()
