class Operation:
    def __init__(self, left, right):
        self.l = left
        self.r = right


def main():
    n = int(input("Enter the number of values: "))
    operations = []

    # Input intermediate code
    for i in range(n):
        left = input(f"Left operand {i+1}: ").strip()
        right = input(f"Right expression {i+1}: ").strip()
        operations.append(Operation(left, right))

    print("\nIntermediate Code:")
    for op in operations:
        print(f"{op.l} = {op.r}")

    # Dead Code Elimination
    pr = []

    for i in range(n - 1):
        temp = operations[i].l

        for j in range(n):
            if temp in operations[j].r:
                pr.append(Operation(operations[i].l, operations[i].r))
                break

    # Add last operation
    if n > 0:
        pr.append(Operation(operations[n - 1].l, operations[n - 1].r))

    print("\nAfter Dead Code Elimination:")
    for op in pr:
        print(f"{op.l} = {op.r}")

    # Common Subexpression Elimination
    for m in range(len(pr)):
        tem = pr[m].r

        for j in range(m + 1, len(pr)):
            if pr[j].r == tem:
                t = pr[j].l
                pr[j].l = pr[m].l

                # Replace occurrences
                for i in range(len(pr)):
                    if t in pr[i].r:
                        pr[i].r = pr[i].r.replace(t, pr[m].l)

    print("\nEliminate Common Expression:")
    for op in pr:
        print(f"{op.l} = {op.r}")

    # Remove duplicates
    optimized = []

    for i in range(len(pr)):
        duplicate = False

        for j in range(i + 1, len(pr)):
            if pr[i].r == pr[j].r and pr[i].l == pr[j].l:
                duplicate = True
                break

        if not duplicate:
            optimized.append(pr[i])

    print("\nOptimized Code:")
    for op in optimized:
        print(f"{op.l} = {op.r}")


if __name__ == "__main__":
    main()
