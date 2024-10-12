class Solution:
    def tribonacci(self, n: int) -> int:

        t0=0
        t1=1
        t2=1
        ti=0
        if(n==1 or n==2):
            return t1

        for i in range(2,n):
            ti = t0 + t1 + t2
            
            t0=t1
            t1=t2
            t2=ti
        
        return ti


        