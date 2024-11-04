# Practical 5: Design 8-Queens matrix having the first Queen placed. Use backtracking to place
# remaining Queens to generate the final 8-queen’s matrix.

def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    n = len(board)

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, first_queen_row, first_queen_col):
    n = len(board)

    if col >= n:
        # All queens are placed, return True
        return True

    # Skip the first queen's position
    if col == first_queen_col:
        # First queen is placed, move to the next column
        return solve_n_queens(board, col + 1, first_queen_row, first_queen_col)

    # Try placing the queen in each row of the current column
    for i in range(n):
        if i != first_queen_row and is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1, first_queen_row, first_queen_col):
                return True
            # If placing the queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False

def main():
    n = 8  # Size of the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    first_queen_row = 0  # Specify the row for the first queen
    first_queen_col = 0  # Specify the column for the first queen

    # Place the first queen at the specified position
    board[first_queen_row][first_queen_col] = 1

    # Call the backtracking function to solve the rest of the board
    if solve_n_queens(board, 0, first_queen_row, first_queen_col):
        print("Solution exists:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
