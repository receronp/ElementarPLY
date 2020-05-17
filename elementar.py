"""
elementar.py

Lexicon and syntaxis analyzer for Elementar language.
Author: Raul Eugenio Ceron Pineda
ID: A00823906
"""
import sys
import json
import logging
import ply.lex as lex
import ply.yacc as yacc

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

variable_table = {}
subroutine_table = {}
# expression_stack = []
operator_stack = []
jump_stack = []
jump_stack_count = []
temp_stack = [[f"T{x}", None] for x in range (10)]
current_type = None
current_var  = None
dimension_args = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    'size' : { 'size_x' : 0, 'size_y' : 0, 'size_z' : 0 }
}

def reset_current():
    global dimension_args
    global current_type
    current_type = None
    for dimension in range(4):
        dimension_args[dimension] = 0
    for each_size in dimension_args['size']:
        dimension_args['size'][each_size] = 0

def get_dimension():
    if dimension_args[3] == 1: return 3
    elif dimension_args[2] == 1: return 2
    elif dimension_args[1] == 1 : return 1
    else: return 0    

def assign_variable(production_array):
    dimension = get_dimension()
    variable_table[production_array] = {    'type' : current_type,
                                            'dimension' : dimension
                                        }
    if dimension == 0:
        variable_table[production_array]['value'] = None
    elif dimension == 1:
        size = dimension_args['size']['size_x']
        variable_table[production_array]['size'] = size
        variable_table[production_array][0] = [None] * size
    elif dimension == 2:
        size_x = dimension_args['size']['size_x']
        size_y = dimension_args['size']['size_y']
        variable_table[production_array]['size_x'] = size_x
        variable_table[production_array]['size_y'] = size_y
        for each_row in range(size_x):
            variable_table[production_array][each_row] = [None] * size_y

    elif dimension == 3:
        size_x = dimension_args['size']['size_x']
        size_y = dimension_args['size']['size_y']
        size_z = dimension_args['size']['size_z']
        variable_table[production_array]['size_x'] = size_x
        variable_table[production_array]['size_y'] = size_y
        variable_table[production_array]['size_z'] = size_z
        for each_row in range(size_x):
            variable_table[production_array][each_row] = [None] * size_y
            for each_col in range(size_y):
                variable_table[production_array][each_row][each_col] = [None] * size_z

# List of token names. This is always required.
tokens = [
    'ID', 'VALUE', "STR", "WRD", "FLT", "DOT", 'COMMA','COLON', 'ASSIGN', 
    'LPAREN', 'RPAREN', 'LBRKT', 'RBRKT', 'QUOTE',
    'PLUS', 'TIMES', 'MINUS', 'DIVIDE', 'MODULO',
    'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'AND', 'OR', 'NOT', 
    'BTAND', 'BTOR', 'BTNOT', 'COMMENT', 'newline',
]

# Dictionary of reserved words.
reserved = {
    'programm' : 'PROGRAMM',
    'schluss' : 'SCHLUSS',
    'dim' : 'DIM',
    'word' : 'WORD',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'als' : 'ALS',
    'begin' : 'BEGIN',
    'ende' : 'ENDE',
    'wenn' : 'WENN',
    'swenn' : 'SWENN',
    'dann' : 'DANN',
    'sonnst' : 'SONNST',
    'break' : 'BREAK',
    'wahrend' : 'WAHREND',
    'tun' : 'TUN',
    'fur' : 'FUR',
    'ein' : 'EIN',
    'aus' : 'AUS',
    'sub' : 'SUB',
    'gsub' : 'GSUB',
    'rukkher' : 'RUKKHER'
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens.
t_ASSIGN = r'='
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r'\:'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MODULO = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRKT = r'\['
t_RBRKT = r'\]'
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_LE = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_BTAND = r'&'
t_BTOR = r'\|'
t_BTNOT = r'~'

# error appeared using r' \t' that removed letter t at the beginning of an ID name.
# t_ignore  = r' \t'
t_ignore  = ' \t'
t_ignore_COMMENT = 	r'//.*'
t_ignore_QUOTE  = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words.
    return t

def t_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_WRD(t):
    r'-?(\d+\.?(\d+)?)'
    t.value = float(t.value) if  "." in t.value else int(t.value)
    return t

def t_FLT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_STR(t):
	r'["][\\a-zA-Z 0-9:!@#$%^&*()\-+=/?<>,]+["]'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule.
def t_error(t):
    logging.error("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)

# Build the lexer.
lexer = lex.lex()


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
    B : BEGIN S
    """

def p_S(p):
    """
    S : S0 S
    |
    """
    
def p_S0(p):
    """
    S0 : IDORAMC ASSIGN E
    | EIN LPAREN IDORAMC INPUT RPAREN
    | AUS LPAREN EXP OUTPUT RPAREN
    | GSUB ID
    | WE SD END
    | WAH END
    | TUN S WAHREND CONDITION
    |
    """
    # | WENN CONDITION DANN S SW SD ENDE
    # print(expression_stack)
    if len(p) > 1 and p[2] == '=':
        if current_var in variable_table and variable_table[current_var]['dimension'] == 0:
            result = operator_stack[0]
            if type(result) == list:
                temp_stack.append(result)
                result = result[1]
            elif type(result) == str and result in variable_table:
                result = variable_table[result]["value"]
            operator_stack.pop()
            variable_table[current_var]['value'] = result    # Have to evaluate expression
            if len(jump_stack) > 0:
                jump_stack.append([p[2], current_var, result])
            # print(f"{p[2]} {current_var} {result}")
        else:
            logging.error("Undeclared variable.")
            operator_stack.clear()
    # expression_stack.clear()

def p_E(p):
    """
    E : T
    | E PLUS T
    | E MINUS T
    """
    if len(p) > 2 :
        result, operator1, operator2 = get_operators()
        result[1] = operator1 + operator2 if p[2] == "+" else operator1 - operator2
        operator_stack.append(result)
        jump_stack.append([p[2], operator1, operator2])
        # print(f"{p[2]} {operator1} {operator2} {result}")

def get_operators():
        # expression_stack.append(p[2])
        operator2 = operator_stack.pop()
        if type(operator2) == list: 
            temp_stack.append(operator2)
            operator2 = operator2[1]
        elif type(operator2) == str and operator2 in variable_table:
            operator2 = variable_table[operator2]["value"]
        operator1 = operator_stack.pop()
        if type(operator1) == list: 
            temp_stack.append(operator1)
            operator1 = operator1[1]
        elif type(operator1) == str and operator1 in variable_table:
            operator1 = variable_table[operator1]["value"]
        return temp_stack.pop(), operator1, operator2

def p_T(p):
    """
    T : F
    | T TIMES F
    | T DIVIDE F
    |
    """
    # | MODULO
    if len(p) > 2 :
        result, operator1, operator2 = get_operators()
        result[1] = operator1 * operator2 if p[2] == "*" else operator1 / operator2
        operator_stack.append(result)
        jump_stack.append([p[2], operator1, operator2])
        # print(f"{p[2]} {operator1} {operator2} {result}")

def p_F(p):
    """
    F : ID
    | VALUE
    | FLT
    | LPAREN E RPAREN
    |
    """
    # | WRD
    if len(p) < 3:    
        # expression_stack.append(p[1])
        operator_stack.append(p[1])

def p_EXP(p):
    """
    EXP : 
    """
#     EXP : VALUE
#     | FLT
#     | STR
#     | EIDORAMC
#     | VALUE OPERATOR EXP
#     | FLT OPERATOR EXP
#     | STR OPERATOR EXP
#     | IDORAMC OPERATOR EXP
#     """

def p_IDORAMC(p):
    """
    IDORAMC : ID
    | ID AMC1
    """
    global current_var
    current_var = p[1]

def p_EIDORAMC(p):
    """
    EIDORAMC : ID
    | ID AMC1
    """

def p_CONDITION(p):
    """
    CONDITION : CONDITION AND CONDITION1
    | CONDITION OR CONDITION1
    | CONDITION1
    """
    if len(p) > 2:
        result, operator1, operator2 = get_operators()
        result[1] = operator1 and operator2 if p[2] == "&&" else operator1 or operator2
        operator_stack.append(result)
        jump_stack.append([p[2], operator1, operator2])
 
def p_CONDITION1(p):
    """
    CONDITION1 : LPAREN CMP GT CMP RPAREN
    | LPAREN CMP GE CMP RPAREN
    | LPAREN CMP EQ CMP RPAREN
    | LPAREN CMP NE CMP RPAREN
    | LPAREN CMP LE CMP RPAREN
    | LPAREN CMP LT CMP RPAREN
    """
    result, operator1, operator2 = get_operators()
    if p[3] == ">":
        result[1] = operator1 > operator2
    elif p[3] == ">=":
        result[1] = operator1 >= operator2
    elif p[3] == "==":
        result[1] = operator1 == operator2
    elif p[3] == "!=":
        result[1] = operator1 != operator2
    elif p[3] == "<=":
        result[1] = operator1 <= operator2
    elif p[3] == "<":
        result[1] = operator1 < operator2
        
    operator_stack.append(result)
    jump_stack.append([p[3], operator1, operator2])
    # print(jump_stack[-1])

def p_CMP(p):
    """
    CMP : VALUE
    | ID
    | FLT
    """
    if type(p[1]) == str and p[1] in variable_table:
        operator_stack.append(variable_table[p[1]]["value"])
    else:
        operator_stack.append(p[1])

def p_WAH(p):
    """
    WAH : WAH0 WAH1 GZ
    """

def p_WAH0(p):
    """
    WAH0 : WAHREND CONDITION
    """
    result = operator_stack.pop()
    result[1] = not result[1]
    jump_stack.append(["Gzf", result.copy(), None])
    jump_stack_count.append(len(jump_stack) - 1)
    temp_stack.append(result)

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
    jump_stack_count.append(len(jump_stack)-1)

def p_WE(p):
    """
    WE : WE0 WE1 GZ
    """

def p_WE0(p):
    """
    WE0 : WENN CONDITION
    """
    result = operator_stack.pop()
    result[1] = not result[1]
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

def p_INPUT(p):
    """
    INPUT : COMMA IDORAMC INPUT
    |
    """

def p_OUTPUT(p):
    """
    OUTPUT : COMMA EXP OUTPUT
    |
    """

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
    if len(p) > 1 : 
        dimension_args['size']['size_x'] = p[2]

def p_AMC2(p):
    """
    AMC2 : LBRKT VALUE RBRKT AMC3
    | LBRKT ID RBRKT AMC3
    | LBRKT VALUE RBRKT
    | LBRKT ID RBRKT
    |
    """
    dimension_args[2] = 1
    if len(p) > 1 : 
        dimension_args['size']['size_y'] = p[2]
    
def p_AMC3(p):
    """
    AMC3 : LBRKT VALUE RBRKT 
    | LBRKT ID RBRKT
    |
    """
    dimension_args[3] = 1
    if len(p) > 1 : 
        dimension_args['size']['size_z'] = p[2]


# Error handling rule.
def p_error(p):
    logging.error("Failed at line {}.".format(str(p.lineno)))

parser = yacc.yacc()

try:
    with open("while.el", 'r') as el_file:
        ein = ""
        for line in el_file:
            ein += line
        parser.parse(ein)
    with open('./data_tables/variable_table.json', 'w') as var_output:
        var_output.write(json.dumps(variable_table, indent=2))
    with open('./data_tables/subroutine_table.json', 'w') as subprocess_output:
        subprocess_output.write(json.dumps(subroutine_table, indent=2))
    with open('./data_tables/jump_stack.json', 'w') as jump_stack_output:
        jump_stack_output.write(json.dumps(jump_stack, indent=2))
except:
    e = sys.exc_info()[0]
    print(e)
