class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        result = 0 
        
        i, j = 0, 0 #start pointer and moving pointer
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        while (j<len(s)): # j is the moving pointer that expands the window
            if s[j] in vowels:
                count = count + 1
            
            if j-i+1 > k: #check window size
                if s[i] in vowels: # if the character that we are planning to exclude because we exceed the window size, is a vowel, then remove it from window and decrement the counter
                    count = count - 1  
                i = i + 1 # i is the start pointer that collapses the window
            
            result = max(result, count)
            j = j + 1
        return result
        