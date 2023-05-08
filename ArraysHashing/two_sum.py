class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            if n in d.keys() and d[n] != i:
                return [d[n], i]
            else:
                d[target-n] = i
                
        return []
