# Recursive Descent Parser in Python

ip_sym = ""
ip_ptr = 0


def advance():
    global ip_ptr
    ip_ptr += 1


def e():
    print("\n\t\tE -> T E'")
    t()
    e_prime()


def e_prime():
    global ip_sym, ip_ptr

    if ip_ptr < len(ip_sym) and ip_sym[ip_ptr] == '+':
        print("\n\t\tE' -> + T E'")
        advance()
        t()
        e_prime()
    else:
        print("\n\t\tE' -> ε")


def t():
    print("\n\t\tT -> F T'")
    f()
    t_prime()


def t_prime():
    global ip_sym, ip_ptr

    if ip_ptr < len(ip_sym) and ip_sym[ip_ptr] == '*':
        print("\n\t\tT' -> * F T'")
        advance()
        f()
        t_prime()
    else:
        print("\n\t\tT' -> ε")


def f():
    global ip_sym, ip_ptr

    if ip_ptr < len(ip_sym) and (
        ip_sym[ip_ptr] == 'i' or ip_sym[ip_ptr] == 'j'
    ):
        print("\n\t\tF -> id")
        advance()

    elif ip_ptr < len(ip_sym) and ip_sym[ip_ptr] == '(':
        advance()
        e()

        if ip_ptr < len(ip_sym) and ip_sym[ip_ptr] == ')':
            advance()
            print("\n\t\tF -> (E)")
        else:
            print("\n\t\tSyntax Error: missing ')'")
            exit(1)

    else:
        print("\n\t\tSyntax Error: unexpected symbol")
        exit(1)


# Main function
def main():
    global ip_sym

    print("\n\t\tGRAMMAR WITHOUT LEFT RECURSION")
    print("\n\t\tE -> T E'")
    print("\t\tE' -> + T E' | ε")
    print("\t\tT -> F T'")
    print("\t\tT' -> * F T' | ε")
    print("\t\tF -> (E) | id")

    ip_sym = input("\n\t\tEnter the input string: ").strip()

    print("\n\t\tSequence of Production Rules:")
    e()

    if ip_ptr == len(ip_sym):
        print("\n\t\tInput accepted!")
    else:
        print("\n\t\tSyntax Error: extra symbols")


if __name__ == "__main__":
    main()
