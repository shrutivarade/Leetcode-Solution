class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Brute Force: O(n^2) -> check each subarray
        # maxsum = nums[0]
        # for i in range(0, len(nums)):
        #     sum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         maxsum = max(maxsum, sum)
        #         sum = sum + nums[j]
        #     maxsum = max(maxsum, sum)    
        # return maxsum        



        # Optimal: O(n) -> sliding window ( No need to check each subarray. we can just discard the prefix if its sum is negative)
        maxS = nums[0]
        sum = 0
        for i in nums:
            if sum<0:
                sum = 0
            sum += i
            maxS = max(maxS,sum)
        return maxS
