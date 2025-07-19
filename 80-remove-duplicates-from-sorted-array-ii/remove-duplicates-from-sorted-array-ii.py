class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # both the logic works
        if not nums:
            return 0

        i = 1
        j = 1
        count = 1

        while j < len(nums):
            if nums[j] == nums[j - 1]:
                count += 1
                if count > 2:
                    j += 1
                    continue
            else:
                count = 1
            nums[i] = nums[j]
            j += 1
            i += 1

        # del nums[i:]
        # return len(nums)
        return i
        
        # extra space for count
        # i=0
        # j=0
        # while j< len(nums):
        #     count = 1
        #     while j+1 < len(nums) and nums[j] == nums[j+1]:
        #         j+=1
        #         count+=1

        #     for k in range(min(2,count)):
        #         nums[i] = nums[j]
        #         i+=1

        #     j+=1
        # return i

        # pop logic is computationally heavy
        # i = 2
        # while i < len(nums):
        #     if nums[i] == nums[i - 2]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return i+1

        