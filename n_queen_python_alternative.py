# N-Queens Problem using Backtracking (CSP)

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve(row, n, board):
    # If all queens are placed
    if row == n:
        print_board(board, n)
        print()
        return True

    found = False

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # place queen

            found = solve(row + 1, n, board) or found

            board[row] = -1  # backtrack

    return found


def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)


# -------- MAIN --------
n = int(input("Enter number of queens: "))

board = [-1] * n

print("\nSolutions:\n")
solve(0, n, board)
