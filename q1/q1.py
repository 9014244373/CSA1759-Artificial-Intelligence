import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.zero_pos = board.index(0)

    def is_goal(self, goal):
        return self.board == goal

    def possible_moves(self):
        moves = []
        x, y = divmod(self.zero_pos, 3)
        directions = {
            "up": (x - 1, y),
            "down": (x + 1, y),
            "left": (x, y - 1),
            "right": (x, y + 1),
        }

        for move, (nx, ny) in directions.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_pos] = new_board[new_pos], new_board[self.zero_pos]
                moves.append((new_board, move))

        return moves

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(state, goal):
    """Calculate Manhattan distance as the heuristic."""
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def solve_puzzle(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, PuzzleState(start)))
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current.is_goal(goal):
            moves = []
            while current.parent:
                moves.append(current.move)
                current = current.parent
            return moves[::-1]  # Return reversed path to the goal

        visited.add(tuple(current.board))

        for new_board, move in current.possible_moves():
            if tuple(new_board) in visited:
                continue

            new_cost = current.cost + 1
            estimated_cost = new_cost + heuristic(new_board, goal)
            heapq.heappush(open_set, (estimated_cost, PuzzleState(new_board, current, move, new_cost)))

    return None  # No solution

# Example usage
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Initial configuration
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Goal configuration

solution = solve_puzzle(start_state, goal_state)
if solution:
    print("Solution found:", solution)
else:
    print("No solution exists.")
