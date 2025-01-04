class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:

        # bruteforce with parcal triangle
        # pos = [[1] * n] * m
        # for i in range(1,m):
        #     for j in range(1,n):
        #         pos[i][j] = pos[i-1][j] + pos[i][j-1]
        # return pos[m-1][n-1]

        # Permutation and combination.
        return comb(m+n-2, m-1)

        # tabulation:
        dp = [[1 for i in range(m)] for j in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = d[i-1][j] + d[i][j-1]
        return dp[n-1][m-1]




            



        