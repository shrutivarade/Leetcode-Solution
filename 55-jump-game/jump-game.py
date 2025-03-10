class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal: #can index(curr position) + val(length of your jump) get you to you destination
                goal = i
        
        return True if goal == 0 else False
        # Move goal from last element to the first element.
        # [2,3,1,1,4*]
        # [2,3,1,1*,4]
        # [2,3,1*,1,4]
        # [2,3*,1,1,4]
        # [2*,3,1,1,4]
