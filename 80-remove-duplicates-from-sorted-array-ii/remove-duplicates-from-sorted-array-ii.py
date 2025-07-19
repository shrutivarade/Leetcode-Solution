class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # both the logic works
        
        # extra space for count
        i=0
        j=0
        while j< len(nums):
            count = 1
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j+=1
                count+=1

            for k in range(min(2,count)):
                nums[i] = nums[j]
                i+=1

            j+=1
        return i

        # pop logic is computationally heavy
        # i = 2
        # while i < len(nums):
        #     if nums[i] == nums[i - 2]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return i+1

        