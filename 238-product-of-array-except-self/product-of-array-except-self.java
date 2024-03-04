
class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Get the length of the input array
        int length = nums.length;

        // Initialize the left product array with 1
        int[] L = new int[length];
        L[0] = 1;
        // Calculate the product of all elements to the left of each index
        for (int i = 1; i < length; i++) {
            L[i] = nums[i - 1] * L[i - 1];
        }

        // Initialize the right product array with 1
        int[] R = new int[length];
        R[length - 1] = 1;
        // Calculate the product of all elements to the right of each index
        for (int i = length - 2; i >= 0; i--) {
            R[i] = nums[i + 1] * R[i + 1];
        }

        // Calculate the final product by multiplying the corresponding left and right products
        int[] answer = new int[length];
        for (int i = 0; i < length; i++) {
            answer[i] = L[i] * R[i];
        }
        return answer;
    }
}
