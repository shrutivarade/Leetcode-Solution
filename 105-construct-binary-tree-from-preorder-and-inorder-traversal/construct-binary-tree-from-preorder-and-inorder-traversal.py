# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if inorder == []:
            return

        root = TreeNode(preorder.pop(0))
        # print(root)

        index = inorder.index(root.val)
        # print(index)

        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])

        return root
        