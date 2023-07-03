#!/usr/bin/python3
"""
Main Module
"""

import sys
from subprocess import check_output, CalledProcessError


def run_nqueens(N):
    """
    Run the nqueens program with the given N.

    Args:
        N (int): The number of queens.

    Returns:
        list: List of solutions.
    """
    try:
        output = check_output(["./101-nqueens.py", str(N)])
        solutions = output.decode().splitlines()
        return solutions
    except CalledProcessError:
        return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-main.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = run_nqueens(N)

    for solution in solutions:
        print(solution)

