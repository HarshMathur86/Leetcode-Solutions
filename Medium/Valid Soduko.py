# Que ---> https://leetcode.com/problems/valid-sudoku/description/

# Solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # printing
        #for row in board:
        #    print(" ".join(row))

        # checking row repition
        for row in board:
            numeric_vals = [x for x in row if x.isnumeric()]
            if len(numeric_vals) != len(set(numeric_vals)):
                return False

        # checking column repition
        for i in range(9):
            numeric_vals = [x for x in [row[i] for row in board] if x.isnumeric()]
            if len(numeric_vals) != len(set(numeric_vals)):
                return False

        # checkin 3x3 blocks
        for i in range(0, 7, 3):
            h_panel = board[0+i : 3+i]
            for j in range(0, 7, 3):
                block = [row[0+j : 3+j] for row in h_panel]
                block_ele = []
                for row in block:
                    block_ele += row
                block_ele = [x for x in block_ele if x.isnumeric()]
                if len(block_ele) != len(set(block_ele)):
                    return False

        return True
