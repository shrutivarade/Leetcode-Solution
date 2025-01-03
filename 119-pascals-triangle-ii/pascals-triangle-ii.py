class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        dp = [[ 1 for i in range(rowIndex+1)] for i in range(rowIndex+1)]

        for i in range(1, rowIndex+1):
            for j in range(1, rowIndex+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        for i in range(rowIndex+1):
            arr = []
            for j in range(i+1):
                arr.append(dp[j][i-j])
            result.append(arr)
        
        return result[rowIndex]