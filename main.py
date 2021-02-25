from Formatter import formatting
from Parser import parsing
from Interpreter import *
import sys
from os import path, remove

banner="""
 _______  _______  ______    __   __  _______  __   __  __   __  __   __  _______ 
|       ||       ||    _ |  |  |_|  ||       ||  | |  ||  |_|  ||  | |  ||   _   |
|____   ||    ___||   | ||  |       ||   _   ||  | |  ||       ||  |_|  ||  |_|  |
 ____|  ||   |___ |   |_||_ |       ||  | |  ||  |_|  ||       ||       ||       |
| ______||    ___||    __  ||       ||  |_|  ||       ||       ||_     _||       |
| |_____ |   |___ |   |  | || ||_|| ||       ||       || ||_|| |  |   |  |   _   |
|_______||_______||___|  |_||_|   |_||_______||_______||_|   |_|  |___|  |__| |__|
 ___      _______  __    _  _______                                               
|   |    |   _   ||  |  | ||       |                                              
|   |    |  |_|  ||   |_| ||    ___|                                              
|   |    |       ||       ||   | __                                               
|   |___ |       ||  _    ||   ||  |                                              
|       ||   _   || | |   ||   |_| |                                              
|_______||__| |__||_|  |__||_______|                                              
"""

filename=sys.argv[1]
ext=path.splitext(path.basename(filename))[1].lower()
var={
    "_brk":0,
    "_continue":0,
    "_return":[0,None],
    "_isLoop":[],
    "_isFunction":[],
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
    print(banner)
    formatting(filename)
    parsed = parsing(filename)
    remove(path.splitext(path.basename(filename))[0]+".tmp")
    for i in parsed:
        # print(i)
        interpret(i,var,functions)
    #print(var)