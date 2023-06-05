#!/usr/bin/python3
"""
Solving the N-queens puzzle.
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Solve the N queens problem using backtracking.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column index to place a queen.
        solutions (list): A list to store the found solutions.

    """
    if col >= len(board):
        add_solution(board, solutions)
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0


def add_solution(board, solutions):
    """
    Add a solution to the list of solutions.

    Args:
        board (list): The current state of the chessboard.
        solutions (list): A list to store the found solutions.

    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])

    solutions.append(solution)


def print_solutions(solutions):
    """
    Print the found solutions.

    Args:
        solutions (list): A list of found solutions.

    """
    for solution in solutions:
        print(solution)


def nqueens(board_size):
    """
    Solve the N queens problem for a given board size.

    Args:
        board_size (int): The size of the chessboard.

    Errors raised:
        ValueError: If the board size is not an integer.
        SystemExit: If the board size is less than 4.

    """
    if not isinstance(board_size, int):
        print("Board size must be a number")
        sys.exit(1)

    if board_size < 4:
        print("Board size must be at least 4")
        sys.exit(1)

    board = [[0] * board_size for _ in range(board_size)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
        nqueens(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
