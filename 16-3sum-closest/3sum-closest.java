class Solution {
    public int threeSumClosest(int[] nums, int target) {

        int diff = Integer.MAX_VALUE, sum=0;

        Arrays.sort(nums);
        
        for(int i =0; i<nums.length && diff!=0; i++){
            int l = i+1;
            int r = nums.length-1;

            while(l<r){

                sum = nums[i] + nums[l] + nums[r];

                if(Math.abs(target - sum) < Math.abs(diff)){
                    diff = target - sum;
                }

                if(sum < target){
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        
        return target-diff;
    }
}