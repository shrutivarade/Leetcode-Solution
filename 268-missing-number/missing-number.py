class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # space O(n) time O(n)
        # n = len(nums)
        # count = set(nums)
        # for i in range(0, n):
        #     if(i not in count):
        #         return i

        # Space O(1), Time O(n), using addition
        res = len(nums)

        for i in range(len(nums)):
            res += (i-nums[i])
        return res









        