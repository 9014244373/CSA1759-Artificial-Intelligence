# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


# Function to print the current state of the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


# Check if the game has ended
def is_game_over(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True
    return False


# Check if there are any available moves
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


# Minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_game_over(board):
        if is_maximizing:
            return -1
        else:
            return 1

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score


# Find the best move for the AI (Player X)
def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


# Main game loop
def play_game():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    current_player = PLAYER_X  # Player X starts

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            print("Player X's turn:")
            row, col = find_best_move(board)
        else:
            print("Player O's turn:")
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())

        board[row][col] = current_player

        if is_game_over(board):
            print_board(board)
            print(f"Game over! Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("Game over! It's a draw!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


# Run the game
if __name__ == "__main__":
    play_game()
