class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        boxes = list(boxes)
        dict = {}

        for i, val in enumerate(boxes):
            dict[i+1] = val
        
        onesIdx = []
        for i in dict:
            if dict[i] == '1':
                onesIdx.append(i)
        # [3+5+6 - (i+1*len(onesIdx))]
        sumIdx = sum(onesIdx)
        res = []
        
        for i in range(1,n+1):
            ans = 0
            for idx in onesIdx:
                ans = ans + abs(idx-i)
            res.append(ans)

        return res

        # [0 0 1 0 1 1]
        # [1 2 3 4 5 6]

        #  onesIDX = [3 5 6] - 

        # 3-4 + 5-4 + 6-4 = -1 +1 +2 = 4
        