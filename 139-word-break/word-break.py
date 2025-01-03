class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # max_len = max(map(len, wordDict))  # The maximum length of a word in the dictionary

        # for i in range(1, n + 1):   # loop for s
        #     for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
        #         print("s[j:i]: ", s[j:i])
        #         if dp[j] and s[j:i] in wordDict:
        #             print("In if, s[j:i]: ", s[j:i])
        #             dp[i] = True
        #             break
        #     print("j at the time of termination: ", j)

        # return dp[n]


        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1 ,-1):
            for w in wordDict:

                if i+len(w)<=len(s) and s[i: i+len(w)] == w:

                    dp[i] = dp[i+len(w)]
                
                if dp[i]:
                    break
        
        return dp[0]


