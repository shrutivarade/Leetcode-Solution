class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # focus on minimizing the difference between the target and the sum.

        diff = float('inf')
        nums.sort()
        for i, a in enumerate(nums):
            l, r = i+1, len(nums)-1
            while(l<r):
                sum = a + nums[l] + nums[r]

                if abs(target-sum) <  abs(diff):
                    diff = abs(target-sum)

                    # keep track of this sum to return it as result
                    res = sum

                if sum > target:
                    r-=1
                else:
                    l+=1
            
        return res


