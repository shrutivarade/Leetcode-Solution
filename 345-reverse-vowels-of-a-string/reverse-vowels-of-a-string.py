# class Solution:
#     def reverseVowels(self, s: str) -> str:

#         s = list(s)
#         n = len(s)

#         vowels = set(['a', 'e', 'i', 'o', 'u'])

#         i = 0
#         j = n-1

#         while i < j:
             
#             if ( s[i] in vowels and s[j] in vowels):
#                 s[i] , s[j] = s[j] , s[i]
#                 i+=1
#                 j-=1

#             else:
#                 if(s[i] not in vowels):
#                     i += 1
#                 if(s[j] not in vowels):
#                     j -= 1
            
#         return ''.join(s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels=set('AEIOUaeiou')
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s