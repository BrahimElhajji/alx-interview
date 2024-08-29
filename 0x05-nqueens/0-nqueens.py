#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard """
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""

    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem using backtracking."""
    def backtrack(row, current_solution):
        if row == N:
            print([[i, current_solution[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(current_solution, row, col):
                current_solution[row] = col
                backtrack(row + 1, current_solution[:])

    board = [-1] * N
    backtrack(0, board)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
