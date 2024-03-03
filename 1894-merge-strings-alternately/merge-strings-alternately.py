class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Using array 
        # ans = []
        # i, j = 0, 0

        # while i < len(word1) and j < len(word2):
        #     ans.append(word1[i])
        #     ans.append(word2[j])
        #     i +=1
        #     j +=1
        
        # ans.append(word1[i:])
        # ans.append(word2[j:])
        # return ''.join(ans)


        # using string operations
        # i=0
        # j=0
        # word3 = ''
        # while((i<len(word1) and (j<len(word2)))):
        #     word3 = word3 + word1[i] + word2[j]
        #     i += 1
        #     j += 1
        # while(i<len(word1)):
        #     word3 = word3 + word1[i]
        #     i += 1
        # while(j<len(word2)):
        #     word3 = word3 + word2[j]
        #     j += 1
        # return word3

        # Using min() and Slicing
        n1 = len(word1)
        n2 = len(word2)
        result = ""
        for i in range(0,min(n1,n2)):
            result = result + word1[i] + word2[i]

        if(n1 < n2):
            result = result + word2[n1:]
        else:
            result = result + word1[n2:]
        
        return result