class Solution:
    def jump(self, nums: List[int]) -> int:

        l,r = 0,0
        # l and r defines the window with start as l=r+1 and r=farthest
        jump=0

        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            # update to next window
            l = r+1
            r = farthest
            jump+=1
        
        return jump


        

