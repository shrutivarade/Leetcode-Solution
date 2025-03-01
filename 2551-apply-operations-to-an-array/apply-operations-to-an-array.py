class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        # logic to iterate over the nums array 0->n-1
        for i in range(n-1):
            if(nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        nonZeros = []
        for num in nums:
            if num != 0:
                nonZeros.append(num)
        
        while len(nonZeros) != n:
            nonZeros.append(0)

        return nonZeros



        