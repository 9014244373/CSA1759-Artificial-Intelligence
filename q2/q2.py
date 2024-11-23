def is_safe(board, row, col):
    """
    Check if a queen can be placed on board[row][col].
    """

    # Check the column for conflicts
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row):
    """
    Solve the N-Queens problem using backtracking.
    """
    if row == len(board):  # All queens are placed
        return [list(row) for row in board]  # Return a solution

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen
            solution = solve_n_queens(board, row + 1)  # Recurse to place next queen
            if solution:  # If a solution is found, return it
                return solution
            board[row][col] = 0  # Backtrack if placing queen doesn't lead to a solution

    return None  # No solution found


def print_board(board):
    """
    Print the chessboard with queens.
    """
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


# Example usage
N = 8
board = [[0] * N for _ in range(N)]  # Initialize an 8x8 chessboard
solution = solve_n_queens(board, 0)

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution exists.")
