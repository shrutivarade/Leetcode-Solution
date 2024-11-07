class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # i=0
        # j=1

        # while j<len(nums):
        #     if(nums[j] != nums[i]):
        #         i+=1
        #         nums[i] = nums[j]
        #     j+=1

        # return i+1


        i=1 #since first number is already sorted
        for j in range(1, len(nums)):
            if(nums[j] != nums[j-1]):
                nums[i] = nums[j]
                i+=1
        return i