class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [ i for i in range(n)]
        rank = [1] * n

        def find(n):
            curr = n
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1


        res = n
        for e1, e2 in edges:
            res -= union(e1,e2)
        
        return res