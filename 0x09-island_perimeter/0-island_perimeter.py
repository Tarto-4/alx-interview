#!/usr/bin/python3
"""
Island Perimeter Problem
"""


def island_perimeter(grid):
        """
            Calculates the perimeter of the island described in grid.
                
                    Args:
                            grid (list of list of int): 2D list of integers containing 0 (water) or 1 (land).
                                
                                    Returns:
                                            int: The perimeter of the island.
                                                """
                                                    
                                                        perimeter = 0
                                                            rows = len(grid)
                                                                cols = len(grid[0]) if rows > 0 else 0
                                                                    
                                                                        for i in range(rows):
                                                                                    for j in range(cols):
                                                                                                    if grid[i][j] == 1:
                                                                                                                        if i == 0 or grid[i - 1][j] == 0:
                                                                                                                                                perimeter += 1
                                                                                                                                                                if i == rows - 1 or grid[i + 1][j] == 0:
                                                                                                                                                                                        perimeter += 1
                                                                                                                                                                                                        if j == 0 or grid[i][j - 1] == 0:
                                                                                                                                                                                                                                perimeter += 1
                                                                                                                                                                                                                                                if j == cols - 1 or grid[i][j + 1] == 0:
                                                                                                                                                                                                                                                                        perimeter += 1
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                return perimeter

