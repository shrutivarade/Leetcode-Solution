# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        

#         # [.5, .6, 1]

#         # [.5, .3, .8, .2]

#         # [.75, , , ] = 2.05/4 = 0.5125
#         # [ , .53, , ] = 2.03/4 = 0.5075
#         # [ , , .88, ] = 1.88/4 = 0.47
#         # [ , , ,.4] = 2/4 = 0.5

#         # [.5, .45, .8, .33] = 2.083 / 4 = 0.5208
#         # 0.53485*4 = 2.13
#         #  / 28+4 = 
    


#         ratio = []
#         passRatio = []
#         for c in classes:
#             ratio.append(c[0]/c[1])
#         idx = ratio.index(min(ratio))
#         classes[idx] = [classes[idx][0]+extraStudents, classes[idx][1]+extraStudents]
#         for c in classes:
#             passRatio.append(c[0]/c[1])
#         avg = sum(passRatio) / len(classes)
#         return avg

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        def gain(pass_, total):
            return (pass_ + 1) / (total + 1) - pass_ / total

        max_heap = []
        sum_ = 0.0

        for pass_, total in classes:
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        for _ in range(extraStudents):
            current_gain, pass_, total = heapq.heappop(max_heap)
            sum_ -= pass_ / total
            pass_ += 1
            total += 1
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        return sum_ / len(classes)