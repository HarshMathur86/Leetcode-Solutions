
""" Que ---> 2133
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
"""

# Solution

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # rows
        N = len(matrix[0])
        for row in matrix:
            for i in range(1, N+1):
                if i not in row:
                    return False
            
        for i in range(N):
            col = [row[i] for row in matrix]
            for i in range(1, N+1):
                if i not in col:
                    return False

        return True
