# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:    

#         vowels = ['a', 'e', 'i', 'o', 'u']
#         ans = []

#         dictwords = {}
#         for word in words:
#             if word[0] in vowels and word[len(word)-1] in vowels:
#                 dictwords[word] = True
#             else:
#                 dictwords[word] = False
            
#         for q in queries:
#             count=0
#             subarr = words[q[0]:q[1]+1]
#             for word in subarr:
#                 if dictwords[word]:
#                     count+=1
#             ans.append(count)
        
#         return ans


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        Prefix = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            Prefix[i + 1] = Prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                Prefix[i + 1] += 1

        ANS = []
        for query in queries:
            ANS.append(Prefix[query[1] + 1] - Prefix[query[0]])

        return ANS

