def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            print(f"\nPlayer {current_player}'s turn.")
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Cell already taken. Choose a different cell.")
                continue

            board[row][col] = current_player
            print_board(board)

            winner = check_winner(board)
            if winner:
                print(f"Player {winner} wins!")
                break

            if is_full(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
