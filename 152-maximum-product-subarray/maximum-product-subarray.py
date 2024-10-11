class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #  just because the multiplication operation behaves differently with the negative numbers we need to keep track of the curreMin and currMax values

        maxPro = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if(n==0):
                currMin, currMax = 1, 1
                continue
            
            temp = currMax * n
            currMax = max(n*currMin, n*currMax, n)
            currMin = min(n*currMin, temp, n)
            maxPro = max(maxPro, currMax)

        return maxPro
