vars = []
vcnt = 0
state = 0
pos = 0
token = ""
tlen = 0

def getAddress(str_):
    global vcnt
    for i in range(vcnt):
        if vars[i] == str_:
            return i
    vars.append(str_)
    vcnt += 1
    return vcnt - 1

def isrelop(c):
    return c in ['+', '-', '*', '/', '%', '^']

input_str = input("Enter the Input String: ")

while pos < len(input_str):
    c = input_str[pos]
    print(c, end='')

    if state == 0:
        if c.isspace():
            pass  # Ignore whitespace

        elif c.isalpha():
            token = c
            tlen = 1
            state = 1

        elif c.isdigit():
            token = c
            tlen = 1
            state = 2

        elif isrelop(c):
            print(f"\t<{ord(c)},{ord(c)}>")

        elif c == ';':
            print("\t<3,3>")

        elif c == '=':
            print("\t<4,4>")

    elif state == 1:
        # Identifier
        if not c.isalnum():
            print(f"\t<1,{getAddress(token)}>")
            state = 0
            pos -= 1
        else:
            token += c
            tlen += 1

    elif state == 2:
        # Number
        if not c.isdigit():
            print(f"\t<2,{token}>")
            state = 0
            pos -= 1
        else:
            token += c
            tlen += 1

    pos += 1

# Flush last token if needed
if state == 1:
    print(f"\t<1,{getAddress(token)}>")

elif state == 2:
    print(f"\t<2,{token}>")
