"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node: return node
        
        # q = deque([node])
        # clones  = {node.val: Node(node.val, [])}
        # while q:
        #     cur = q.popleft() 
        #     cur_clone = clones[cur.val]            

        #     for ngbr in cur.neighbors:
        #         if ngbr.val not in clones:
        #             clones[ngbr.val] = Node(ngbr.val, [])
        #             q.append(ngbr)
                    
        #         cur_clone.neighbors.append(clones[ngbr.val])
                
        # return clones[node.val]

        if not node:
            return None
        old_to_new = {None: None}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            for nei in node.neighbors:
                old_to_new[node].neighbors.append(dfs(nei))
            return old_to_new[node]

        return dfs(node)