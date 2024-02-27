class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # first we concatenate both the strings to check whether the result of concatenation is same or not.
        #  if str1 = ABCABC and str2 = ABC, then concatenation should be ABCABCABC if we do (str1+str2 or str2+str1)
         # for str1 = LEET and str2 = CODE
        if str1 + str2 != str2 + str1: 
            return ""

        # now calcuate the gcd of both the string and return the substring starting from 0 to gcd of str1,str2
        from math import gcd
        result = str1[0: gcd(len(str1),len(str2))]

        return result