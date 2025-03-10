class Solution:
    def rob(self, nums: List[int]) -> int:

        # Dynamic Programming
        n = len(nums)
        dp = [0] * n
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]

        for i in range(n-3, -1, -1):
            dp[i] = nums[i] + max(dp[i+2:])
        return max(dp)
        
        
        
        
        # # 1,2,3,1,0
        # nums.append(0)
        # for i in range(len(nums)-4, -1, -1):
        #     nums[i] = max(nums[i]+nums[i+2], nums[i]+nums[i+3])
        # return max(nums[0], nums[1])
        