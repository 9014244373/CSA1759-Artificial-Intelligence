import itertools

def travelling_salesman_problem(distance_matrix, start_city):
    # Get the total number of cities
    num_cities = len(distance_matrix)
    
    # Generate all possible routes excluding the start city
    cities = list(range(num_cities))
    cities.remove(start_city)
    
    min_distance = float('inf')
    best_route = None

    # Generate all permutations of cities to visit
    for perm in itertools.permutations(cities):
        # Start and end at the start city
        current_route = [start_city] + list(perm) + [start_city]
        
        # Calculate the total distance of the route
        current_distance = 0
        for i in range(len(current_route) - 1):
            current_distance += distance_matrix[current_route[i]][current_route[i + 1]]
        
        # Update the minimum distance and best route
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route

    return best_route, min_distance

# Example usage
if __name__ == "__main__":
    # Define a distance matrix (symmetric for undirected graph)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_city = 0  # Starting from city 0

    best_route, min_distance = travelling_salesman_problem(distance_matrix, start_city)
    print("Best route:", best_route)
    print("Minimum distance:", min_distance)
