
class Solution {
    public int maxArea(int[] height) {
        // int area = 0;
        
        // int l = 0;
        // int r = height.length - 1;

        // while (l < r) {
        //     int width = r - l;
            
        //     area = Math.max(area, Math.min(height[l], height[r]) * width);
            
        //     if (height[l] <= height[r]) {
        //         l++;
        //     } else {
        //         r--;
        //     }
        // }
        
        // return area;



        int max = 0;
        int left = 0;
        int right = height.length -1;

        while(left < right){
            if(height[right] >= height[left]){
                max = Math.max(max, height[left] * (right - left));
                left++;
            }
            if(height[left] > height[right]){
                max = Math.max(max, height[right] * (right - left));
                right--;
            }
        
        }
        return max;
    }
    
}

