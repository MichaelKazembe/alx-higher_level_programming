#!/usr/bin/python3

import sys


def n_queens(size):
    """
    Solve the N Queens problem and print every possible solution.

    Args:
        size (int): The number of queens and size of the chessboard.

    Returns:
        None
    """

    queens = [0] * size
    s = size

    while True:
        while size > 1:
            if valid(queens, size):
                size -= 1
            else:
                queens[size] += 1
                if queens[size] >= s:
                    queens[size] = 0
                    queens[size + 1] += 1

        print("Solution:")
        print(queens)

        queens[0] += 1
        size = 0

    def valid(queens, size):
        """
        Check if the current queen placement is valid.

        Args:
            queens (list): List representing the current queen placements.
            size (int): The index of the current queen being checked.

        Returns:
            bool: True if the queen placement is valid, False otherwise.
        """
        i = size + 1
        while i < s:
            if queens[i] == queens[size]:
                return False
            i += 1

        i = size + 1
        x = 1
        while i < s:
            if queens[i] == queens[size] - x:
                return False
            i += 1
            x += 1

        i = size + 1
        x = 1
        while i < s:
            if queens[i] == queens[size] + x:
                return False
            i += 1
            x += 1

        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(size)
