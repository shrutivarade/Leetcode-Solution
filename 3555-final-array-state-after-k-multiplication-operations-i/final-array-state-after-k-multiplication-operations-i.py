class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        while k>0:
            x = min(nums)
            idx = nums.index(x)

            nums[idx] = x*multiplier
            k-=1
        return nums
