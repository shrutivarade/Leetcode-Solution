class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Start from last element
        # last elmet itself is an LIS
        # then iterate backward using i and then forward from i->n using j
        # update dp tabel only if nums[j]>nums[i] 
        # and LIS[i]<=LIS[j] to avoid overwrite the value that is updated once,
        # eg. 3,7,101,18, for 3 the dp value should me 3 consisting of 3-7-101 or 3-7-18
        #  but the i->3 and j->101 the value is unnecessarily modified.



        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[j]>nums[i] and LIS[i]<=LIS[j]:
                    LIS[i] = 1+LIS[j]
        return max(LIS)

