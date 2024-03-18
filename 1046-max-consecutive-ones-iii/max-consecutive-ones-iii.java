class Solution {
    public int longestOnes(int[] nums, int k) {

        int max=0;
        int l = 0;
        for(int r=0; r<nums.length; r++){
            if(nums[r]==0){
                k--;
            }
            while(k<0){
                if(nums[l]==0){
                    k++;
                }
                l++;
            }
            max = Math.max(max, r-l+1);
        }

     
        return max;
        
    }
}