class Solution {
    public int longestSubarray(int[] nums) {
        
        int max = 0;
        int atmost = 0;
        int l = 0;
        for ( int r=0; r<nums.length; r++){
            if(nums[r]==0){
                atmost++;
            }
            while(atmost>1){
                if(nums[l]==0){
                    atmost--;
                }
                l++;
            }
            max = Math.max(max,r-l);
        }
        return max;

    }
}