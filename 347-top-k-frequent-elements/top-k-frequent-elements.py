
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]