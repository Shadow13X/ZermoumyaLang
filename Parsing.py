import ply.yacc as yacc
from Lexing import tokens

precedence = (
    ('nonassoc', 'LT', 'GT'),
    ('left', 'SUM', 'SUB'),
    ('left', 'MUL', 'DIV'),
)

# Program
def p_program(p):
    '''program : program statement
               | statement'''
    p[0]=p[1]
def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1
#### Statement -incomplete-
def p_statement(p):
    """statement : statement command
                 | command
            """
    p[0] = p[1]
def p_command(p):
    #done: i/o, ass, 
    """command : function_def
               | conditional
               | expression
               | assignment
               | expression_ass
               | input
               | output
               | for_loop
               | while_loop
               | return
               | break
               | continue
               | COMMENT
               | NEWLINE
               | import
            """
    p[0]=p[1]
######## Import
def p_import(p):
    '''import : IMPORT files
    '''
    p[0]=("IMPORT",tuple(p[2]))
def p_files(p):
    '''files : files COMMA FILENAME
             | FILENAME'''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
######## Assign
def p_assignment(p):
    '''assignment : ID ASSIGN expression
                  | ID ASSIGN LBRACKET list RBRACKET
            '''
    if len(p)==4:
        p[0] = ('ASS',(p[1],"var"),p[3])
    elif len(p)==6:
        p[0] = ('ASS',(p[1],"list"),("LIST",p[4]))
    elif len(p)==7:
        p[0] = ("ASS",(p[1],"list"),("LIST","vide"))
######## Input
def p_input(p):
    '''input : SCAN LPAREN ID RPAREN
            '''
    p[0] = ('SCAN',p[3])
######## Output
def p_output(p):
    '''output : PRINT LPAREN plist RPAREN
            '''
    a = []
    for i in p[3]:
        a.append(i)
    p[0] = ("PRINT",tuple(a))
def p_plist(p):
    '''plist : pitem
             | plist COMMA pitem
            '''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
def p_item_expr(p):
    '''pitem : expression'''
    p[0] = ("", p[1])  
######## Conditional
def p_condition(p):
    """condition : expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression NE expression
                 | expression EQ expression
                 | expression LAND expression
                 | expression LOR expression
                 | LNOT expression
                 | BOOLEAN
                """
    if(len(p)==4):
        p[0]=(p[2],p[1],p[3])
    elif(len(p)==3):
        p[0]=("LNOT",p[2])
    else:
        p[0]=("BOOL",p[1])
def p_ternary(p):
    'ternary_condition : LPAREN condition RPAREN QUES bloc COLON bloc'
    p[0] = ("TERNARY", p[2],p[5],p[7])
def p_if_bloc(p):
    """if_bloc : IF LPAREN condition RPAREN bloc"""
    p[0] = ("IFCOND", p[3], p[5])
def p_if_elif_bloc(p):
    """if_elif_bloc : if_elif_bloc ELSE if_bloc
                    | if_bloc"""
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
def p_conditional(p):
    """conditional : if_elif_bloc ELSE bloc
                   | if_elif_bloc
                """
    if(len(p)>3):
        p[0]=("COND", tuple(p[1]),tuple(p[3]))
    else:
        p[0]=("COND",tuple(p[1]))
def p_bloc(p):
    '''bloc : LBRACE stat_bloc RBRACE
        '''
    p[0]=("BLOC",tuple(p[2]))
def p_stat_bloc(p):
    '''stat_bloc : stat_bloc command
                 | command
            '''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]
######## DEF/CALL Function
def p_function_def(p):
    '''function_def : FUNCTION ID LPAREN param_list RPAREN bloc
                    | FUNCTION ID LPAREN RPAREN bloc'''
    if len(p)>6:
        p[0]=("FUNC_DEF",p[2],p[4],p[6])
    else:
        p[0]=("FUNC_DEF",p[2],None,p[5])
def p_function_call(p):
    '''function_call : ID LPAREN param_list_call RPAREN
                     | ID LPAREN RPAREN '''
    if len(p)>3:
        p[0]=("FUNC_CALL",p[1],p[3])
    else:
        p[0]=("FUNC_CALL",p[1],None)
def p_param_list_call(p):
    '''param_list_call : param_list_call COMMA param_call
                       | param_call
            '''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
def p_param_call(p):
    'param_call : factor'
    p[0] = p[1]
def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param
            '''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
def p_param(p):
    'param : ID'
    p[0] = (p[1], None)
def p_return(p):
    '''return : RETURN expression
    '''
    print(p[2])
    p[0] = ("RETURN",p[2])
######## LOOPS
def p_for_loop(p):
    """for_loop : FOR LPAREN assignment SEMI condition SEMI expression RPAREN bloc"""
    p[0]=("FOR", p[3], p[5], p[7], p[9])
def p_while_loop(p):
    """while_loop : WHILE LPAREN condition RPAREN bloc"""
    p[0]=("WHILE", p[3], p[5])
def p_continue(p):
    '''continue : CONTINUE
                | CONTINUE SEMI'''
    p[0] = ("CONTINUE",None)
def p_break(p):
    '''break : BREAK
             | BREAK SEMI'''
    p[0] = ("BREAK",None)
############ Expression
def p_binary_operators(p): 
    '''expression : expression SUM term
                  | expression SUB term
       term       : term MUL factor
                  | term DIV factor
                  | term IDIV factor
                  | term MOD factor
    '''
    if p[2] == '+':
        p[0] = ("SUM",p[1],p[3])
    elif p[2] == '-':
        p[0] = ("SUB",p[1],p[3])
    elif p[2] == '*':
        p[0] = ("MUL",p[1],p[3])
    elif p[2] == '/':
        p[0] = ("DIV",p[1],p[3])
    elif p[2] == '//':
        p[0] = ("IDIV",p[1],p[3])
    elif p[2] == '%':
        p[0] = ("MOD",p[1],p[3])
def p_unary_operators(p): 
    '''expression : expression DECR
                  | expression INCR
    '''
    if p[2] == '++':
        p[0] = ("ASS",(p[1][1][0],"var"), ("SUM",p[1],("NUMBER",1)))
    elif p[2] == '--':
        p[0] = ("ASS",(p[1][1][0],"var"), ("SUB",p[1],("NUMBER",1)))
def p_unary_operators(p): 
    '''expression : expression DECR
                  | expression INCR
    '''
    if p[2] == '++':
        p[0] = ("SUM",p[1],("NUMBER",1))
    elif p[2] == '--':
        p[0] = ("SUB",p[1],("NUMBER",1))
def p_binary_operators_ass(p): 
    '''expression_ass : ID SUM_ASS expression
                      | ID SUB_ASS expression
                      | ID MUL_ASS expression
                      | ID DIV_ASS expression
                      | ID IDIV_ASS expression
                      | ID MOD_ASS expression
    '''
    if p[2] == '+=':
        p[0] = ("ASS",(p[1], 'var'), ('SUM', ('VAR', (p[1], None)),p[3]))
    elif p[2] == '-=':
        p[0] = ("ASS",(p[1], 'var'), ("SUB",('VAR', (p[1], None)),p[3]))
    elif p[2] == '*=':
        p[0] = ("ASS",(p[1], 'var'), ("MUL",('VAR', (p[1], None)),p[3]))
    elif p[2] == '/=':
        p[0] = ("ASS",(p[1], 'var'), ("DIV",('VAR', (p[1], None)),p[3]))
    elif p[2] == '//=':
        p[0] = ("ASS",(p[1], 'var'), ("IDIV",('VAR', (p[1], None)),p[3]))
    elif p[2] == '%=':
        p[0] = ("ASS",(p[1], 'var'), ("MOD",('VAR', (p[1], None)),p[3]))
def p_expression(p):
    """expression : condition
                  | ternary_condition
                  | term
                  | NULL
                  | function_call
            """
    p[0] = p[1]
def p_term_factor(p):
    """term : factor
    """
    p[0] = p[1]
def p_factor_num(p):
    """factor : NUMBER
              | ID
              | STRING 
              | ID LBRACKET expression RBRACKET
        """
    # float(tmp)
    # try:
    #     if(float(tmp)==int(tmp)):
    #         var[str(expr[1])] = [int(tmp)]
    # except ValueError:
    #     var[str(expr[1])] = [float(tmp)]
    if(isinstance(p[1], int) or isinstance(p[1], float)):
        p[0] = ("NUMBER",p[1])
    elif(p[1][0]=="'" or p[1][0]=='"'):
        p[0] = ("STRING",p[1])
    else:
        if len(p)<3:
            p[0]=("VAR",(p[1],None))
        else:
            p[0]=("VAR",(p[1],p[3]))
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
def p_list(p):
    """ list : list COMMA factor
             | factor
             |  """
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    elif len(p)==2:
        p[0] = [p[1]]
    else:
        p[0] = []
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

