class Solution:
    
    def explore(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return

        grid[i][j] = 'W'

        self.explore(grid, i + 1, j)  # down
        self.explore(grid, i - 1, j)  # up
        self.explore(grid, i, j + 1)  # right
        self.explore(grid, i, j - 1)  # left



    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        island_count = 0  

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # If we find a land cell ('L'), it means we've found a new island
                if grid[i][j] == 'L':
                    island_count += 1  
                    self.explore(grid, i, j)  

        return island_count  