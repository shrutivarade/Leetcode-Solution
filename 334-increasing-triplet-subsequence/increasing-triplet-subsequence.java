class Solution {
    public boolean increasingTriplet(int[] nums) {

        // 
        int num1 = Integer.MAX_VALUE, num2 = Integer.MAX_VALUE;
        for(int n:nums){
            if(n <= num1){
                num1 = n;
            }
            else if(n <= num2){
                num2 = n;
            }
            else{
                return true;
            }
        }
        return false;

        //using leftmin[] and rightmax[] array to compare with the current element:
        // int n = nums.length;
        // if (n < 3){
        //     return false;
        // }
        // int[] leftmin = new int[n];
        // leftmin[0] = nums[0];
        // for(int i=1; i<nums.length; i++){
        //     leftmin[i] = Math.min(leftmin[i-1], nums[i]);
        // }
        // int[] rightmax = new int[n];
        // rightmax[n-1] = nums[n-1];
        // for(int i=n-2; i>=0; i--){
        //     rightmax[i] = Math.max(rightmax[i+1], nums[i]);
        // }
        // for(int i=0; i<n; i++){
        //     if(leftmin[i]<nums[i] && nums[i]<rightmax[i]){
        //         return true;
        //     }
        // }
        // return false;

        // Brute Force:
        // for (int i=0; i<nums.length; i++){
        //     for(int j=i+1; j<nums.length; j++){
        //         for(int k=j+1; k<nums.length; k++){
        //             if(nums[i]<nums[j] && nums[j]<nums[k]){
        //                 return true;
        //             }
        //         }
        //     }
        // }
        // return false;
    }
}