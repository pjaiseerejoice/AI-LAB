
# Experiment 7: Minimax Algorithm

# Binary game tree with terminal utility values
tree = [
    [3, 5],
    [2, 9]
]

def minimax(node, maximizing):
    if isinstance(node, int):
        return node

    if maximizing:
        values = [minimax(child, False) for child in node]
        result = max(values)
        print("Max values:", values, "->", result)
        return result
    else:
        values = [minimax(child, True) for child in node]
        result = min(values)
        print("Min values:", values, "->", result)
        return result

best_value = minimax(tree, True)

print("\nBest value for AI:", best_value)
print("Best move: First branch (left)")
