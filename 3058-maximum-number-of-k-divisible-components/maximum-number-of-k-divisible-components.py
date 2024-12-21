# class Solution:
#     def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

class Solution:
    def maxKDivisibleComponents(self, n, edges, vals, k):
        from collections import deque, defaultdict
        
        if n < 2:
            return 1
        
        graph = defaultdict(list)
        degree = [0] * n
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        node_vals = vals[:]
        leaf_q = deque([i for i in range(n) if degree[i] == 1])
        comp_cnt = 0
        
        while leaf_q:
            curr = leaf_q.popleft()
            degree[curr] -= 1
            carry = 0
            
            if node_vals[curr] % k == 0:
                comp_cnt += 1
            else:
                carry = node_vals[curr]
            
            for nbr in graph[curr]:
                if degree[nbr] == 0:
                    continue
                degree[nbr] -= 1
                node_vals[nbr] += carry
                if degree[nbr] == 1:
                    leaf_q.append(nbr)
        
        return comp_cnt















        # reach the leaf node
        #  at leaf node, check for div

            # if div -> cut, pop, increment
            #  if not div -> merge to parent, pop

        # maxComp = 1
        # def dfs(currNode, maxComp, edges, k):

        #     # if the currNode is leaf Node
        #     adjnodes = []
        #     for edge in edges:
        #         if currnode in edge:
        #             adjnodes.append(for e in edge if e != currnode )




        


        # dfs(0, maxComp, edges, k)
        # return maxComp



        





















        # # Start with any node

        # # check if value for that node is divisible by k

        # # if yes then check 


        
        # def dfs(currnode):

        #     comp = [e for e in edges if currnode in e]

        #     adjnodes = [value for pair in comp for value in pair if value != currnode]
            
            
        #     if values[currnode]%k == 0:
        #         for adjnode in adjnodes:
        #             flag = dfs(adjnode)

        #             if flag :
        #                 maxCom+=1
        #             else:

            
        #     else:
        #         # add the adjnodes
        #         sum = value[currnode] + value[adjnodes[0]]
        #         # check divisibility

        #         # dfs on next adj nodes


        # dfs(0)

