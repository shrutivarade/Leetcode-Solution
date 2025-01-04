# class Solution:
#     def canJump(self, nums: List[int]) -> bool:

#         i=0
#         while i<len(nums):

#             if i<len(nums)-1 and nums[i]==0:
#                 return False

#             i += nums[i]
#             if(i==nums[len(nums)-1]):
#                 return True
        

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True