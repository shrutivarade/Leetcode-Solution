class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        # res = [1,1,2,6]

        postfix = 1
        for i in range((len(nums) - 1), -1, -1):
            res[i] *= postfix  # [1,1,2,6] * [24,12,4,1]
            postfix *= nums[i] # postfix = 4,12,24

        return res