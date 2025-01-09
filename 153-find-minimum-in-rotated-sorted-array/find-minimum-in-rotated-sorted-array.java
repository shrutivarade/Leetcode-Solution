
class Solution {
    public int findMin(int[] nums) {
        int l = 0;                      
        int r = nums.length - 1;        

        while (l <= r) {                
            if (nums[l] <= nums[r]) {   
                return nums[l];        
            }
            int mid = (l + r) / 2;      

            if (nums[mid] >= nums[l]) { // we are in the left portion
                l = mid + 1;            
            } else { // we are in the right portion
                r = mid;                
            }
        }
        return 0;                      
    }
}


// Time complexity analysis:
// - The code uses a while loop to perform binary search, and the loop runs until the left pointer is less than or equal to the right pointer. In each iteration, the search space is halved.
// - Since the binary search is dividing the search space in half at each step, the time complexity of the binary search algorithm is O(log n), where n is the length of the input array 'nums'.
// - Therefore, the overall time complexity of the provided code is O(log n), where n is the length of the input array 'nums'. The algorithm efficiently finds the minimum element in the rotated sorted array using binary search, resulting in logarithmic-time complexity.