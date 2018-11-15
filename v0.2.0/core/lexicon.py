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
    (resword,           'RESWORD'),
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

file_dir = "files/function.js"
f = open(file_dir, "r")

print '--------- Lexicon ---------\n'
scanner = Scanner(lexicon, f, file_dir)
statements = []
lexico_actions = []
lexico_values = [] 
lexico_patterns = []
tokens = []
chain = []
descriptions = ''
while 1:
    token = scanner.read()
    tokens.append(token)
    print token
    if token[0] is None:
        break

print '\n--------- Syntax ---------\n'
instructions = [line.rstrip('\n') for line in open(file_dir)]
i=0
for token in tokens:
    descriptions += str(token[0]) 
    if str(token[0]) == '\n':
        statements.append(descriptions)
        print instructions[i]      
        print statements[len(statements)-1]  
        descriptions = ''
