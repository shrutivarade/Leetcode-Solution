class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums) # -> O(n)

        # Bruteforce: Linear search ->  O(n)

        # Optimal: Binary Search -> O(log n)
        # l, r = 0 , len(nums)-1
        # if nums[l]<nums[r]: # no rotation
        #     return nums[l]
        # while(l<r):
        #     mid = (l+r)//2
        #     if(nums[mid]>nums[r]):
        #         l = mid+1
        #     else:
        #         r = mid
        # return nums[l]
        