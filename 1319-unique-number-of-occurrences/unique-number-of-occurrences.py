class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        map = {}

        for i in arr:
            if i in map:
                map[i] = map[i]+1
            else:
                map[i] = 1

        # for i in arr:
        #     if i in map.keys():
        #         map.update({i:map.get(i)+1})
        #     else:
        #         map.setdefault(i,1)


        if(len(map.values()) != len(set(map.values()))):
            return False
        else:
            return True