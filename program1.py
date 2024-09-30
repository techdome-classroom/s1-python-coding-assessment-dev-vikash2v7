class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here

    if not grid:  # If the grid is empty, return 0 islands
        return 0

    def dfs(grid, i, j):
        # Boundary check and if it's water or already visited land, stop
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        # Mark the land as visited (turn 'L' to 'W')
        grid[i][j] = 'W'
        # Explore the four possible directions (up, down, left, right)
        dfs(grid, i + 1, j)  # down
        dfs(grid, i - 1, j)  # up
        dfs(grid, i, j + 1)  # right
        dfs(grid, i, j - 1)  # left

    island_count = 0
    # Iterate over the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':  # Found an unvisited landmass
                island_count += 1   # Start a new island
                dfs(grid, i, j)     # Visit all parts of the island

    return island_count
                    
        return 0
