
from collections import deque

def get_next_states(state):
    x, y = state
    states = []

    # Fill the 4-litre jug
    states.append(((4, y), "Fill 4-litre jug"))

    # Fill the 3-litre jug
    states.append(((x, 3), "Fill 3-litre jug"))

    # Empty the 4-litre jug
    states.append(((0, y), "Empty 4-litre jug"))

    # Empty the 3-litre jug
    states.append(((x, 0), "Empty 3-litre jug"))

    # Pour 4-litre jug into 3-litre jug
    pour = min(x, 3 - y)
    states.append(((x - pour, y + pour),
                   "Pour 4-litre jug into 3-litre jug"))

    # Pour 3-litre jug into 4-litre jug
    pour = min(y, 4 - x)
    states.append(((x + pour, y - pour),
                   "Pour 3-litre jug into 4-litre jug"))

    return states


def bfs():
    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Goal: exactly 2 litres in the 4-litre jug
        if state[0] == 2:
            print("Solution found!")
            print("Initial state:", start)

            for action, next_state in path:
                print(action, "->", next_state)

            print("Goal state:", state)
            return

        for next_state, action in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [(action, next_state)])
                )

    print("No solution found.")


bfs()
