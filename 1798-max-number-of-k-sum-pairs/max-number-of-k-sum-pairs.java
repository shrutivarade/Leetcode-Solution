class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        int count = 0;

        for ( int i = 0; i<nums.length; i++){

            int result = k - nums[i];

            if( map.containsKey(result) ){
                count++;
                if(map.get(result) == 1) map.remove(result);
                else{
                    map.put(result, map.get(result)-1);
                }
            }
            else{
                map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
            }
        }

        return count;
        
    }
}