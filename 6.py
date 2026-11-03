def shift_reduce_parser(input_str):
    stack = []
    ip = list(input_str)
    ip.append('$')  # End marker
    pointer = 0

    print("\n\tShift Reduce Parser")
    print("\nGrammar:")
    print("E → E + E\nE → E * E\nE → E / E\nE → a | b")
    print("\nStack\t\tInput\t\tAction")

    def print_state(action):
        print(
            f"{''.join(stack):<16}"
            f"{''.join(ip[pointer:]):<16}"
            f"{action}"
        )

    def reduce_stack():
        nonlocal stack
        s = ''.join(stack)

        if s.endswith("E+E") or s.endswith("E*E") or s.endswith("E/E"):
            rule = s[-3:]
            stack = stack[:-3]
            stack.append('E')
            print_state(f"Reduce by E → {rule}")
            return True

        elif stack and stack[-1] in ['a', 'b']:
            stack[-1] = 'E'
            print_state(f"Reduce by E → {s[-1]}")
            return True

        return False

    print_state("--")

    while pointer < len(ip) - 1:
        stack.append(ip[pointer])
        pointer += 1
        print_state(f"Shift '{stack[-1]}'")

        while reduce_stack():
            pass

    if stack == ['E'] and ip[pointer] == '$':
        print_state("Accept")
    else:
        print_state("Reject")


# Input
input_expr = input(
    "Enter the input expression (only a, b, +, *, /): "
).strip()

shift_reduce_parser(input_expr)
