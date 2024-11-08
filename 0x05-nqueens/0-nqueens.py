#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""

def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return (pos0[0] == pos1[0] or  # same row
            pos0[1] == pos1[1] or  # same column
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))  # same diagonal

def build_solution(row, group):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    if row == n:
        solutions.append(group.copy())
        return

    for col in range(n):
        new_position = (row, col)
        if all(not is_attacking(new_position, pos) for pos in group):
            group.append(new_position)
            build_solution(row + 1, group)
            group.pop()

def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global n
    build_solution(0, [])

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
