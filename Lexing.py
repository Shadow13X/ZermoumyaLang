import ply.lex as lex
import re as re

letterCount = 0

reserved = {
    '_KTB'      : "PRINT",
    '_9RA'      : "SCAN",
    '_ILA'      : "IF",
    '_ILALA'    : "ELSE",
    '_LGA3'     : "FOR",
    '_KOLMA'    : "WHILE",
    '_7BS'      : "BREAK",
    '_KML'      : "CONTINUE",
    '_KHDMA'    : "FUNCTION",
    '_RJ3'      : "RETURN",
    '_WALOU'    : "NULL",
    '_JIB'      : "IMPORT"
}

tokens = [
    # Literals (identifier, integer constant, float constant, string constant)
    'RESERVED', 'ID', 'NUMBER', 'STRING', 'BOOLEAN',

    # Comments
    'COMMENT',

    # Arithmetic Operators (+, -, *, /, %, //, ++, --, +=, -=, *=, /=, //=, %=)
    'SUM', 'SUB', 'MUL', 'DIV', 'IDIV', 'MOD', 'INCR', 'DECR', 
    'SUM_ASS', 'SUB_ASS', 'MUL_ASS', 'DIV_ASS', 'IDIV_ASS', 'MOD_ASS',

    # Comparison Operators
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',

    # Assignment (=)
    'ASSIGN',

    # Logical Operators (||, &&, !)
    'LOR', 'LAND', 'LNOT',

    # Ternary Operator (?, :)
    'QUES', 'COLON',

    # Delimeters ( ) [ ] { } , . ;
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA',
    #'DOT',
    'SEMI',
    #IMPORT
    'FILENAME',
    # Other
    'NEWLINE',
] + list(reserved.values())

# Arithmetic Operators
t_SUM             = r'\+'
t_SUB            = r'\-'
t_MUL            = r'\*'
t_IDIV          = r'\/\/'
t_DIV           = r'\/'
t_MOD           = r'\%'
t_INCR        = r'\+\+'
t_DECR        = r'\-\-'
t_SUM_ASS          = r'\+\='
t_SUB_ASS          = r'\-\='
t_MUL_ASS          = r'\*\='
t_DIV_ASS          = r'\/\='
t_IDIV_ASS          = r'\/\/\='
t_MOD_ASS          = r'\%\='

# Logical Operators
t_LOR              = r'\|\|'
t_LAND             = r'\&\&'
t_LNOT             = r'\!'

# Comparison Operators
t_LT               = r'\<'
t_GT               = r'\>'
t_LE               = r'\<\='
t_GE               = r'\>\='
t_EQ               = r'\=\='
t_NE               = r'\!\='

# Ternary Operators
t_QUES             = r'\?'
t_COLON            = r'\:'

# Assignment operator
t_ASSIGN           = r'\='

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_SEMI            = r';'

# Boolean
def t_BOOLEAN(t):
    r'(_S7I7|_GHALT)'
    return t

# Identifier
def t_ID(t):
    r'[a-z]([_]?[A-Za-z0-9]+)*'
    return t

# Filename
def t_FILENAME(t):
    r'[_][a-z][A-Za-z0-9]*'
    return t
# Reserved
def t_RESERVED(t):
    r'[_][A-Z0-9]+'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t
# Number
def t_NUMBER(t):
    r'([-]?[0-9]+)(\.[0-9]+)?'
    try:
        t.value=int(t.value)
    except(ValueError):
        t.value=float(t.value)
    return t

# Comments
def t_COMMENT(t):
    r'(\#\# *.*)'
    return t

# String Literal 
def t_STRING(t):
    r'((\")([^\\\n]|(\\.))*?(\"))|((\')([^\\\n]|(\\.))*?(\'))'
    return t

# New line
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return None

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    if re.match(r'(\"|\')', t.value[0]):
        print("Unclosed string literal", t.value, "at line", t.lineno)
    else:
        print("Illegal character '%s'" % t.value[0], "at line", t.lineno)
    t.lexer.skip(1)

lexer=lex.lex()