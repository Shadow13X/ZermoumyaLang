# This file provides the runtime support for running a basic program
# Assumes the program has been parsed using basparse.py

import sys
import math
import random


# def __init__(self, prog):
#     prog = prog

#     functions = {           # Built-in function table
#         '_SIN': lambda z: math.sin(interpret(z)),
#         '_COS': lambda z: math.cos(interpret(z)),
#         '_TAN': lambda z: math.tan(interpret(z)),
#         '_EXP': lambda z: math.exp(interpret(z)),
#         '_ABS': lambda z: abs(interpret(z)),
#         '_LOG': lambda z: math.log(interpret(z)),
#         '_SQR': lambda z: math.sqrt(interpret(z)),
#         '_3LH': lambda z: random.random()
#     }

# Evaluate an expression
def interpret(expr,var):
    etype = expr[0]
    if etype == 'SCAN':
        tmp = input()
        try:
            float(tmp)
            try:
                if(float(tmp)==int(tmp)):
                    var[str(expr[1])] = int(tmp)
            except ValueError:
                var[str(expr[1])] = float(tmp)
        except ValueError:
            var[str(expr[1])]=tmp
        # if(tmp.isnumeric()):
        #     if(float(tmp)==int(tmp)):
        #         var[str(expr[1])] = int(tmp)     
        #     else:   
        #         var[str(expr[1])] = float(tmp)        
        # else:
        #     var[str(expr[1])]=tmp
    elif etype == 'PRINT':
        # ('PRINT', (('', ('STRING', '"i"')),))
        for i in expr[1]:
            if (i[1][0]=="STRING"):
                s = i[1][1].replace("$","\n")
                print(s[1:len(s)-1],end="")
            elif (i[1][0]=="NUMBER"):
                print(i[1][1],end="")
            else:

                print(interpret(i[1],var),end="")  
    elif etype == 'ASS':
        if expr[1][1]=='var':
            var[str(expr[1][0])] = interpret(expr[2],var)
        if expr[1][1]=='list':
            l=[]
            for i in expr[2][1]:
                l.append(interpret(i,var))
            var[str(expr[1][0])]=l
    elif etype == 'NUMBER':
        return expr[1]
    elif etype == 'STRING':
        return expr[1]
    elif etype == 'SUM':
        return interpret(expr[1],var) + interpret(expr[2],var)
    elif etype == 'SUB':
        return interpret(expr[1],var) - interpret(expr[2],var)
    elif etype == 'MUL':
        return interpret(expr[1],var) * interpret(expr[2],var)
    elif etype == 'DIV':
        return interpret(expr[1],var) / interpret(expr[2],var)
    elif etype == 'IDIV':
        return interpret(expr[1],var) // interpret(expr[2],var)
    elif etype == 'MOD':
        return interpret(expr[1],var) % interpret(expr[2],var)
    elif etype == 'VAR':
        v, dim1= expr[1]
        if not dim1:
            if v in var:
                return var[v]
            else:
                print("UNDEFINED VARIABLE %s" %
                        v)
                raise RuntimeError
        # May be a list lookup or a function interpretuation
        else :
            dim1val = interpret(dim1,var)
            if dim1val < 0 or dim1val > len(var[v]):
                print("LIST INDEX OUT OF BOUNDS AT LINE")
                raise RuntimeError
            return var[v][dim1val]
    elif etype == 'BLOC':
        for i in expr[1]:
            interpret(i,var)
    elif etype == 'FOR':
        if(expr[1][1][1]!='var'):
            print("Unexpected variable type in Loop assignment")
            exit(1)
        if(expr[2][0] not in [">","<",">=","<="]):
            print("Unexpected condition type in Loop assignment")
            exit(1)
        if(expr[3][0] not in ["SUM","SUB","DIV","IDIV","MOD","MUL"]):
            print("Unexpected incrementation in Loop assignment")
            exit(1)
        if(expr[4][0]!="BLOC"):
            print("Bloc expected in loop")
            exit(1)
        var[str(expr[1][1][0])]=expr[1][2][1]
        while(interpret(expr[2],var)):
            interpret(expr[4],var)
            var[str(expr[1][1][0])] = interpret(expr[3],var)
    elif etype == 'WHILE':
        if(expr[1][0] not in [">","<",">=","<="]):
            print("Unexpected condition type in Loop assignment")
            exit(1)
        if(expr[2][0]!="BLOC"):
            print("Bloc expected in loop")
            exit(1)
        while(interpret(expr[1],var)):
            interpret(expr[2],var)
    elif etype == 'COND':
        for cond in expr[1]:
            if(interpret(cond[1],var)):
                interpret(cond[2],var)
                return 1
        interpret(expr[2],var)
        return 1
    elif etype in (">","<",">=","<=","==","!=","&&","||") :
        lhs = interpret(expr[1],var)
        rhs = interpret(expr[2],var)
        if etype == '<':
            if lhs < rhs:
                return 1
            else:
                return 0

        elif etype == '<=':
            if lhs <= rhs:
                return 1
            else:
                return 0

        elif etype == '>':
            if lhs > rhs:
                return 1
            else:
                return 0

        elif etype == '>=':
            if lhs >= rhs:
                return 1
            else:
                return 0

        elif etype == '==':
            if lhs == rhs:
                return 1
            else:
                return 0

        elif etype == '!=':
            if lhs != rhs:
                return 1
            else:
                return 0
        elif etype == '&&':
            if lhs and rhs:
                return 1
            else:
                return 0

        elif etype == '||':
            if lhs or rhs:
                return 1
            else:
                return 0
    elif etype == 'LNOT' :
        lhs = interpret(expr[1],var)
        return not lhs
    elif etype == 'BOOL':
        if expr[1] == '_S7I7':
            return 1
        elif expr[1] == '_GHALET':
            return 0

    # Run it