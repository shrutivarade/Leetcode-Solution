class Solution {
    public int maxProduct(int[] nums) {

        // Initialize variables
        int currMax = nums[0];
        int currMin = nums[0];
        int maxPro = nums[0]; // Start with the first element as the initial maximum

        // Traverse the array from the second element
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            // Swap currMax and currMin if num is negative
            if (num < 0) {
                int temp = currMax;
                currMax = currMin;
                currMin = temp;
            }

            // Update currMax and currMin
            currMax = Math.max(num, currMax * num);
            currMin = Math.min(num, currMin * num);

            // Update maxPro to store the maximum product found so far
            maxPro = Math.max(maxPro, currMax);
        }

        return maxPro;
    }
}