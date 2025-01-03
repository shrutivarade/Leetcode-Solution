class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        dp = [[ 1 for i in range(numRows)] for i in range(numRows)]

        for i in range(1, numRows):
            for j in range(1, numRows):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        for i in range(numRows):
            arr = []
            for j in range(i+1):
                arr.append(dp[j][i-j])
            result.append(arr)
        
        return result


        