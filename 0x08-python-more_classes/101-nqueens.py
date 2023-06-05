#!/usr/bin/python3

import sys


def nQueens(n):
    """
    Solve the N Queens problem and print every possible solution.
    
    """

    queens = [0] * n
    s = n

    while True:
        while n > 1:
            if valid(queens, n):
                n -= 1
            else:
                queens[n] += 1
                if queens[n] >= s:
                    queens[n] = 0
                    queens[n + 1] += 1

        print("Solution:")
        print(queens)

        queens[0] += 1
        n = 0

    def valid(queens, n):
        """
        Check if the current queen placement is valid.
        
        """
        i = n + 1
        while i < s:
            if queens[i] == queens[n]:
                return False
            i += 1

        i = n + 1
        x = 1
        while i < s:
            if queens[i] == queens[n] - x:
                return False
            i += 1
            x += 1

        i = n + 1
        x = 1
        while i < s:
            if queens[i] == queens[n] + x:
                return False
            i += 1
            x += 1

        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nQueens(n)
