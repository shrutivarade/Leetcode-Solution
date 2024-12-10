class Solution:
    def maximumLength(self, s: str) -> int:
        map = {}

        for i in range(0,len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in map:
                    map[s[i:j+1]] += 1
                else:
                    map[s[i:j+1]] = 1   
        res = -1
        for substr in map:
            if map[substr] >= 3 and len(set(substr)) == 1:
                res = max(res, len(substr))

        return res if res>-1 else -1
        