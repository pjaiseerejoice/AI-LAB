
# Experiment 6: Map Colouring using CSP

# 1. Define CSP variables (regions)
regions = ['A', 'B', 'C', 'D', 'E', 'F']

# 2. Define available colours (domains)
colours = ['Red', 'Green', 'Blue']

domains = {
    region: colours.copy() for region in regions
}

# 3. Define adjacency constraints
neighbours = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

# Store colour assignments
assignment = {}

# Count assignment attempts
attempts = 0


# Check whether a colour is valid
def is_valid(region, colour):
    for neighbour in neighbours[region]:
        if neighbour in assignment:
            if assignment[neighbour] == colour:
                return False
    return True


# 4. Backtracking search
def backtrack():
    global attempts

    # Check whether all regions are coloured
    if len(assignment) == len(regions):
        return True

    # Select an unassigned region
    region = next(r for r in regions if r not in assignment)

    # Try each colour in its domain
    for colour in domains[region]:
        attempts += 1

        if is_valid(region, colour):
            assignment[region] = colour

            if backtrack():
                return True

            # Backtrack
            del assignment[region]

    return False


# 5. Execute CSP algorithm
if backtrack():
    print("Valid Map Colouring Assignment:\n")

    for region in regions:
        print(f"Region {region} : {assignment[region]}")

    # Verify adjacency constraints
    print("\nConstraint Verification:")

    valid = True

    for region in regions:
        for neighbour in neighbours[region]:
            if assignment[region] == assignment[neighbour]:
                valid = False
                print(f"Conflict between {region} and {neighbour}")

    if valid:
        print("All adjacency constraints are satisfied.")

    print("\nTotal Assignment Attempts:", attempts)

else:
    print("No valid colouring exists.")
