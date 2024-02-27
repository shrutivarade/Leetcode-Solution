class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # count = 0
        # def isPrefixAndSuffix(str1, str2):
        #     n = len(str1)
        #     return str2[:n]==str1 and str2[-n:]==str1
        
        # for i in range(len(words)-1):
        #     for j in range(i+1, len(words)):
        #         c = isPrefixAndSuffix(words[i], words[j])
        #         count = count + c
        
        # return count

        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    cnt += 1
        
        return cnt