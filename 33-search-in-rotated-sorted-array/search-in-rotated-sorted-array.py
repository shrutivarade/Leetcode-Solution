class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = 0

        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] == target):
                return mid

            if(nums[l]<=nums[mid]):
                # left is sorted, right is unsorted
                if(target<nums[mid] and target>=nums[l]):
                    r = mid-1
                else:
                    l = mid+1
            else:
                # right sorted, left is unsorted
                if(target>nums[mid] and target<=nums[r]):
                    l = mid+1
                else:
                    r = mid-1
        return -1
