from preloaded import Any, Normal, Or, Str, ZeroOrMore
import re
LEFT_BRACKET = "("
RIGHT_BRACKET = ")"


def is_correct_input(indata):
    def correct_bracket_counter():
        if left_bracket_counter < right_bracket_counter:
            return False
        return True

    def correct_window():
        if window.count("|") > 1:
            return False
        return True

    if not indata:
        return False

    if "**" in indata:
        return False

    regexp_set = set(["(", ")", "*", ".", "|"])
    window = ["", ""]
    left_bracket_counter = 0
    right_bracket_counter = 0

    for ind, symbol in enumerate(indata):
        if symbol == LEFT_BRACKET:
            left_bracket_counter += 1
            if not correct_bracket_counter():
                return False
        elif symbol == RIGHT_BRACKET:
            right_bracket_counter += 1
            if not correct_bracket_counter():
                return False

        if symbol in regexp_set:
            window[0] = window[1]
            window[1] = symbol
            if not correct_window():
                print(symbol, ind)
                return False
    if left_bracket_counter != right_bracket_counter:
        return False

    return True


NUMBER = "Number"
EXPRESSION = "Expression"
MODIFICATION = "Modification_*"
CHILDREN = "Children"
FINISHED = "Finished"
SYMBOL_GROUP = "Symbol_group"
OR = 'Or'


def build_group_struct(number, expression, modification=False, finished=False, symbol_group=False, is_or=False):
    group_struct = {
                    NUMBER: number,
                    EXPRESSION: expression,
                    MODIFICATION: modification,
                    CHILDREN: [],
                    SYMBOL_GROUP: symbol_group,
                    FINISHED: finished,
                    OR: is_or,
                    }
    return group_struct


def find_children(group, start_number):
    is_or = False
    groups_arr = []
    group_counter = start_number
    # print(start_number)
    stroka = group[EXPRESSION]
    while stroka:
        print("STR: ", stroka)
        match_obj = re.search(r"([^()*|]+\**)|(\(.+\)\**)", stroka)
        if not match_obj:
            if stroka == "|":
                is_or = True
            if stroka == ")|(":
                is_or = True
            break
        span = match_obj.span()
        print("FINDED", match_obj.groups())
        child_str = re.sub(r"(^\()|(\){0,1}\*{0,1}$)", "", stroka[span[0]:span[1]])
        # print("CHILD:", child_str)
        if child_str:
            if stroka[span[0]:span[1]][-1] == "*":
                modification = True
            else:
                modification = False

            symbol_group = True
            for symbol in stroka[span[0]:span[1]]:
                if symbol in ("(", ")", "|"):
                    symbol_group = False

            finished = True
            for symbol in child_str:
                if symbol in ("(", ")", "|"):
                    finished = False
            # print(f"APPEND {child_str}\n")
            child = build_group_struct(group_counter, child_str,finished=finished,
                                       symbol_group=symbol_group, modification=modification)
            group_counter += 1
            groups_arr.append(child)
        stroka = stroka[0:span[0]] + stroka[span[1]:]

    return groups_arr, is_or


def create_groups(indata):
    groups_arr = []
    group_counter = 1
    unfinished_counter = 1
    groups_arr.append(build_group_struct(0, indata))
    children = []
    while unfinished_counter != 0:
        unfinished_counter = 0
        for group in groups_arr:
            if not group[FINISHED]:
                children_finded, is_or = find_children(group, start_number=group_counter)
                group_counter += len(children_finded)
                unfinished_counter += 1
                children.extend(children_finded)
                group[FINISHED] = True
                for child in children_finded:
                    group[CHILDREN].append(child[NUMBER])
                if is_or:
                    for group_i in groups_arr:
                        if group_counter - 1 in group_i[CHILDREN]:
                            group_i[OR] = True
                            break
        groups_arr.extend(children)
        children = []

    for g in groups_arr:
        print(g)
    return groups_arr


def get_output(groups, index):
    args = []
    func_arr = []
    append_Or = groups[index][OR]
    if append_Or:
        func_arr.append(Or)

    if groups[index][MODIFICATION] and not groups[index][SYMBOL_GROUP]:
        func_arr.append(ZeroOrMore)

    if len(groups[index][CHILDREN]) != 0:
        for child_ind in groups[index][CHILDREN]:
            args.append(get_output(groups, child_ind))
    else:
        args = [Normal(symbol) if symbol != "." else Any() for symbol in groups[index][EXPRESSION]]

    if groups[index][MODIFICATION] and groups[index][SYMBOL_GROUP]:
        args[-1] = ZeroOrMore(args[-1])

    if len(args) == 1:
        args = args[0]
    elif not append_Or:
        args = Str(args)
    output = args
    for func in func_arr:
        if func == Or:
            output = Or(args[0], args[1])
        else:
            output = func(output)
    return output


def parse_regexp(indata):
    print("INPUT:", indata)
    if not is_correct_input(indata):
        return None
    groups = create_groups(indata)

    output = get_output(groups, 0)
    print("OUTPUT:", output)
    print("#####################################################")
    return output





str_list = ['a*b',
            'a*b*ab',
            # "6UW!\x0b[3sMA8\x0cd\t9:P{17QuBb\nTF(K5)`@ J~}i",
            # "(a.*)|(bb)",
            # "a.*",
            # "(((aa)|ab)*|a)*",
            # "(((aa)|ab)|a)*",
            # ".",
            # "a",
            # "a|b",
            # "a*",
            # "(a)",
            # "(a)*",
            # "(a|b)*",
            # "a|b*",
            # "abcd",
            # "ab|cd",
            # "((aa)|ab)*|a",
            # "((a.)|.b)*|a",
            # "ab*",
            # "(ab)*",
            # "ab|a",
            # "a(b|a)",
            # "a|b*",
            ]

for string in str_list:
    parse_regexp(string)
