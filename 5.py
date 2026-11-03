from collections import defaultdict, deque

# Step 1: Input NFA
n = int(input("Enter number of NFA states: "))

print("Enter the NFA transition table row by row.")
print("Use 'e' for epsilon, 'a'/'b' for symbols, '.' for none.")
print("Example for 3 states: e.a ..a ...")

# Initialize transition table
data = [['' for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    row = input(f"State {i}: ").replace(" ", "")

    if len(row) != n:
        raise ValueError("Invalid row length. Must be exactly n characters.")

    for j in range(1, n + 1):
        data[i][j] = row[j - 1]

# Step 2: Compute epsilon closures
e_close = defaultdict(list)


def compute_epsilon_closure(state):
    closure = set()
    stack = [state]

    while stack:
        s = stack.pop()

        if s not in closure:
            closure.add(s)

            for j in range(1, n + 1):
                if data[s][j] == 'e':
                    stack.append(j)

    return sorted(closure)


# Calculate epsilon closure for each state
for i in range(1, n + 1):
    e_close[i] = compute_epsilon_closure(i)

# Display epsilon closures
print("\nEpsilon Closures:")

for i in range(1, n + 1):
    print(f"E({i}) = {{{', '.join(map(str, e_close[i]))}}}")

# Step 3: Subset Construction for DFA
symbol_set = ['a', 'b']  # Assuming alphabet is {a, b}

dfa_states = []
dfa_transitions = {}


def move(states, symbol):
    result = set()

    for state in states:
        for j in range(1, n + 1):
            if data[state][j] == symbol:
                result.update(e_close[j])

    return sorted(result)


# Initial DFA state = epsilon closure of NFA start state
initial = e_close[1]

dfa_states.append(initial)
queue = deque([initial])

print("\nDFA Transition Table:")
print(f"{'State':<15}{'a':<20}{'b':<20}")
print("-" * 55)

while queue:
    current = queue.popleft()
    current_label = ",".join(map(str, current))

    dfa_transitions[current_label] = {}

    row = f"{{{current_label}}}".ljust(15)

    for symbol in symbol_set:
        target = move(current, symbol)
        target_label = ",".join(map(str, target))

        if target:
            target_label = f"{{{target_label}}}"
        else:
            target_label = "-"

        row += target_label.ljust(20)
        dfa_transitions[current_label][symbol] = target_label

        if target and target not in dfa_states:
            dfa_states.append(target)
            queue.append(target)

    print(row)

# Final DFA states list
print("\nDFA States:")

for state in dfa_states:
    print("{" + ",".join(map(str, state)) + "}")
