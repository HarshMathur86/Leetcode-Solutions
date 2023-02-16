# Brute Force approach needed to optimize later


class Solution:
    time = 0
    grid = None

    def isRottingPossible():
        for i in range(len(Solution.grid)):
            for j in range(len(Solution.grid[0])):
                if Solution.grid[i][j] == 1:
                    try:
                        if i-1 >= 0 and Solution.grid[i-1][j] == 2:
                            return True
                    except:
                        pass
                    try:
                        if i+1 >= 0 and Solution.grid[i+1][j] == 2:
                            return True
                    except:
                        pass
                    try:
                        if j-1 >= 0 and Solution.grid[i][j-1] == 2:
                            return True
                    except:
                        pass
                    try:
                        if j+1 >= 0 and Solution.grid[i][j+1] == 2:
                            return True
                    except:
                        pass
        
        return False
                    
    def expansion(i, j):
        try:
            if i < 0 or j < 0:
                return
            if Solution.grid[i][j] == 2:
                # expansion in all four directions
                try:
                    if i-1 >= 0 and Solution.grid[i-1][j] == 1:
                        Solution.grid[i-1][j] = 2
                except:
                    pass
                try:
                    if i+1 >= 0 and Solution.grid[i+1][j] == 1:
                        Solution.grid[i+1][j] = 2
                except:
                    pass
                try:
                    if j-1 >= 0 and Solution.grid[i][j-1] == 1:
                        Solution.grid[i][j-1] = 2
                except:
                    pass
                try:
                    if j+1 >= 0 and Solution.grid[i][j+1] == 1:
                        Solution.grid[i][j+1] = 2
                except:
                    pass
        except:
            return

    def orangesRotting(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        time = 0

        while Solution.isRottingPossible():
            indexes = []
            for i in range(len(Solution.grid)):
                for j in range(len(Solution.grid[0])):
                    if Solution.grid[i][j] == 2:
                        indexes.append([i, j])
            
            #print(indexes)
            
            for i, j in indexes:
                Solution.expansion(i, j)

            """for i in range(len(Solution.grid)):
                for j in range(len(Solution.grid[0])):
                    print(Solution.grid[i][j], end=" ")
                print()"""

            time += 1

        if 1 in [ele for row in Solution.grid for ele in row]:
            return -1
        
        return time








