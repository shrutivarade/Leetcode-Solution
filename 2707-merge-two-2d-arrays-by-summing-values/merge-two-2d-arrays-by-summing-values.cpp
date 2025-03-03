class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        
        int i=0, j=0;

        vector<vector<int>> res;

        while ( i< nums1.size() && j<nums2.size()){
            int key1 = nums1[i][0];
            int key2 = nums2[j][0];
            if( key1 == key2){
                int sum = nums1[i][1] + nums2[j][1];
                res.push_back({key1, sum});
                i++;
                j++;
            }
            else{
                // Append the vector with the smaller key
                if(key1<key2){
                    res.push_back(nums1[i]);
                    i++;
                }
                else{
                    res.push_back(nums2[j]);
                    j++;
                }
            }
        }

        // Append any remaining elements from nums1
        while (i < nums1.size()) {
            res.push_back(nums1[i]);
            i++;
        }
        // Append any remaining elements from nums2
        while (j < nums2.size()) {
            res.push_back(nums2[j]);
            j++;
        }
        
        return res; 
    }
};