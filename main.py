from Formatter import formatting
from Parser import parsing
from Interpreter import *
import sys
from os import path, remove

filename=sys.argv[1]
ext=path.splitext(path.basename(filename))[1].lower()
var={
    "_brk":0,
    "_continue":0,
    "_isLoop":[]
}
functions={}
function_scope={
    #function_name : [function_local_vars]
}
#functions dictionnary structure
# functions={"functionName" : [(params),(bloc)]}
if (ext!=".zr"):
    print("File should be .zr")
else:
    formatting(filename)
    parsed = parsing(filename)
    remove(path.splitext(path.basename(filename))[0]+".tmp")
    for i in parsed:
        #print(i)
        interpret(i,var,functions)
    print(var)