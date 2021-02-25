from Lexing import lexer
from Parsing import parser
from os import path
from os import remove
def parsing(filename):
    base=path.splitext(path.basename(filename))[0]
    input=open(base+".tmp","r")
    inputLines = "".join(input.readlines())
    lexer.input(inputLines)
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break      # No more input
    #     print(tok)
    datalist = inputLines.split('\n')
    bloc=[]
    line = ""
    parsed=[]
    lineno=1
    for d in datalist:
        s=d
        if not s: continue
        tmp=bloc
        if '{' in s:
            bloc.append("1")
        if(bloc!=[]):
            line+=s
        else:
            line=""
        if '}' in s:
            bloc.pop()
        if(bloc!=[]):
            continue
        if line=='':
            result = parser.parse(s)
        else :    
            result = (parser.parse(line))
            line=""
        parsed.append(result)
    # print(parsed)
    return parsed