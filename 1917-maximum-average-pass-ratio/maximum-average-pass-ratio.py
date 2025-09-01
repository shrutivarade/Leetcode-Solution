class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # gain(p,t) = (p+1)/(t+1) - p/t, we always add a student to the class with max gain
        def gain(p: int, t: int) -> float:
            # compute marginal improvement for adding one pass
            return (p + 1) / (t + 1) - p / t

        # max heap by gain, store as negative for heapq
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))  # push current gain and state

        # assign extra students greedily
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)       # get class with largest gain
            p += 1                               # add guaranteed pass student
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))  # push updated class

        # compute final average
        total = 0.0
        for _, p, t in heap:
            total += p / t
        return total / len(classes)