from Lexing import lexer
from os import path
from re import sub
def formatting(filename):
    base=path.splitext(path.basename(filename))[0]
    output=open(base+".tmp","w+") 
    input=open(filename,"r")
    inputLines = "".join(input.readlines())
    lexer.input(inputLines)
    datalist = inputLines.split('\n')
    datalist = [sub( r"[#].*", "", d) for d in datalist]
    bloc=[]
    line = ""
    code=[]
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
            code.append(s)
        else :    
            code.append(line)
            line=""
    for l in code:
            output.write("%s\n" % l)