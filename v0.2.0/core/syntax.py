#from lexicon import instructions, statements, f
import re

patterns = [
    r"RESWORD UID(){RESWORD (RESWORD){}}NoneRESWORD UID(){RESWORD (RESWORD){ RESWORD RESWORD; }}",
    r"RESWORD UID(){RESWORD (RESWORD){}}",
    r"RESWORD UID(){RESWORD (RESWORD){ RESWORD RESWORD;}}",
    r"RESWORD UID(){RESWORD RESWORD;}"
]

print "\n------ PATTERNS VALIDATED -------\n"

for line in f:
    if re.match(patterns, line):
        print line + '\n is a JavaScript Function'
