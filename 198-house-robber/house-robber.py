class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1,2,3,1,0
        nums.append(0)
        for i in range(len(nums)-4, -1, -1):
            nums[i] = max(nums[i]+nums[i+2], nums[i]+nums[i+3])
        return max(nums[0], nums[1])
        