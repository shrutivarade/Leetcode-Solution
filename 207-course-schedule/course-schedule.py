class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjmap = {i:[] for i in range(numCourses)}

        for p in prerequisites:
            adjmap[p[0]].append(p[1])

        visited = set()

        def dfs(i):

            if i in visited: #cycle detected
                return False
            
            if adjmap[i] == []:
                return True

            visited.add(i)
            for j in adjmap[i]:
                
                if not dfs(j): 
                    return False
            
            visited.remove(i)
            adjmap[i] = []
            return True


        for i in range(numCourses):
            if not dfs(i): return False
        return True


