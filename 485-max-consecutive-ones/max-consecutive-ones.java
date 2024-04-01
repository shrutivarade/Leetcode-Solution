class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        // if we encounter 0, then reset the counter and keep track of the max value.

        int count = 0, max=0;
        for( int i=0; i<nums.length; i++){
            if(nums[i]==0){
                count = 0;
                // max = Math.max(max,count);
            }else{
                count += 1;
            }
            max = Math.max(max,count);
        }

        return max;



        
    }
}