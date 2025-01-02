class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = {}

        for i, val in enumerate(nums):

            if val in hashmap:
                if abs(hashmap[val]-i)<=k:
                    return True
            
            hashmap[val] = i
            
        return False


                
        