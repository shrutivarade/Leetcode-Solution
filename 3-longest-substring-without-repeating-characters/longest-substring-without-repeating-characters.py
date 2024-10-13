class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substr = {}
        maxLen = 0

        i, j = 0, 0
        while j < len(s):
            if s[j] in substr:
                i = max(substr[s[j]]+1, i)

            # first add the element and later update the value
            substr[s[j]] = j

            maxLen = max(maxLen, j-i+1)
            j += 1

        return maxLen
            

        