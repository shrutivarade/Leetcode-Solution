class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        count = 0
        for i in range(len(s)):
            # count += 1

            temp = self.compare(s,i,i)
            # if(len(temp) > len(res)):
            #     res = temp
            count += temp
            
            temp = self.compare(s,i,i+1)
            # if(len(temp) > len(res)):
            #     res = temp
            count += temp

        return count


    def compare(self,s,l,r):
        count = 0
        while((l>=0 and r<len(s)) and s[l] == s[r]):
            l-=1
            r+=1
            count += 1

        return count
        