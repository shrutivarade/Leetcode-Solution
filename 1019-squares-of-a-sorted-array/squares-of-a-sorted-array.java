class Solution {
    public int[] sortedSquares(int[] nums) {

        // solution 1: O(n log n)

        // for(int i=0; i<nums.length; i++){
        //     nums[i] = Math.abs(nums[i] * nums[i]);
        // }
        
        // Arrays.sort(nums);
        // return nums;
        

        //  Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

        // Solution 2: O(n)
        // this solution work in reverse order because we already have a sorted array

        int len = nums.length;
        int[] result = new int[len];
        int rightIndex = len - 1;
        int leftIndex = 0;

        for(int i = len-1; i>=0; i--){
            if(Math.abs(nums[leftIndex]) > Math.abs(nums[rightIndex])){
                result[i] = nums[leftIndex] * nums[leftIndex];
                leftIndex++;
            } else {
                result[i] = nums[rightIndex] * nums[rightIndex];
                rightIndex--;
            }
        }
        return result;

    }
}