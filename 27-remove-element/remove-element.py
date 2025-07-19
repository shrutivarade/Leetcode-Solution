class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        i=0
        
        while i<len(nums):
            if nums[i] == val:
                # nums[i:] = nums[i+1:]
                nums.pop(i)
                continue
            i+=1
        return len(nums)

        