class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        # sliding window
        i, j = 0, 0
        while j<len(nums):
            if nums[j] - nums[i] > 2*k:
                i+=1
            j+=1

        return j-i
        