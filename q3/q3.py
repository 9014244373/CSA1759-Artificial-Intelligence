from collections import deque

def water_jug_problem(x, y, z):
    """
    Solve the Water Jug Problem using BFS.
    Args:
        x: Capacity of Jug 1.
        y: Capacity of Jug 2.
        z: Target amount of water to measure.
    Returns:
        A list of states representing the solution or an empty list if no solution exists.
    """
    if z > max(x, y):
        return []  # The target cannot be measured

    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    parent = {}  # To store the path

    def is_valid(state):
        return 0 <= state[0] <= x and 0 <= state[1] <= y

    def get_neighbors(current):
        jug1, jug2 = current
        return [
            (x, jug2),          # Fill Jug 1
            (jug1, y),          # Fill Jug 2
            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2
            (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),  # Pour Jug 1 -> Jug 2
            (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1)),  # Pour Jug 2 -> Jug 1
        ]

    while queue:
        current = queue.popleft()
        jug1, jug2 = current

        if jug1 == z or jug2 == z:
            # Construct the path from start to goal
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]

        if current in visited:
            continue

        visited.add(current)
        for neighbor in get_neighbors(current):
            if is_valid(neighbor) and neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = current

    return []  # No solution exists


# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
if solution:
    print("Solution found:")
    for step in solution:
        print(f"Jug 1: {step[0]}L, Jug 2: {step[1]}L")
else:
    print("No solution exists.")
