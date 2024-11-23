from collections import deque

def is_valid_state(state):
    """
    Check if the state is valid: No side should have more cannibals than missionaries.
    """
    m_left, c_left, m_right, c_right, _ = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    return True

def get_successors(state):
    """
    Generate all possible successor states.
    """
    m_left, c_left, m_right, c_right, boat_position = state
    successors = []
    moves = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1),  # One missionary and one cannibal
    ]

    for m, c in moves:
        if boat_position == 'left':  # Boat on the left side
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
        else:  # Boat on the right side
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')

        if is_valid_state(new_state):
            successors.append(new_state)

    return successors

def bfs_missionaries_cannibals():
    """
    Solve the Missionaries and Cannibals problem using BFS.
    """
    start_state = (3, 3, 0, 0, 'left')  # (m_left, c_left, m_right, c_right, boat_position)
    goal_state = (0, 0, 3, 3, 'right')

    queue = deque([(start_state, [])])  # Each element is a tuple (state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            return path + [current_state]

        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))

    return None

# Run the solution
solution = bfs_missionaries_cannibals()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
