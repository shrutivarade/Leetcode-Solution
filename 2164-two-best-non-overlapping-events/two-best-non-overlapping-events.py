# class Solution:
#     def maxTwoEvents(self, events: List[List[int]]) -> int:

#         maxSum = 0
#         events = sorted(events,key=lambda x: (x[0]))

#         for i in range(0,len(events)):
#             sum = events[i][2]
#             for j in range(i+1, len(events)):
#                 if events[j][0] >= events[i][1]+1 and events[i][2]+events[j][2]>sum:
#                     sum = events[i][2] + events[j][2]
#                     # break
#             maxSum = max(maxSum, sum)

#         return maxSum

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events.sort(key=lambda x: x[0])

        max_val = 0
        max_sum = 0

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum