class Solution:
    def rob(self, nums: List[int]) -> int:
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

        
        