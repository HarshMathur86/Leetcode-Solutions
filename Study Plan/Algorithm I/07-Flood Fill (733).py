class Solution:
    image = None
    start_color = None
    color = None
    def paintColor(px, py):
        print(px, py)
        try:
            if px < 0 or py < 0:
                return
            if Solution.image[px][py] == Solution.color:
                return
            if Solution.image[px][py] == Solution.start_color:
                Solution.image[px][py] = Solution.color
            else:
                return
        except:
            return
        # four direction
        # up
        Solution.paintColor(px-1, py)
        # down
        Solution.paintColor(px+1, py)
        # right
        Solution.paintColor(px, py+1)
        # left
        Solution.paintColor(px, py-1)
    

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Solution.image = image
        Solution.start_color = image[sr][sc]
        Solution.color = color
        # Four direction calling
        Solution.paintColor(sr, sc)
        return Solution.image
