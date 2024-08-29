#!/usr/bin/python3
"""
0-island-perimetr
"""


def island_perimeter(grid):
    """Calculate the perimeter of island"""
    perimeter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (grid[i][j] == 1):
                perimeter += 4
                if (i > 0 and grid[i - 1][j] == 1):
                    perimeter -= 2
                if (j > 0 and grid[i][j - 1] == 1):
                    perimeter -= 2
    return perimeter
