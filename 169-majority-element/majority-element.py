class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        hashmap = Counter(nums)
        for val, count in hashmap.items():
            if count > n/2:
                return val

