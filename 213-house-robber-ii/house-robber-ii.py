class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def HR1(num):
            n = len(num)
            dp = [0] * n
            dp[n-1] = num[n-1]
            dp[n-2] = num[n-2]

            for i in range(n-3, -1, -1):
                dp[i] = num[i] + max(dp[i+2:])
            return max(dp)

        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)

        return max(HR1(nums[1:]), HR1(nums[:len(nums)-1]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        # 2,3,2,0
        # 1,2,3,1,0
        if len(nums)<=3: return max(nums)
        arr = nums.copy()

        nums.append(0)
        for i in range(len(nums)-4, 0, -1):
            nums[i] = max(
                nums[i]+nums[i+3], 
                nums[i]+nums[i+2]
                )
        max1 = max(nums[1], nums[2])
        print("Max1",max1)

        nums = arr
        nums[-1] = 0
        print(nums)
        for i in range(len(nums)-4, -1, -1):
            nums[i] = max(
                nums[i]+nums[i+3], 
                nums[i]+nums[i+2]
                )
        max2 = max(nums[0], nums[1])
        print(max2)

        return max(max1, max2)

        
        