class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # return 0

        # def greatest_factor_excluding_self(number):
        #     for i in range(number // 2, 1, -1):
        #         if number % i == 0:
        #             return i 
        #     return float('inf') 
        # result = float('inf')
        # for n in nums:
        #     result = min(result, greatest_factor_excluding_self(n))
        # return result

        # smallest = int (sum(nums) / (len(nums) + maxOperations))
        # while maxOperations > 0:
        #     maxNum = max(nums)
        #     nums.remove(maxNum)
        #     nums.append(maxNum-smallest)
        #     nums.append(smallest)
        #     maxOperations -= 1
        # print(nums)
        # return max(nums)

        low, high = 1, max(nums) # min and max posible bags
        while low < high:
            mid = (low + high) // 2
            sum = 0
            for n in nums:
                sum += (n - 1) // mid 

            if sum <= maxOperations: 
                high = mid
            else: 
                low = mid + 1
        return high
        


        






