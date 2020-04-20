"""
elementar.py

Lexicon and syntaxis analyzer for Elementar language.
Author: Raul Eugenio Ceron Pineda
ID: A00823906
"""
import logging
import json
import ply.lex as lex
import ply.yacc as yacc

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

variable_table = {}
subroutine_table = {}
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
    'ID', 'VALUE', "STR", "FLT", "DOT", 'COMMA','COLON', 'ASSIGN', 
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

def t_FLT(t):
    r'\d+\.\d+'
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
    | AUS LPAREN E OUTPUT RPAREN
    | GSUB ID
    | WENN CONDITION DANN S SW SD ENDE
    | WAHREND CONDITION S ENDE
    | TUN S WAHREND CONDITION
    |
    """
    if len(p) > 1 and p[2] == '=':
        if current_var in variable_table and variable_table[current_var]['dimension'] == 0:
            variable_table[current_var]['value'] = 1    # Have to evaluate expression

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
    CONDITION : LPAREN CMP COMPARATOR CMP RPAREN
    | CONDITION AND CONDITION
    | CONDITION OR CONDITION
    """

def p_CMP(p):
    """
    CMP : VALUE
    | IDORAMC
    | FLT
    """
def p_COMPARATOR(p):
    """
    COMPARATOR : GT
    | GE
    | EQ
    | NE
    | LE
    | LT
    """

def p_SW(p):
    """
    SW : SWENN CONDITION DANN S SW
    |
    """

def p_SD(p):
    """
    SD : SONNST DANN S
    |
    """

def p_E(p):
    """
    E : VALUE
    | FLT
    | STR
    | EIDORAMC
    | VALUE OPERATOR E
    | FLT OPERATOR E
    | STR OPERATOR E
    | IDORAMC OPERATOR E
    """

def p_OPERATOR(p):
    """
    OPERATOR : PLUS
    | TIMES
    | MINUS
    | DIVIDE
    | MODULO
    """

def p_INPUT(p):
    """
    INPUT : COMMA IDORAMC INPUT
    |
    """

def p_OUTPUT(p):
    """
    OUTPUT : COMMA E OUTPUT
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
    with open("main.el", 'r') as el_file:
        ein = ""
        for line in el_file:
            ein += line
        parser.parse(ein)
        with open('./data_tables/variable_table.json', 'w') as out:
            out.write(json.dumps(variable_table, indent=2))
        with open('./data_tables/subroutine_table.json', 'w') as out:
            out.write(json.dumps(subroutine_table, indent=2))
except:
    print("Error")
