class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            print(nums.index(target))
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
