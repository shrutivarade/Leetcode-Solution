class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     sum1 = sum(nums[:i+1])
        #     sum2 = sum(nums[n-(n-i-1):])
        #     if sum1>=sum2 and 0<=i<n-1:
        #         count+=1
        # return count

        left = 0
        right = (sum(nums) + 1) // 2
        res = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= right:
                res += 1
        return res
