class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] == 0:
                count += 1
                nums.remove(0)
                nums.append(0)
