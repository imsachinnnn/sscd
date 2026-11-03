import re

# Keywords and operators
keywords = [
    "int", "void", "main", "char", "if", "for", "while", "else", "printf", "scanf",
    "FILE", "include", "stdio.h", "conio.h", "iostream.h"
]

operators = {
    "(": "openpara", ")": "closepara", "{": "openbrace", "}": "closebrace",
    "<": "lesser", ">": "greater", '"': "doublequote", "'": "singlequote",
    ":": "colon", ";": "semicolon", "#": "preprocessor", "=": "equal",
    "==": "assign", "%": "percentage", "^": "bitwise", "&": "reference",
    "*": "star", "+": "add", "-": "sub", "\\": "backslash", "/": "slash"
}

# Sample input code
input_code = """ #include "stdio.h" #include
 {
“””
int a=10; getch();
}"""

# Tokenization
tokens = []
current_token = ""

for c in input_code:
    if c.isalnum() or c in ['[', ']', '.']:
        current_token += c
    else:
        if current_token:
            tokens.append(current_token)
            current_token = ""

        if c == '\n':
            tokens.append('$')  # Line marker
        elif not c.isspace():
            tokens.append(c)

# Append last token if present
if current_token:
    tokens.append(current_token)

# Lexical analysis
print("Lexical Analysis")
line = 1
print(f"\nLine: {line}")

for token in tokens:
    if token == '$':  # Line break marker
        line += 1
        print(f"\nLine: {line}")
        continue

    if token in operators:
        print(f"\t\t{token}\t:\t{operators[token]}")
    elif token in keywords:
        print(f"\t\t{token}\t:\tKeyword")
    elif token.isdigit():
        print(f"\t\t{token}\t:\tConstant")
    else:
        print(f"\t\t{token}\t:\tIdentifier")
