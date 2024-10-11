class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force: O(n^2)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]
        return []

        # Optimal: O(n)
        # dict = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in dict:
        #         return [dict[target - nums[i]], i]
        #     dict[nums[i]] = i

        # return []

