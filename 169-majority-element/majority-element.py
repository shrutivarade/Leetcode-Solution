class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Simple Hashmap technique
        # n = len(nums)
        # hashmap = Counter(nums)
        # for val, count in hashmap.items():
        #     if count > n/2:
        #         return val

        # two pointers for O(1) space;
        nums.sort()
        count =1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count +=1
                if count>len(nums)/2:
                    return nums[i]
            else:
                count = 1
        
        return nums[0]



