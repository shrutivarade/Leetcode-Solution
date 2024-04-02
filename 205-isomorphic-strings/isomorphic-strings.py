class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if(len(set(s)) != len(set(t))):
            return False

        dict = {}
        for i in range(0, len(s)):

            if(s[i] in dict):
                if(dict.get(s[i]) != t[i]):
                    return False
            
            dict[s[i]] = t[i]


        return True

        #one liner
        # return len(set(s))==len(set(t))==len(set(zip(s,t)))
        