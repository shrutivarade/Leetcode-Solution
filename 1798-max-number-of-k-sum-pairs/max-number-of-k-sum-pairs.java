class Solution {
    public int maxOperations(int[] nums, int k) {
        // Method 3 : using Hashmap and 1 for loop

        // Map<Integer, Integer> map = new HashMap<>();

        // int count = 0;

        // for ( int i = 0; i<nums.length; i++){

        //     int result = k - nums[i];

        //     if( map.containsKey(result) ){
        //         count++;
        //         if(map.get(result) == 1) map.remove(result);
        //         else{
        //             map.put(result, map.get(result)-1);
        //         }
        //     }
        //     else{
        //         map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
        //     }
        // }

        // return count;

        // method 2: using Arrays.sort() and 1 while loop:

        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;
        int count = 0;

        while (left < right) {
            int sum = nums[left] + nums[right];

            if (sum == k) {
                count++;
                left++;
                right--;
            } else if (sum < k) {
                left++;
            } else {
                right--;
            }
        }

        return count;
        
    }
}