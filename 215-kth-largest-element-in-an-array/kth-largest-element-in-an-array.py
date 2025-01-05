class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # nums.sort()
        # return nums[len(nums) - k]

        # Time complexity: O(nlogn)
        # Space complexity: O(sort)

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

        # Time complexity: O(nlogk)
        # Space complexity: O(k)