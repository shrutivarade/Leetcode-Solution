class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        # max = 0 
        # for i in range(n):
        #     if max < candies[i]:
        #         max = candies[i]

        greatest = max(candies)
        
        result = []

        for j in range(n):
            if candies[j] + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        
        return result
