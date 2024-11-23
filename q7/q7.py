from collections import deque

def bfs(graph, start):
    # Create a queue for BFS
    queue = deque([start])
    # List to keep track of visited nodes
    visited = set()
    
    # Mark the starting node as visited
    visited.add(start)
    
    print("BFS Traversal Order:")
    while queue:
        # Dequeue a vertex from the queue
        current = queue.popleft()
        print(current, end=" ")
        
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex hasn't been visited, mark it as visited and enqueue it
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

# Example usage
if __name__ == "__main__":
    # Graph representation as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Perform BFS starting from vertex 'A'
    bfs(graph, 'A')
