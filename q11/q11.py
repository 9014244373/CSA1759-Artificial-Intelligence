# Define the map coloring problem
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']  # Australian states
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania has no neighbors
}
colors = ['Red', 'Green', 'Blue']

# Create a dictionary to hold the colors assigned to each region
color_assignment = {}

# Check if a color can be assigned to a region
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm for map coloring
def backtrack(region_index):
    if region_index == len(regions):  # All regions are colored
        return True

    region = regions[region_index]
    for color in colors:
        if is_valid(region, color):
            color_assignment[region] = color
            if backtrack(region_index + 1):  # Recurse to color the next region
                return True
            del color_assignment[region]  # Backtrack
    return False

# Solve the problem
if backtrack(0):
    print("Color Assignment:")
    for region, color in color_assignment.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
