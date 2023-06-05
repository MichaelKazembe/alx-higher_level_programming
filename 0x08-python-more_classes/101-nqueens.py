#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    """
    Solve the N-queens problem and print all the possible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]

    def solve_util(board, col):
        if col == N:
            print_solution(board)
            return True

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0

    def print_solution(board):
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    print("[{}, {}]".format(i, j), end=" ")
        print()

    solve_util(board, 0)


if __name__ == "__main__":
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
