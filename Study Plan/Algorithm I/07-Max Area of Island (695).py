class Solution:
    grid = None
    land = []
    cur_area = 0

    def calculateArea(x, y):
        if [x, y] in Solution.land:
            Solution.cur_area += 1
            Solution.land.remove([x,y])
        else:
            return
        
        # four direction
        # up
        Solution.calculateArea(x-1, y)
        # down
        Solution.calculateArea(x+1, y)
        # right
        Solution.calculateArea(x, y+1)
        # left
        Solution.calculateArea(x, y-1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        Solution.land = []
        areas = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    Solution.land.append([i, j])
        
        while len(Solution.land) > 0:
            Solution.cur_area = 0
            Solution.calculateArea(Solution.land[0][0], Solution.land[0][1])
            areas.append(Solution.cur_area)
        
        if len(areas) == 0:
            return 0
        else:
            return max(areas)