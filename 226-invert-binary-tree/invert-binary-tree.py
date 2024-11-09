# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # edge case
        if not root:
            return

        # call dfs recursively on each node. left and right subtree
        # at each node swap its left and right subtree

        tempTree = root.left
        root.left = root.right
        root.right = tempTree

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root