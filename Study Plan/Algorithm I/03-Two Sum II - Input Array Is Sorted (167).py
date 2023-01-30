class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            if numbers[i]+numbers[i+1] == target:
                return [i+1, i+2]

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
