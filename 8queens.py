
# Experiment 5: 8-Queens Problem Using Backtracking

N = 8

# Store the column position of each queen
board = [-1] * N

attempts = 0


# Function to check whether a queen can be placed safely
def is_safe(row, col):
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False

        # Check diagonal attacks
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Recursive backtracking function
def solve(row):
    global attempts

    # All eight queens are placed
    if row == N:
        return True

    # Try placing queen in each column
    for col in range(N):
        attempts += 1

        if is_safe(row, col):
            board[row] = col

            # Recursively place the next queen
            if solve(row + 1):
                return True

            # Backtrack if no solution is found
            board[row] = -1

    return False


# Execute the algorithm
if solve(0):
    print("Valid 8-Queens Solution:\n")

    # Display chessboard
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()

    # Display queen positions
    print("\nQueen Positions:")
    for row in range(N):
        print(f"Queen {row + 1}: Row {row + 1}, Column {board[row] + 1}")

    print("\nTotal Placement Attempts:", attempts)

else:
    print("No solution exists.")
