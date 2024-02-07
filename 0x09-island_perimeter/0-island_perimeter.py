#!/usr/bin/python3

""" Function to find perimiter of an island """


def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """


def is_valid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def count_perimeter(x, y):
    perimeter = 0


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for dx, dy in directions:
    new_x, new_y = x + dx, y + dy
    if is_valid(new_x, new_y) and not grid[new_x][new_y]:
        perimeter += 4
return perimeter

    perimeter = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]:
            perimeter += count_perimeter(i, j)

return perimeter
