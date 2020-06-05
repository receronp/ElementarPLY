import logging
import ply.lex as lex

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

# List of token names. This is always required.
tokens = [
    "ID",
    "VALUE",
    "STR",
    "WRD",
    "DOT",
    "COMMA",
    "COLON",
    "ASSIGN",
    "LPAREN",
    "RPAREN",
    "LBRKT",
    "RBRKT",
    "QUOTE",
    "PLUS",
    "TIMES",
    "MINUS",
    "DIVIDE",
    "MODULO",
    "GT",
    "GE",
    "LT",
    "LE",
    "EQ",
    "NE",
    "AND",
    "OR",
    "NOT",
    "BTAND",
    "BTOR",
    "BTNOT",
    "COMMENT",
    "newline",
]

# Dictionary of reserved words.
reserved = {
    "programm": "PROGRAMM",
    "schluss": "SCHLUSS",
    "dim": "DIM",
    "word": "WORD",
    "float": "FLOAT",
    "string": "STRING",
    "als": "ALS",
    "begin": "BEGIN",
    "ende": "ENDE",
    "wenn": "WENN",
    "swenn": "SWENN",
    "dann": "DANN",
    "sonnst": "SONNST",
    "break": "BREAK",
    "wahrend": "WAHREND",
    "tun": "TUN",
    "fur": "FUR",
    "ein": "EIN",
    "aus": "AUS",
    "sub": "SUB",
    "gsub": "GSUB",
    "rukkher": "RUKKHER",
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens.
t_ASSIGN = r"="
t_COMMA = r","
t_DOT = r"\."
t_COLON = r"\:"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRKT = r"\["
t_RBRKT = r"\]"
t_GT = r">"
t_GE = r">="
t_EQ = r"=="
t_NE = r"!="
t_LT = r"<"
t_LE = r"<="
t_AND = r"&&"
t_OR = r"\|\|"
t_NOT = r"!"
t_BTAND = r"&"
t_BTOR = r"\|"
t_BTNOT = r"~"

# error appeared using r' \t' that removed letter t at the beginning of an ID name.
# t_ignore  = r' \t'
t_ignore = " \t"
t_ignore_COMMENT = r"//.*"
t_ignore_QUOTE = r"\""


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")  # Check for reserved words.
    return t


def t_VALUE(t):
    r"(-?[\d]*[\.][\d]+)|-?\d+"
    if str(t).find(".") != -1:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


def t_WRD(t):
    r"-?(\d+\.?(\d+)?)"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_STR(t):
    r'["][\\a-zA-Z 0-9:!@#$%^&*()\-+=/?<>,\.\[\]]+["]'
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling rule.
def t_error(t):
    logging.error("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)


# Build the lexer.
lexer = lex.lex()
