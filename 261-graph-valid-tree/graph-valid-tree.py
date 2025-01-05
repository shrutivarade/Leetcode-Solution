class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()
        adjlist = {i:[] for i in range(n)}

        for e in edges:
            adjlist[e[0]].append(e[1])
            adjlist[e[1]].append(e[0])

        def dfs(curr, prev):
            if curr in visited: # cyle detected
                return False

            visited.add(curr)
  
            for c in adjlist[curr]:
                if prev==c:
                    continue
                if not dfs(c, curr):
                    return False
                    
            return True

        return dfs(0, -1) and len(visited) == n
