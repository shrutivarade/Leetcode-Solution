class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # unique characters from both the strings should be same.
        if(set(word1)!=set(word2)):
            return False
        
        # create a dictionary to track count of characters in both the strings.
        # frequency of all keys.
        k1 = Counter(word1)
        k2 = Counter(word2)
        # if(k1 != k2):
        #     return False

        # frequency of all values
        v1 = Counter(list(k1.values()))
        v2 = Counter(list(k2.values()))
        if(v1 != v2):
            return False
        
        return True