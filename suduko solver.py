def print_board(board):
    """Function to print the Sudoku board in a readable format."""
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(len(board[row])):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()

def find_empty_location(board):
    """Find an empty spot (represented by 0) in the Sudoku board."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, num, pos):
    """Check if placing a number in a given position is valid."""
    row, col = pos
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(len(board))]:
        return False
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty_location(board)
    if not empty:
        return True 
    row, col = empty

    for num in range(1, 10): 
        if is_valid(board, num, (row, col)):
            board[row][col] = num  

            if solve_sudoku(board):
                return True

            board[row][col] = 0  

    return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Sudoku puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
