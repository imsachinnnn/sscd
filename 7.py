# Operator Precedence Parser in Python 3.7

# Precedence table (converted from C version)
q = [
    ['>', '>', '<', '<', '<', '<', '>', '<', '>'],
    ['>', '>', '<', '<', '<', '<', '>', '<', '>'],
    ['>', '>', '>', '>', '<', '<', '>', '<', '>'],
    ['>', '>', '>', '>', '<', '<', '>', '<', '>'],
    ['>', '>', '<', '<', '<', '<', '>', '<', '>'],
    ['<', '<', '<', '<', '<', '<', '=', '<', 'E'],
    ['>', '>', '>', '>', '>', 'E', '>', 'E', '>'],
    ['>', '>', '>', '>', '>', 'E', '>', 'E', '>'],
    ['<', '<', '<', '<', '<', '<', 'E', '<', 'A']
]

stack = []
qs = []
p = 0


# Find index in precedence table
def find(a):
    if a == '+':
        return 0
    elif a == '-':
        return 1
    elif a == '*':
        return 2
    elif a == '/':
        return 3
    elif a == '^':
        return 4
    elif a == '(':
        return 5
    elif a == ')':
        return 6
    elif a.isalpha():
        return 7
    elif a == '$':
        return 8
    else:
        return -1


# Display shift action
def display(a):
    print(f"\nShift {a}")


# Display reduce action
def display1(a):
    if a.isalpha():
        print(f"\nReduce E -> {a}")
    elif a in ['+', '-', '*', '/', '^']:
        print(f"\nReduce E -> E{a}E")
    elif a == ')':
        print("\nReduce E -> (E)")


# Relation check based on precedence
def rel(a, b, d):
    if a.isalpha():
        a = 'a'

    if b.isalpha():
        b = 'a'

    return q[find(a)][find(b)] == d


# Main function
def operator_precedence_parser():
    global p

    # Operator Precedence Parser
    expr = input(
        "\nEnter the Arithmetic Expression ending with $: "
    ).strip()

    stack.append('$')

    while True:
        if expr[p] == '$' and stack[-1] == '$':
            print("\n\nAccepted")
            break

        elif rel(stack[-1], expr[p], '<') or rel(stack[-1], expr[p], '='):
            display(expr[p])
            stack.append(expr[p])
            p += 1

        elif rel(stack[-1], expr[p], '>'):
            while True:
                qs.append(stack.pop())
                display1(qs[-1])

                if rel(stack[-1], qs[-1], '<'):
                    break


# Run the parser
operator_precedence_parser()
