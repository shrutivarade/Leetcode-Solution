class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

        # l, r = 0 , len(nums)-1

        # while(l<r):

        #     mid = (l+r)//2

        #     if(nums[mid]>nums[r]):
        #         l = mid+1
        #     else:
        #         r = mid-1
        # return nums[r]
        