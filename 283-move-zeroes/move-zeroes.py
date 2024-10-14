class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0

        while (i<len(nums) and nums[i] != 0) and (j<len(nums) and nums[j] != 0):
                i+=1
                j+=1
        while j<len(nums):
            while j < len(nums) and nums[j] == 0:
                j+=1
            if(j < len(nums)):
                temp = nums[j]
                nums[j] = 0
                nums[i] = temp
            i+=1
                


                
        