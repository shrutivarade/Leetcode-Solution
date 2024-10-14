class Solution:
    def climbStairs(self, n: int) -> int:

        #its basically a fibonacci series
        # 2-2
        # 3-3
        # 4-5
        # 5-8
        # 6-13
        # 7-21

        if n < 0:
            return -1 # Invalid input
        elif n == 0:
            return 0 # Base case: n is 0, return 0
        elif n == 1:
            return 1 # Base case: n is 1, return 1
        else:
            a = 0
            b = 1
            for i in range(2, n+2):
                c = a + b
                a = b
                b = c
            return b