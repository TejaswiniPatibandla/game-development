def solve_sudoku(board):
    """
    A function that takes a partially filled 9x9 Sudoku board and solves it.

    :param board: A list of lists representing the Sudoku board
    :return: True if the board is solvable, False otherwise
    """
    
    
    # Find the the  first empty cell (represented by 0)
    row, col = find_empty_cell(board)

    # If there are no empty cells, the board is solved
    if row is None:
        return True

    # Try each number from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # If the move is valid, place the number in the cell
            board[row][col] = num

            # Recursively solve the rest of the board
            if solve_sudoku(board):
                return True

            # If the recursive solve fails, backtrack and try the next number
            board[row][col] = 0

    # If none of the numbers worked, the board is unsolvable
    return False


def find_empty_cell(board):
    """
    A helper function that finds the first empty cell (represented by 0) on the board.

    :param board: A list of lists representing the Sudoku board
    :return: The row and column indices of the empty cell, or None if there are no empty cells
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None


def is_valid_move(board, row, col, num):
    """
    A helper function that checks if a given number can be placed in a given cell.

    :param board: A list of lists representing the Sudoku board
    :param row: The row index of the cell
    :param col: The column index of the cell
    :param num: The number to be placed in the cell
    :return: True if the move is valid, False otherwise
    """
    # Check if the number is already in the row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is already in the 3x3 sub-grid
    subgrid_row, subgrid_col = (row // 3) * 3, (col // 3) * 3
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False

    # If the number is not already in the row, column, or sub-grid, it is a valid move
    return True
