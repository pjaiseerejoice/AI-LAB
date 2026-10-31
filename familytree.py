# Step 1: Define parent facts
parent = [
    ("John", "David"),
    ("Mary", "David"),
    ("John", "Sarah"),
    ("Mary", "Sarah"),
    ("David", "Peter"),
    ("Lisa", "Peter"),
    ("Sarah", "Emma"),
    ("Robert", "Emma")
]

# Step 2: Find parents
def find_parents(person):
    print("\nParents of", person, ":")
    for p, child in parent:
        if child == person:
            print(p)

# Step 3: Find children
def find_children(person):
    print("\nChildren of", person, ":")
    for p, child in parent:
        if p == person:
            print(child)

# Step 4: Find grandparents
def find_grandparents(person):
    print("\nGrandparents of", person, ":")
    for p, child in parent:
        if child == person:
            for gp, parent_name in parent:
                if parent_name == p:
                    print(gp)

# Step 5: Display relationships
find_parents("David")
find_children("John")
find_grandparents("Peter")
