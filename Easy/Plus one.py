
""" Que ---> 
https://leetcode.com/problems/plus-one/description/
"""

# Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 10:
                idx = digits.index(digits[i])
                digits[idx] = 0
                if idx == 0:
                    digits.insert(0, 1)
                else:
                    digits[idx-1] += 1

        return digits
