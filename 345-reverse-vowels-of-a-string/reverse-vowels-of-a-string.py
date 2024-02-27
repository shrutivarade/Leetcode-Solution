class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        n = len(s)

        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        i = 0
        j = n-1

        while i < j:
             
            if ( s[i] in vowels and s[j] in vowels):
                s[i] , s[j] = s[j] , s[i]
                i+=1
                j-=1

            else:
                if(s[i] not in vowels):
                    i += 1
                if(s[j] not in vowels):
                    j -= 1
            
        return ''.join(s)