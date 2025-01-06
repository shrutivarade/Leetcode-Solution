
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # counter = Counter(nums)
        # return [num for num, _ in counter.most_common(k)]

        freq_count= Counter(nums)

        min_heap=[]

        for num, freq in freq_count.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap)> k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]
