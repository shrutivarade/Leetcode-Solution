class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {

        // Convert to Array to Set to get the unique values from both the arrays.
        Set<Integer> s1 = new HashSet<Integer>();
        for (int n : nums1){
            s1.add(n);
        }
        Set<Integer> s2 = new HashSet<Integer>();
        for (int n : nums2){
            s2.add(n);
        }

        // Remove the number from set1 present in nums2 and from set2 present in nums1.
        for(int n : nums1){
            if(s2.contains(n)){
                s2.remove(n);
            }
        }
        for(int n : nums2){
            if(s1.contains(n)){
                s1.remove(n);
            }
        }

        // Create List of Lists using ArrayList to ass set1 and set2
        List<List<Integer>> ans = new ArrayList<>();
        for( int i=0; i<2; i++){
            ans.add(new ArrayList());
        }
        for ( Integer s : s1){
            ans.get(0).add(s);
        }
        for ( Integer s : s2){
            ans.get(1).add(s);
        }
        
        return ans;

    }
}