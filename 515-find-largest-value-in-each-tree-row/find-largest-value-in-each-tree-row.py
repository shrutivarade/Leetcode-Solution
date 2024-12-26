# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        levels = []
        queue = deque([root])

        while queue:
            size = len(queue)
            curr_level = []

            while size>0:
                node = queue.popleft()
                curr_level.append(node.val)

                if (node.left):
                    queue.append(node.left)
                
                if(node.right):
                    queue.append(node.right)
                
                size-=1
            levels.append(max(curr_level))

        return levels



















        # ans = []
        # queue = deque([root])
        
        # while queue:
        #     current_length = len(queue)
        #     curr_max = float("-inf")
            
        #     for _ in range(current_length):
        #         node = queue.popleft()
        #         curr_max = max(curr_max, node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     ans.append(curr_max)
        
        # return ans