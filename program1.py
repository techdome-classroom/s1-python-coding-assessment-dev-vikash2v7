class Solution:
   
   
    def explore(grid, i, j):
        
        if i < 0 or i >= len(grid) or j < 0 or grid[i][j] == 'W' or j >= len(grid[0]) :
            return

        grid[i][j] = 'W'

        explore(grid, i + 1, j)  
        explore(grid, i - 1, j)  
        explore(grid, i, j + 1)  
        explore(grid, i, j - 1)  



    def getTotalIsles(self, grid: list[list[str]]) -> int:

        if not grid:  
            return 0

        island_count = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  # Found an unvisited landmass
                    island_count += 1   # Start a new island
                    explore(grid, i, j)     # Visit all parts of the island

        return island_count
                        
