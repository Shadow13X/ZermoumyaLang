from Formatter import formatting
from Parser import parsing
from Interpreter import *
import sys
from os import path, remove

filename=sys.argv[1]
ext=path.splitext(path.basename(filename))[1]
var={}
lists={}
if (ext!=".z"):
    print("File should be .z")
else:
    formatting(filename)
    parsed = parsing(filename)
    remove(path.splitext(path.basename(filename))[0]+".tmp")
    for i in parsed:
        #print(i)
        interpret(i,var)