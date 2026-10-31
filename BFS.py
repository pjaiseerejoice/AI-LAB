
from collections import deque

# Hospital layout represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['B', 'C', 'F'],
    'F': ['E', 'H'],
    'G': ['D', 'H'],
    'H': ['F', 'G']
}

def bfs(graph, source, destination):
    queue = deque([(source, [source])])
    visited = {source}
    explored = 0

    while queue:
        node, path = queue.popleft()
        explored += 1

        if node == destination:
            print("Shortest route:", " -> ".join(path))
            print("Corridors traversed:", len(path) - 1)
            print("Nodes explored:", explored)
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("No route found.")

source = input("Enter source node (A-H): ").upper()
destination = input("Enter destination node (A-H): ").upper()

if source in graph and destination in graph:
    bfs(graph, source, destination)
else:
    print("Invalid node! Enter a node from A to H.")
