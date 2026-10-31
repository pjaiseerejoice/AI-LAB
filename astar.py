
import heapq

# Weighted graph representing the locations
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 6, 'E': 4},
    'D': {'B': 5, 'C': 6, 'E': 1, 'F': 2},
    'E': {'C': 4, 'D': 1, 'F': 3},
    'F': {'D': 2, 'E': 3}
}

# Admissible heuristic estimates to goal F
h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    queue = [(h[start], 0, start)]
    parent = {}
    cost = {start: 0}
    expanded = []

    while queue:
        f, g, node = heapq.heappop(queue)

        if g != cost[node]:
            continue

        expanded.append(node)

        if node == goal:
            path = []
            current = goal

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            print("Selected route:", " -> ".join(path))
            print("Total path cost:", cost[goal])
            print("Node expansion order:", " -> ".join(expanded))
            return

        for neighbor, weight in graph[node].items():
            new_cost = g + weight

            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                parent[neighbor] = node
                f_value = new_cost + h[neighbor]

                heapq.heappush(
                    queue, (f_value, new_cost, neighbor)
                )

    print("No route found.")

start = input("Enter start node (A-F): ").upper()
goal = input("Enter goal node (A-F): ").upper()

if start in graph and goal in graph:
    astar(start, goal)
else:
    print("Invalid node!")
