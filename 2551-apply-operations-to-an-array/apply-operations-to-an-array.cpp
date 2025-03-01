class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();

        for(int i=0; i<n-1; i++){
            if(nums[i] == nums[i+1]){
                nums[i] *= 2;
                nums[i+1] = 0;
            }
        }

        vector<int> nonZeros;
        for(int num : nums){
            if(num != 0){
                nonZeros.push_back(num);
            }
        }

        // Append zeros until the nonZeros vector has size n
        while(nonZeros.size() != n){
            nonZeros.push_back(0);
        }

        return nonZeros;

    }
};