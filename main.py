import os

UNCLASS_DIR = r"C:\Users\Максим\Desktop\ClassificationNPA\Unclassified"
MODIF_DIR = r"C:\Users\Максим\Desktop\ClassificationNPA\Modifying"
INFOR_DIR = r"C:\Users\Максим\Desktop\ClassificationNPA\Informative"

file_list = os.listdir(UNCLASS_DIR)

for ind, file_name in enumerate(file_list):
    print(file_name)
    changing = False
    file_path = os.path.join(UNCLASS_DIR, file_name)





    # with open(file_path, "r") as file:
    #     for line in file:
    #         if "утвердить прилагаемые изменения" in line or \
    #            "Утвердить прилагаемые изменения" in line:
    #             informative = True
    #             break
    # if informative:
    #     os.replace(file_path, os.path.join(INFOR_DIR, file_name))
    #     print("Is INFORMATIVE")




    with open(file_path, "r") as file:
        counter = 0
        for line in file:
            counter += 1
            print(line)
            if counter >= 100:
                break
    print('FILE_NUM', ind + 1)
    user_input = input()
    if user_input == "i":
        os.replace(file_path, os.path.join(INFOR_DIR, file_name))
        print("Is INFORMATIVE")
    if user_input == "m":
        os.replace(file_path, os.path.join(MODIF_DIR, file_name))
        print("Is MODIFYING")
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')




    # with open(file_path, "r") as file:
    #     for line in file:
    #         if "О внесении изменений" in line or \
    #            "О внесении изменения" in line:
    #             changing = True
    #             break
    # if not changing:
    #     os.replace(file_path, os.path.join(INFOR_DIR, file_name))
    #     print("Is INFORMATIVE")
    # else:
    #     os.replace(file_path, os.path.join(MODIF_DIR, file_name))
    #     print("Is MODIFYING")





















# import re
#
#
# def calc(expression):
#     print("CALC_IN:", expression)
#     expression = expression.replace(' ', '')
#     # expression = expression.replace('--', '+')
#     # expression = expression.replace('+-', '-')
#     mo = re.search(r"-*\([^()]+\)", expression)
#     while mo:
#         result = primitive_calc(mo.group(0))
#         # print("EXPRESSION_BEFORE:", expression)
#         expression = expression[:mo.start()] + result + expression[mo.end():]
#         # print("EXPRESSION_AFTER:", expression)
#         mo = re.search(r"\([^()]+\)", expression)
#
#     result = primitive_calc(expression)
#
#     # print("CALC_OUT:", result)
#     return float(result)
#
#
# def operate(num_1, num_2, operation):
#     if operation == "*":
#         return float(num_1) * float(num_2)
#     elif operation == "/":
#         return float(num_1) / float(num_2)
#     elif operation == "+":
#         return float(num_1) + float(num_2)
#     elif operation == "-":
#         return float(num_1) - float(num_2)
#
#
# def primitive_calc(expression):
#     # print("-------------------------------------")
#     # print('IN:', expression)
#     minus_mod = False
#     if "-(" in expression:
#         minus_mod = True
#         expression = expression[1:]
#     if expression[0] == "(":
#         expression = expression[1:-1]
#     # expression = expression.replace('--', '+')
#     # expression = expression.replace('+-', '-')
#
#     oper_regs = [r'\*|/', r'\+|-']
#     for oper_reg in oper_regs:
#         # mo_1 = re.search(fr'(-*[^-+*/]+)({oper_reg})', expression)
#         mo_1 = re.search(fr'(-[^-+*/]+)|([^-+*/]+)({oper_reg})', expression)
#         mo_2 = None
#         if mo_1:
#             mo_2 = re.search(fr'(-{0,1}[^-+*/]+)', expression[mo_1.end():])
#             # print("MO_1:", mo_1.groups())
#             # print("MO_2:", mo_2.groups())
#         while mo_1 and mo_2:
#             result = operate(num_1=mo_1.group(1), num_2=mo_2.group(1), operation=mo_1.group(2))
#             # expression = expression.replace(mo_1.group(0) + mo_2.group(0), str(result))
#             expression = expression[:mo_1.start()] + str(result) + expression[mo_1.end()+ mo_2.end():]
#             # print("@@@", expression)
#             mo_1 = re.search(fr'([^-+*/]+)({oper_reg})', expression)
#             mo_2 = None
#             if mo_1:
#                 mo_2 = re.search(fr'([^-+*/]+)', expression[mo_1.end():])
#                 # print("MO_1:", mo_1.groups())
#                 # print("MO_2:", mo_2.groups())
#     # print('OUT:', expression)
#     if minus_mod:
#         expression = "-" + expression
#         # expression = expression.replace('--', '+')
#     return expression
#
#
# arr = [
#         # '(2-2.4*7*5)',
#         "4-(-4)",
#         # "(2+2)/(3+3)",
#         # "(2/(2+3.33/5)*4)--6-8+11",
#       ]
#
# # for s in arr:
# #     calc(s)
#
# # for s in arr:
# #     primitive_calc(s)
#
# # mo = re.search(fr'(\d+\.*\d*)({oper_reg})(\d+\.*\d*)', expression)
# # mo = re.search(fr'([^-+*/]+)({oper_reg})([^-+*/]+)', expression)
# # print(re.sub(fr'(2-2.4*7*5)', "0", '(2-2.4*7*5)'))
#
# cases = (
#     # ("1 + 1", 2),
#     # ("8/16", 0.5),
#     # ("3 -(-1)", 4),
#     # ("2 + -2", 0),
#     # ("10- 2- -5", 13),
#     # ("(((10)))", 10),
#     # ("3 * 5", 15),
#     # ("-7 * -(6 / 3)", 14),
#     ("40 - -21 - -57 / -48 * 78 - 99 - -86 - 62", 106.625),
# )
#
# for case in cases:
#     print(calc(case[0]), case[1])
#
