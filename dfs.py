
# Directed graph representing the AI deployment pipeline
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': ['L'],
    'L': []
}

def dfs(graph, start, target):
    visited = set()
    path = []
    traversal = []

    def search(node):
        visited.add(node)
        traversal.append(node)
        path.append(node)

        if node == target:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                if search(neighbor):
                    return True

        path.pop()
        return False

    found = search(start)

    print("DFS Traversal:", " -> ".join(traversal))

    if found:
        print("Target is reachable.")
        print("Path:", " -> ".join(path))
    else:
        print("Target is not reachable.")

start = input("Enter starting task (A, B, C, D, E, F, G, H, L): ").upper()
target = input("Enter target task (A, B, C, D, E, F, G, H, L): ").upper()

if start in graph and target in graph:
    dfs(graph, start, target)
else:
    print("Invalid task!")
