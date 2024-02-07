#!/usr/bin/python3

""" Function to find perimeter of an island """

def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    def is_valid(x, y):
        return 0 <= x < row and 0 <= y < col

    count = 0
    row, col = len(grid), len(grid[0]) if grid else 0

    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                count += 4

                neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
                count -= sum(1 for x, y in neighbors if is_valid(x, y) and grid[x][y])

    return count

# Example usage:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

result = island_perimeter(grid)
print(result)

