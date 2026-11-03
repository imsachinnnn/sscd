
vars = []
vcnt = 0

input_str = input("Enter the Input String: ")
token = ""
state = 0
pos = 0
tlen = 0


def getAddress(str_):
    global vcnt

    for i in range(vcnt):
        if vars[i] == str_:
            return vars[i]

    vars.append(str_)
    vcnt += 1
    return vars[vcnt - 1]


def isrelop(c):
    return c in ['+', '-', '*', '/', '%', '^', '>', '<']


while pos < len(input_str):
    c = input_str[pos]

    if state == 0:
        if c.isspace():
            pass

        elif c.isalpha():
            token = c
            tlen = 1
            state = 1

        elif c.isdigit():
            token = c
            tlen = 1
            state = 2

        elif isrelop(c):
            token = c
            tlen = 1
            state = 3

        elif c == ';':
            print(f"{c}\t<3,3>")

        elif c == '=':
            print(f"{c}\t<4,4>")

    elif state == 1:
        if c.isalnum():
            token += c
            tlen += 1
        else:
            print(f"{token}\t<1,{getAddress(token)}>")
            state = 0
            pos -= 1

    elif state == 2:
        if c.isdigit():
            token += c
            tlen += 1
        else:
            print(f"{token}\t<2,{token}>")
            state = 0
            pos -= 1

    elif state == 3:
        if c == '=':
            print(f"{token + c}\t<{ord(token)*10},{ord(token)*10}>")
        else:
            print(f"{token}\t<{ord(token)},{ord(token)}>")

        pos -= 1
        state = 0

    pos += 1


# Final token check
if state == 1:
    print(f"{token}\t<1,{getAddress(token)}>")

elif state == 2:
    print(f"{token}\t<2,{token}>")

elif state == 3:
    print(f"{token}\t<{ord(token)},{ord(token)}>")
