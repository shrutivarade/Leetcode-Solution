class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # # unique characters from both the strings should be same.
        # if(set(word1)!=set(word2)):
        #     return False
        
        # # create a dictionary to track count of characters in both the strings.

        # k1 = Counter(word1)
        # k2 = Counter(word2)
        

        # # frequency of all values
        # v1 = Counter(list(k1.values()))
        # v2 = Counter(list(k2.values()))
        # if(v1 != v2):
        #     return False
        
        # return True


        # if any characters are different immediately return False
        unique1, unique2 = set(word1), set(word2)
        if unique1 != unique2: return False

        freq1 = sorted([word1.count(i) for i in unique1])
        freq2 = sorted([word2.count(i) for i in unique2])

        return freq1 == freq2