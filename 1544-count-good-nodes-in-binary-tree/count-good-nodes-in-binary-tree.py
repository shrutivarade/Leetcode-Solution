# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, maxVal: int, count: int):

            if root == None:
                return count

            if(root.val >= maxVal):
                count+=1
                maxVal = root.val
            

            count = dfs(root.left, maxVal, count)
            count = dfs(root.right, maxVal, count)
            
            return count

        return dfs(root, root.val, 0)

    
