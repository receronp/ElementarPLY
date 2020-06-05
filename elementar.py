"""
elementar.py

Lexicon and syntaxis analyzer for Elementar language.
Author: Raul Eugenio Ceron Pineda
ID: A00823906
"""
import sys
import logging
import json
import ply.yacc as yacc
from elexer import tokens

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

str_output = ""
variable_table = {}
subroutine_table = {}
# expression_stack = []
operator_stack = []
jump_stack = []
jump_stack_count = []
while_stack_count = []
temp_stack = [[f"{x}", None] for x in range(10)]
current_type = None
current_var = None
current_x = None
current_y = None
current_z = None
current_var_e = None
current_x_e = None
current_y_e = None
current_z_e = None

dimension_args = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    "size": {"size_x": 0, "size_y": 0, "size_z": 0},
}


def reset_current():
    global dimension_args
    global current_type
    current_type = None
    for dimension in range(4):
        dimension_args[dimension] = 0
    for each_size in dimension_args["size"]:
        dimension_args["size"][each_size] = 0


def get_dimension():
    if dimension_args[3] == 1:
        return 3
    elif dimension_args[2] == 1:
        return 2
    elif dimension_args[1] == 1:
        return 1
    else:
        return 0


def assign_variable(production_array):
    dimension = get_dimension()
    variable_table[production_array] = {"type": current_type, "dimension": dimension}
    if dimension == 0:
        variable_table[production_array]["value"] = None
    elif dimension == 1:
        size = dimension_args["size"]["size_x"]
        variable_table[production_array]["size"] = size
        variable_table[production_array][0] = [None] * size
    elif dimension == 2:
        size_x = dimension_args["size"]["size_x"]
        size_y = dimension_args["size"]["size_y"]
        variable_table[production_array]["size_x"] = size_x
        variable_table[production_array]["size_y"] = size_y
        for each_row in range(size_x):
            variable_table[production_array][each_row] = [None] * size_y

    elif dimension == 3:
        size_x = dimension_args["size"]["size_x"]
        size_y = dimension_args["size"]["size_y"]
        size_z = dimension_args["size"]["size_z"]
        variable_table[production_array]["size_x"] = size_x
        variable_table[production_array]["size_y"] = size_y
        variable_table[production_array]["size_z"] = size_z
        for each_row in range(size_x):
            variable_table[production_array][each_row] = [None] * size_y
            for each_col in range(size_y):
                variable_table[production_array][each_row][each_col] = [None] * size_z


def add_operators(action):
    result, operator1, operator2 = get_operators()
    operator_stack.append(result)
    jump_stack.append([action, result, operator1, operator2])


def get_operators():
    # expression_stack.append(p[2])
    operator2 = operator_stack.pop()
    if type(operator2) == list:
        if operator2[0] not in variable_table:
            temp_stack.append(operator2)
    operator1 = operator_stack.pop()
    if type(operator1) == list:
        if operator1[0] not in variable_table:
            temp_stack.append(operator1)
    return temp_stack.pop(), operator1, operator2


######################## YACC PROGRAM ###########################

# Yacc expressions.
def p_program(p):
    """
    program : PROGRAMM V R B SCHLUSS
    """
    print("SUCCESS: No errors found in syntax.")


def p_V(p):
    """
    V : V0 V
    |
    """


def p_V0(p):
    """
    V0 : DIM ID V1
    | DIM ID V2
    """
    assign_variable(p[2])


def p_V1(p):
    """
    V1 : COMMA ID V1
    | COMMA ID V2
    """
    assign_variable(p[2])


def p_V2(p):
    """
    V2 : ALS TYPE AMC0
    """


def p_R(p):
    """
    R : R0 COLON B RUKKHER R 
    |
    """


def p_R0(p):
    """
    R0 : SUB ID
    """
    subroutine_table[p[2]] = p.lexer.lineno


def p_B(p):
    """
    B : B1 S
    """


def p_B1(p):
    """
    B1 : BEGIN
    """
    jump_stack.append(["Gz", 1])


def p_S(p):
    """
    S : S0 S
    |
    """


def p_S0(p):
    """
    S0 : IDORAMC ASSIGN E
    | IN NON
    | OUT NON
    | GSUB ID
    | WE SD END
    | WAH ENDE
    | TUN S WAHREND CONDITION
    |
    """
    # | WENN CONDITION DANN S SW SD ENDE
    # print(expression_stack)
    if len(p) > 1 and p[2] == "=":
        if (
            current_var in variable_table
            and variable_table[current_var]["dimension"] == 0
        ):
            result = operator_stack[0]
            if type(result) == list and result[0] not in variable_table:
                temp_stack.append(result)
            operator_stack.pop()
            jump_stack.append([p[2], current_var, result])
            # print(f"{p[2]} {current_var} {result}")
        elif (
            current_var in variable_table
            and variable_table[current_var]["dimension"] == 1
        ):
            result = operator_stack[0]
            if type(result) == list:
                temp_stack.append(result)
            operator_stack.pop()
            jump_stack.append([p[2], current_var, result, current_x])
        elif (
            current_var in variable_table
            and variable_table[current_var]["dimension"] == 2
        ):
            result = operator_stack[0]
            if type(result) == list:
                temp_stack.append(result)
            operator_stack.pop()
            jump_stack.append([p[2], current_var, result, current_x, current_y])
        elif (
            current_var in variable_table
            and variable_table[current_var]["dimension"] == 3
        ):
            result = operator_stack[0]
            if type(result) == list:
                temp_stack.append(result)
            operator_stack.pop()
            jump_stack.append(
                [p[2], current_var, result, current_x, current_y, current_z]
            )
        else:
            logging.error("Undeclared variable.")
            operator_stack.clear()
    # expression_stack.clear()


def p_NON(p):
    """
    NON :
    """


def p_E(p):
    """
    E : T
    | E PLUS T
    | E MINUS T
    """
    if len(p) > 2:
        add_operators(p[2])


def p_T(p):
    """
    T : F
    | T TIMES F
    | T DIVIDE F
    | T MODULO F
    |
    """
    if len(p) > 2:
        add_operators(p[2])


def p_F(p):
    """
    F : IDORAMCE
    | VALUE
    | FLT
    | LPAREN E RPAREN
    |
    """
    # | WRD
    if len(p) < 3:
        if p[1] == None:
            operator_stack.append(
                [current_var_e, current_x_e, current_y_e, current_z_e]
            )
        else:
            # expression_stack.append(p[1])
            operator_stack.append(p[1])


def p_IDORAMC(p):
    """
    IDORAMC : ID
    | ID AMC1A
    """
    global current_var
    current_var = p[1]


def p_AMC1A(p):
    """
    AMC1A : LBRKT VALUE RBRKT AMC2A
    | LBRKT ID RBRKT AMC2A
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    global current_x
    current_x = p[2]


def p_AMC2A(p):
    """
    AMC2A : LBRKT VALUE RBRKT AMC3A
    | LBRKT ID RBRKT AMC3A
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    global current_y
    current_y = p[2]


def p_AMC3A(p):
    """
    AMC3A : LBRKT VALUE RBRKT 
    | LBRKT ID RBRKT
    |
    """
    global current_z
    current_z = p[2]


def p_IDORAMCE(p):
    """
    IDORAMCE : ID
    | ID AMC1AE
    """
    global current_var_e
    current_var_e = p[1]


def p_AMC1AE(p):
    """
    AMC1AE : LBRKT VALUE RBRKT AMC2AE
    | LBRKT ID RBRKT AMC2AE
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    global current_x_e
    current_x_e = p[2]


def p_AMC2AE(p):
    """
    AMC2AE : LBRKT VALUE RBRKT AMC3AE
    | LBRKT ID RBRKT AMC3AE
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    global current_y_e
    current_y_e = p[2]


def p_AMC3AE(p):
    """
    AMC3AE : LBRKT VALUE RBRKT 
    | LBRKT ID RBRKT
    |
    """
    global current_z_e
    current_z_e = p[2]


def p_CONDITION(p):
    """
    CONDITION : CONDITION AND CONDITION1
    | CONDITION OR CONDITION1
    | CONDITION1
    """
    if len(p) > 2:
        add_operators(p[2])


def p_CONDITION1(p):
    """
    CONDITION1 : LPAREN CMP GT CMP RPAREN
    | LPAREN CMP GE CMP RPAREN
    | LPAREN CMP EQ CMP RPAREN
    | LPAREN CMP NE CMP RPAREN
    | LPAREN CMP LE CMP RPAREN
    | LPAREN CMP LT CMP RPAREN
    """
    add_operators(p[3])
    # print(jump_stack[-1])   # Remove after test


def p_CMP(p):
    """
    CMP : VALUE
    | ID
    | FLT
    """
    operator_stack.append(p[1])


def p_WAH(p):
    """
    WAH : WAH0 WAH1 ENDW
    """


def p_WAH0(p):
    """
    WAH0 : WAHREND CONDITION
    """
    result = operator_stack.pop()
    # result[1] = not result[1]
    jump_stack.append(["Gzf", result.copy(), None])
    while_stack_count.append(len(jump_stack) - 1)
    temp_stack.append(result)


def p_ENDW(p):
    """
    ENDW :
    """
    jump_stack[while_stack_count[-1]][2] = len(jump_stack) + 1
    # print(jump_stack[jump_stack_count[-1]])
    jump_stack.append(["Gz", while_stack_count.pop() - 1])
    # jump_stack_count.append(len(jump_stack) - 1)


def p_WAH1(p):
    """
    WAH1 : S
    """


def p_GZ(p):
    """
    GZ :
    """
    jump_stack[jump_stack_count[-1]][2] = len(jump_stack) + 1
    # print(jump_stack[jump_stack_count[-1]])
    jump_stack_count.pop()
    jump_stack.append(["Gz", None])
    jump_stack_count.append(len(jump_stack) - 1)


def p_WE(p):
    """
    WE : WE0 WE1 GZ
    """


def p_WE0(p):
    """
    WE0 : WENN CONDITION
    """
    result = operator_stack.pop()
    # result[1] = not result[1]
    jump_stack.append(["Gzf", result.copy(), None])
    jump_stack_count.append(len(jump_stack) - 1)
    temp_stack.append(result)


def p_WE1(p):
    """
    WE1 : DANN S
    """


# def p_SW(p):
#     """
#     SW : SWENN CONDITION WE1 SW
#     |
#     """


def p_SD(p):
    """
    SD : SONNST WE1
    |
    """
    # print(p.lexer.lineno)


def p_END(p):
    """
    END : ENDE
    """
    if len(jump_stack[jump_stack_count[-1]]) < 3:
        jump_stack[jump_stack_count[-1]][1] = len(jump_stack)
    else:
        jump_stack[jump_stack_count[-1]][2] = len(jump_stack)
    # print(jump_stack[jump_stack_count[-1]])
    jump_stack_count.pop()


def p_IN(p):
    """
    IN : EIN LPAREN ID RPAREN
    """
    jump_stack.append(["EIN", p[3]])


def p_OUT(p):
    """
    OUT : AUS LPAREN ST0 RPAREN
    """
    global str_output
    jump_stack.append(["AUS", str_output])
    str_output = ""


def p_ST0(p):
    """
    ST0 : ST1
    | ST0 PLUS ST1
    | 
    """


def p_ST1(p):
    """
    ST1 : STR
    | ID
    """
    global str_output
    str_output += str(p[1])


def p_TYPE(p):
    """
    TYPE : WORD 
    | FLOAT 
    | STRING     
    """
    reset_current()
    global current_type
    current_type = p[1]


# Array, Matrix, and Cube
def p_AMC0(p):
    """
    AMC0 :  AMC1
    |
    """
    dimension_args[0] = 1


def p_AMC1(p):
    """
    AMC1 : LBRKT VALUE RBRKT AMC2
    | LBRKT ID RBRKT AMC2
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    dimension_args[1] = 1
    if len(p) > 1:
        dimension_args["size"]["size_x"] = p[2]


def p_AMC2(p):
    """
    AMC2 : LBRKT VALUE RBRKT AMC3
    | LBRKT ID RBRKT AMC3
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    dimension_args[2] = 1
    if len(p) > 1:
        dimension_args["size"]["size_y"] = p[2]


def p_AMC3(p):
    """
    AMC3 : LBRKT VALUE RBRKT 
    | LBRKT ID RBRKT
    |
    """
    dimension_args[3] = 1
    if len(p) > 1:
        dimension_args["size"]["size_z"] = p[2]


# Error handling rule.
def p_error(p):
    logging.error("Failed at line {}.".format(str(p.lineno)))


parser = yacc.yacc()


def parse(file):
    try:
        with open(file, "r") as el_file:
            ein = ""
            for line in el_file:
                ein += line
            parser.parse(ein)
    except:
        e = sys.exc_info()[0]
        print(e)

    with open("./data_tables/subroutine_table.json", "w") as subprocess_output:
        subprocess_output.write(json.dumps(subroutine_table, indent=2))
    with open("./data_tables/jump_stack.json", "w") as jump_stack_output:
        jump_stack_output.write(json.dumps(jump_stack, indent=2))
