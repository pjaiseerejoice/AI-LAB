
# Experiment 8: Alpha-Beta Pruning

tree = [
    [3, 5],
    [2, 9]
]

nodes_evaluated = 0
branches_pruned = 0

def alpha_beta(node, alpha, beta, maximizing):
    global nodes_evaluated, branches_pruned

    if isinstance(node, int):
        nodes_evaluated += 1
        print("Evaluating:", node)
        return node

    if maximizing:
        value = float('-inf')

        for i, child in enumerate(node):
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                branches_pruned += len(node) - i - 1
                print("Pruned remaining branches:", len(node) - i - 1)
                break

        return value

    else:
        value = float('inf')

        for i, child in enumerate(node):
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                branches_pruned += len(node) - i - 1
                print("Pruned remaining branches:", len(node) - i - 1)
                break

        return value

best_value = alpha_beta(tree, float('-inf'),
                        float('inf'), True)

print("\nBest value for AI:", best_value)
print("Best move: First branch (left)")
print("Nodes evaluated:", nodes_evaluated)
print("Branches pruned:", branches_pruned)
