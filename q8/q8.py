# Function to perform DFS on a graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Keep track of visited nodes
    
    print(start, end=' ')  # Process the current node
    visited.add(start)  # Mark the current node as visited

    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start DFS from a specified node
print("Depth First Search starting from node 'A':")
dfs(graph, 'A')
