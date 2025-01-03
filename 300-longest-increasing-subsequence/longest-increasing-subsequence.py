class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[j]>nums[i] and LIS[i]<=LIS[j]:
                    LIS[i] = 1+LIS[j]
        return max(LIS)




        
























        # n = len(nums)

        # lis = [1] * n

        # for i in range(1,n):
        #     for j in range(0,i):
        #         if((nums[i] > nums[j]) and lis[i] <=lis[j]):
        #             lis[i] = 1+lis[j]
        # return max(lis)