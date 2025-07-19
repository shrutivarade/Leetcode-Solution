class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # both the logic works
        
        # i=0
        # j=1

        # while j<len(nums):
        #     if(nums[j] != nums[i]):
        #         i+=1
        #         nums[i] = nums[j]
     
        #     j+=1
        # return i+1

        i=1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                continue
            i+=1
        return len(nums)
