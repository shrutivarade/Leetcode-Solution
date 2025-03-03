class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        int i=0, j=0;
        List<int[]> res = new ArrayList<>();

        while( i<nums1.length && j<nums2.length){
            int key1 = nums1[i][0];
            int key2 = nums2[j][0];

            if (key1 == key2){
                int sum = nums1[i][1] + nums2[j][1];
                res.add(new int[] {key1, sum});
                i++;
                j++;
            }
            else{

                if (key1<key2){
                    res.add(nums1[i]);
                    i++;
                }
                else{
                    res.add(nums2[j]);
                    j++;
                }

            }
        }

        while (i < nums1.length) {
            res.add(nums1[i]);
            i++;
        }
        
        while (j < nums2.length) {
            res.add(nums2[j]);
            j++;
        }

        // Convert the List<int[]> to int[][]
        int[][] ans = new int[res.size()][2];
        for( int k=0; k<res.size(); k++){
            ans[k] = res.get(k);
        }

        return ans;

    }
}