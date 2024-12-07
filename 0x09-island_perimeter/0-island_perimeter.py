#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A rectangular grid where
                                    0 represents water and 1 represents land.

    Returns:
        int: The total perimeter of the island.
    """
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for a land cell
                perimeter += 4

                # Subtract sides shared with the land cell above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Subtract sides shared with the land cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter

