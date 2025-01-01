class Solution:
    def maxScore(self, s: str) -> int:

        start = 0
        split = 1
        end = len(s)-1
        res = 0
        while split <= end:
            countl = s[start:split].count('0')
            countr = s[split:end+1].count('1')
            res = max(res, countl + countr)
            split+=1
        return res

        # n = len(s)
        # max_score = 0

        # for split in range(1, n):
 
        #     left_count = s[:split].count('0')

        #     right_count = s[split:].count('1')

        #     max_score = max(max_score, left_count + right_count)

        # return max_score


        