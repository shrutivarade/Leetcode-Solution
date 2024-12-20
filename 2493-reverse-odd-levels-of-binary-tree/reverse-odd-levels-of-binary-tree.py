# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # using DFS
        currlevel = 0
        def dfs ( leftsubtree, rightsubtree, currlevel ):
            if not leftsubtree and not rightsubtree:
                return
            
            if currlevel % 2 == 0:

                temp = leftsubtree.val
                leftsubtree.val = rightsubtree.val
                rightsubtree.val= temp

            dfs( leftsubtree.left, rightsubtree.right, currlevel+1 )
            dfs( leftsubtree.right, rightsubtree.left, currlevel+1 )    
        
        dfs(root.left, root.right, currlevel)
        return root

        


        # Using array representation
        # if not root:
        #     return []
        # result = []
        # queue = deque([root])
        # while queue:
        #     level_size = len(queue)
        #     level = []
        #     while level_size:
        #         node = queue.popleft()
        #         if node:
        #             level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         level_size -= 1
        #     result.append(level)
        # for i in range(len(result)):
        #     if i%2 != 0:
        #         result[i] = result[i][::-1]
        # print(result)

        # # Create the root node
        # root = TreeNode(result[0][0])
        # current_level = [root]

        # # Build the tree level by level
        # for level in result[1:]:
        #     next_level = []
        #     i = 0
        #     for node in current_level:
        #         if i < len(level):
        #             node.left = TreeNode(level[i])
        #             next_level.append(node.left)
        #             i += 1
        #         if i < len(level):
        #             node.right = TreeNode(level[i])
        #             next_level.append(node.right)
        #             i += 1
        #     current_level = next_level

        # return root
