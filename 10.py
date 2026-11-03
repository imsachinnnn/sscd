class Register:
    def __init__(self):
        self.var = ""
        self.alive = False


# Initialize 10 registers
preg = [Register() for _ in range(10)]


def substring(exp, start, end):
    return exp[start:end]


def get_register(var):
    for i in range(10):
        if not preg[i].alive:
            preg[i].var = var
            return i
    return -1


def get_var(exp):
    var = ""

    for ch in exp:
        if ch.isalpha():
            var += ch
        else:
            break

    return var


def main():
    basic = []

    print("\nEnter the Three Address Code (type 'exit' to finish):")

    while True:
        line = input().strip()

        if line.lower() == "exit":
            break

        basic.append(line)

    print("\nThe Equivalent Assembly Code is:")
    vc = 0

    for j in range(len(basic)):
        exp = basic[j]

        # Get first variable
        var1 = get_var(exp)
        vc += 1
        fstr = var1
        exp = substring(exp, len(var1) + 1, len(exp))

        # Get second variable
        var2 = get_var(exp)
        vc += 1
        reg = get_register(var2)

        if reg == -1:
            print("No free register available.")
            return

        if not preg[reg].alive:
            print(f"\nMov R{reg}, {var2}")
            preg[reg].alive = True

        # Get operator
        op = exp[len(var2)]
        exp = substring(exp, len(var2) + 1, len(exp))

        # Get third variable
        var3 = get_var(exp)
        vc += 1

        # Print operation
        if op == '+':
            print("Add", end='')
        elif op == '-':
            print("Sub", end='')
        elif op == '*':
            print("Mul", end='')
        elif op == '/':
            print("Div", end='')

        # Check if var3 is in any register
        flag = True

        for k in range(reg + 1):
            if preg[k].var == var3:
                print(f" R{k}, R{reg}")
                preg[k].alive = False
                flag = False
                break

        if flag:
            print(f" {var3}, R{reg}")

        print(f"\nMov {fstr}, R{reg}")
        preg[reg].var = fstr


if __name__ == "__main__":
    main()
