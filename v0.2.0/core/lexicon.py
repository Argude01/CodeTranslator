import sys
from plex import *

letter = Range("AZaz")
digit = Range("09")
name = letter + Rep(letter | digit)
number = Rep1(digit)
space = Any(" \t")
end_line = Str("\n")
operator = Any("+-*/=<>")
end_instruction = Str(";")
open_parenthesis = Str("(")
close_parenthesis =  Str(")")
open_bracket = Str("{")
close_bracket = Str("}")
resword = Str("if", "then", "else", "end", "function", "true", "false", "return")

lexicon = Lexicon([
    (resword,           TEXT),
    (name,              'UID'),
    (number,            'int'),
    (operator,          TEXT),
    (end_instruction,   TEXT),
    (open_parenthesis,  TEXT),
    (close_parenthesis, TEXT),
    (open_bracket,      TEXT),
    (close_bracket,     TEXT),
    (end_line,          TEXT),
    (space,             TEXT)
])

file_dir = sys.argv[1] # from gui import self.filename
#file_dir = 'files/function.js'
f = open(file_dir, "r")
scanner = Scanner(lexicon, f, file_dir)
#tokens = []
#descriptions = []
#values = []
#description_items = []
#value_items = []
while 1:
    token = scanner.read()
    #tokens.append(token)
    #value_items.append(token[1])
    #description_items.append(token[0])
    print (token) 
    #if token[0] == '\n' or token[0] == 'None':
    #    values.append(value_items)
    #    descriptions.append(description_items)
    if token[0] is None:
        break
