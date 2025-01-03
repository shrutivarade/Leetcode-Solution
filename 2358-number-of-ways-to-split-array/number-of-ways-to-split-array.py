class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     sum1 = sum(nums[:i+1])
        #     sum2 = sum(nums[n-(n-i-1):])
        #     if sum1>=sum2 and 0<=i<n-1:
        #         count+=1
        # return count

        n=len(nums)
        Sum=sum(nums)
        acc, cnt=0, 0
        for i in range(n-1):
            acc+=nums[i]
            cnt+=(2*acc>=Sum)
        return cnt