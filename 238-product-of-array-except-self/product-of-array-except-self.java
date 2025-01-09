
class Solution {
    public int[] productExceptSelf(int[] nums) {

        int len = nums.length;

        int[] res = new int[len];
        for (int i = 0; i < len; i++) {
            res[i] = 1;
        }

        int prefix = 1;
        for ( int i=0; i<len; i++){
            res[i] = prefix;
            prefix *= nums[i];
        }

        int postfix = 1;
        for( int i=len-1; i>=0; i--){
            res[i] *= postfix;
            postfix *= nums[i];
        }
    
        return res;
    }
}

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    //     // Get the length of the input array
    //     int length = nums.length;

    //     // Initialize the left product array with 1
    //     int[] L = new int[length];
    //     L[0] = 1;
    //     // Calculate the product of all elements to the left of each index
    //     for (int i = 1; i < length; i++) {
    //         L[i] = nums[i - 1] * L[i - 1];
    //     }

    //     // Initialize the right product array with 1
    //     int[] R = new int[length];
    //     R[length - 1] = 1;
    //     // Calculate the product of all elements to the right of each index
    //     for (int i = length - 2; i >= 0; i--) {
    //         R[i] = nums[i + 1] * R[i + 1];
    //     }

    //     // Calculate the final product by multiplying the corresponding left and right products
    //     int[] answer = new int[length];
    //     for (int i = 0; i < length; i++) {
    //         answer[i] = L[i] * R[i];
    //     }
    //     return answer;
    // }

