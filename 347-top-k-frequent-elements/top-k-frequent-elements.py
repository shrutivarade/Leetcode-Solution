
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Generic way
        # counter = Counter(nums)
        # return [num for num, _ in counter.most_common(k)]


        # Using Priority queue and min heap
        freq_count= Counter(nums)
        min_heap=[]

        for num, freq in freq_count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap)> k:
                heapq.heappop(min_heap)
                
        return [num for freq, num in min_heap]

        # use this testcase: [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
