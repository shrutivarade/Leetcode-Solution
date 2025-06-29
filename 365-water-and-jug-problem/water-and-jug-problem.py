class Solution:
    def operate_jug(self, action, maxX, maxY, curX, curY):
        if action == "fill_x":
            return maxX, curY
        elif action == "fill_y":
            return curX, maxY
        elif action == "pour_x":
            return 0, curY
        elif action == "pour_y":
            return curX, 0
        elif action == "x_to_y":
            return max(curX - min(maxY - curY, maxX), 0), min(curX + curY, maxY)
        elif action == "y_to_x":
            return min(curX + curY, maxX), max(curY - min(maxX - curX, maxY), 0)
        return 0, 0

    def canMeasureWater(self, x, y, target):
        if x + y == target or x == target or y == target:
            return True

        operations = ["fill_x", "fill_y", "pour_x", "pour_y", "y_to_x", "x_to_y"]
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            x1, y1 = queue.popleft()

            if (x1, y1) in visited:
                continue

            if x1 == target or y1 == target or x1 + y1 == target:
                return True

            visited.add((x1, y1))

            for operation in operations:
                next_state = self.operate_jug(operation, x, y, x1, y1)
                queue.append(next_state)

        return False

# class Solution:
#     def canMeasureWater(self, x: int, y: int, target: int) -> bool:
#         def XFillTank():
#             k=x
#         def XFillY():
#             if m<x-k: k=k+m
#             k=x
#         def XEmptyTank():
#             k=0
#         def XEmptyY():
#             diff=y-m
#             k=k-diff
#             m=m+diff
#             if k<0: k=0
#             if m>y: m=y
#         def YFillTank():
#             m=y
#         def YFillX():
#             if k<y-m: m=m+k
#             m=y
#         def YEmptyTank():
#             m=0
#         def YEmptyX():
#             diff=x-k
#             k=k+diff
#             m=m-diff
#             if m<0: m=0
#             if k>x: k=x

#         k=0
#         m=0




# class Solution:
#     def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

#         seen = set()

#         def dfs(tot):
#             if tot == targetCapacity:
#                 return True
#             if tot in seen or tot < 0 or tot > jug1Capacity + jug2Capacity:
#                 return False
            
#             seen.add(tot)

#             return dfs(tot+jug1Capacity) or dfs(tot-jug1Capacity) or dfs(tot+jug2Capacity) or dfs(tot-jug2Capacity)
        
#         return dfs(0)