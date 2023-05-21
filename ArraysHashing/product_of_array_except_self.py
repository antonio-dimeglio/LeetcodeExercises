class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            l[i] = prefix
            prefix *= nums[i]

        postfix = 1 

        for j in range(len(nums) - 1, -1, -1):
            l[j] *= postfix
            postfix *= nums[j]



        return l
