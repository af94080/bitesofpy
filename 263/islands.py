def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                mark_islands(i, j, grid)
                count += 1

    return count


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.

    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
        return

    grid[i][j] = '#'   

    mark_islands(i+1, j, grid)
    mark_islands(i-1, j, grid)
    mark_islands(i, j+1, grid)
    mark_islands(i, j-1, grid)

g2 =  [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]]

g3 = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]

print(count_islands(g3))