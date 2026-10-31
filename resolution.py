# Step 1: Knowledge Base in CNF
# Enjoys learning = E
# Has free time = F
# Happy student = H

clauses = [
    {"E"},       # Student enjoys learning
    {"F"},       # Student has sufficient free time
    {"~E", "~F", "H"}  # E AND F implies H
]

print("Initial Knowledge Base:")
for c in clauses:
    print(c)

# Step 2: Negate the goal
# Goal: H
# Negated goal: ~H

clauses.append({"~H"})

print("\nAfter adding negated goal:")
for c in clauses:
    print(c)

# Step 3: Resolution function
def resolve(c1, c2):
    for literal in c1:
        if literal.startswith("~"):
            opposite = literal[1:]
        else:
            opposite = "~" + literal

        if opposite in c2:
            new_clause = (c1 - {literal}) | (c2 - {opposite})
            return new_clause

    return None

# Step 4: Apply resolution
print("\nResolution Steps:")

new_clauses = []

while True:
    found = False

    for i in range(len(clauses)):
        for j in range(i + 1, len(clauses)):

            result = resolve(clauses[i], clauses[j])

            if result is not None and result not in clauses:
                print(clauses[i], "+", clauses[j], "=", result)

                clauses.append(result)
                found = True

                if len(result) == 0:
                    print("\nEmpty clause obtained!")
                    print("Contradiction found.")
                    print("Therefore, the student is HAPPY.")
                    raise SystemExit

    if not found:
        break

print("\nNo empty clause obtained.")
print("The goal could not be proved.")



