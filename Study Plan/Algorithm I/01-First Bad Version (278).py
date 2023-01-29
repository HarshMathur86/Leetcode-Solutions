
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) is True and isBadVersion(mid-1) is False:
                return mid
            if isBadVersion(mid) is False:
                low = mid + 1
            else:
                high = mid - 1
        print("o")
        return high
