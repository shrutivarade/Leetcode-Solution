class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height)-1
        area = 0

        while (i<j):
            area = max(area, min(height[i], height[j])*(j-i))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        
        return area


        