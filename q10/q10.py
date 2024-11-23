from queue import PriorityQueue

# A* Algorithm implementation
def a_star_algorithm(graph, start, goal, heuristic):
    # Priority Queue to store (cost, node, path)
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()

    while not pq.empty():
        cost, current_node, path = pq.get()

        # If goal is reached, return the path and cost
        if current_node == goal:
            return path, cost

        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                total_cost = cost + weight
                estimated_cost = total_cost + heuristic[neighbor]
                pq.put((estimated_cost, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 1), ('E', 4)],
        'C': [('F', 2)],
        'D': [('G', 3)],
        'E': [('G', 1)],
        'F': [('G', 5)],
        'G': []
    }

    # Heuristic values (estimated cost to reach the goal 'G')
    heuristic = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 6,
        'G': 0
    }

    start = 'A'
    goal = 'G'
    path, cost = a_star_algorithm(graph, start, goal, heuristic)

    if path:
        print(f"Shortest path: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
