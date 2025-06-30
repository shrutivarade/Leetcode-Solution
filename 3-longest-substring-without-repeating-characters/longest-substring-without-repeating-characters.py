class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j = 0, 1
        count = 1
        result = 0
        if len(s)==1:
            return 1
        while j<len(s):
            if s[j] in s[i:j]:
                i+=1
                count -= 1
            else:
                j=j+1
                count += 1
            result = max(result, count)
        return result
        