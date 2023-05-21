class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            val_mid = nums[mid]
            if  val_mid == target:
                return True
            if val_mid < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if self.search(row, target):
                return True

        return False