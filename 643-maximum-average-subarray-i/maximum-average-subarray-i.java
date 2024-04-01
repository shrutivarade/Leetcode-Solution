public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Initialize a variable to store the sum of the first 'k' elements.
        double sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i]; // Summing up the first 'k' elements.

        // Initialize a variable 'res' to store the maximum average.
        double res = sum;

        // Loop through the array starting from index 'k'.
        for (int i = k; i < nums.length; i++) {
            // Add the current element and subtract the element that's k positions behind the current one.
            sum += nums[i] - nums[i - k];
            // Update 'res' with the maximum of 'res' and 'sum'.
            res = Math.max(res, sum);
        }
        
        // Return the maximum average by dividing 'res' by 'k'.
        return res / k;
    }
}

