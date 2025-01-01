class Solution:
    def maxScore(self, s: str) -> int:

        # start = 0
        # split = 1
        # end = len(s)-1
        # res = 1
        # while split < end:

        #     # Count zeros on the left side of the split
        #     countl = s[:split+1].count('0')

        #     # Count ones on the right side of the split
        #     countr = s[split:].count('1')

        #     res = max(res, countl + countr)

        #     split+=1
        
        # return res

        n = len(s)
        max_score = 0

        for split in range(1, n):
            # Count zeros on the left side of the split
            left_count = s[:split].count('0')
            # Count ones on the right side of the split
            right_count = s[split:].count('1')

            # Calculate the score for this split
            current_score = left_count + right_count
            max_score = max(max_score, current_score)

        return max_score


        